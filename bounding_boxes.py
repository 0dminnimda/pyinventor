from pathlib import Path

from pyinventor import (
    Inventor,
    LoftDefinition,
    LoftFeature,
    ObjectCollection,
    Document,
    DrawingDocument,
    PartDocument,
    SketchImage,
    WorkPlane,
    Profile3D,
    Sketch3D,
    Sketch,
    Point2d,
    const,
    make_points,
    make_wire,
    cast_to,
    add_file,
    const,
    com,
)


def tight_bounding_box(body: com.SurfaceBody, tolerance_in_cm: float = 0) -> com.Box:
    # inspired by https://modthemachine.typepad.com/my_weblog/2017/06/getting-the-overall-size-of-parts.html
    """
    Calculates a tight bounding box around the input body.
    An optional tolerance argument is available.
    If not provided the best existing display mesh is used.
    """

    # If the tolerance is zero, use the best display mesh available
    if tolerance_in_cm <= 0:
        # Get the best display mesh available
        _, tols = body.GetExistingFacetTolerances()
        best_tol = min(tols)
        vert_count, facet_count, vert_coords, norm_vectors, vert_inds = body.GetExistingFacets(best_tol)
    else:
        # Calculate a new mesh based on the input tolerance
        vert_count, facet_count, vert_coords, norm_vectors, vert_inds = body.CalculateFacets(tolerance_in_cm)

    tg = body.Application.TransientGeometry

    # Calculate the range of the mesh
    small_pnt = tg.CreatePoint(vert_coords[0], vert_coords[1], vert_coords[2])
    large_pnt = tg.CreatePoint(vert_coords[0], vert_coords[1], vert_coords[2])

    for i in range(vert_count):
        vert_X = vert_coords[i * 3]
        vert_Y = vert_coords[i * 3 + 1]
        vert_Z = vert_coords[i * 3 + 2]

        if vert_X < small_pnt.X:
            small_pnt.X = vert_X

        if vert_Y < small_pnt.Y:
            small_pnt.Y = vert_Y

        if vert_Z < small_pnt.Z:
            small_pnt.Z = vert_Z

        if vert_X > large_pnt.X:
            large_pnt.X = vert_X

        if vert_Y > large_pnt.Y:
            large_pnt.Y = vert_Y

        if vert_Z > large_pnt.Z:
            large_pnt.Z = vert_Z

    # Create and return a BoundingBox3D as the result
    newBox = tg.CreateBox()
    newBox.MinPoint = small_pnt
    newBox.MaxPoint = large_pnt
    return newBox


inventor = Inventor.make(visible=True)
print(f"Running {inventor.Caption}")

file = Path(__file__).parent / "test" / ("part" + PartDocument.extention)
document = PartDocument.open(inventor, file)

body = inventor.CommandManager.Pick(const.kPartBodyFilter, "Выбери тело")
print(body.Name)

bnd_box = body.OrientedMinimumRangeBox

# Draw the bounding box using a sketch.
sk = Sketch3D.make(document)
lines = sk.SketchLines3D

tg = inventor.TransientGeometry

center = bnd_box.CornerPoint
p1 = tg.CreatePoint(
    center.X + bnd_box.DirectionOne.X,
    center.Y + bnd_box.DirectionOne.Y,
    center.Z + bnd_box.DirectionOne.Z,
)
p2 = tg.CreatePoint(
    center.X + bnd_box.DirectionTwo.X,
    center.Y + bnd_box.DirectionTwo.Y,
    center.Z + bnd_box.DirectionTwo.Z,
)
p3 = tg.CreatePoint(
    center.X + bnd_box.DirectionThree.X,
    center.Y + bnd_box.DirectionThree.Y,
    center.Z + bnd_box.DirectionThree.Z,
)

lines.AddByTwoPoints(center, p1)
lines.AddByTwoPoints(center, p2)
lines.AddByTwoPoints(center, p3)
