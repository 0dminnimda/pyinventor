# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]
# From type library '{D98A091D-3A0F-4C3E-B36E-61F62068D488}'
# On Mon Jul 17 12:29:47 2023
'Autodesk Inventor Object Library'
makepy_version = '0.5.01'
python_version = 0x30b02f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{D98A091D-3A0F-4C3E-B36E-61F62068D488}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class constants:
	kASideDefault                 =106241     # from enum ASideFaceStatusEnum
	kASideSick                    =106242     # from enum ASideFaceStatusEnum
	kASideUpToDate                =106243     # from enum ASideFaceStatusEnum
	kHigh                         =69379      # from enum AccuracyEnum
	kLow                          =69377      # from enum AccuracyEnum
	kMedium                       =69378      # from enum AccuracyEnum
	kVeryHigh                     =69380      # from enum AccuracyEnum
	kActivationAction             =2          # from enum ActionTypeEnum
	kAllActions                   =-1         # from enum ActionTypeEnum
	kDeleteAction                 =1          # from enum ActionTypeEnum
	kMoveAction                   =16         # from enum ActionTypeEnum
	kNoAction                     =0          # from enum ActionTypeEnum
	kReorderAction                =4          # from enum ActionTypeEnum
	kRestructureAction            =8          # from enum ActionTypeEnum
	kAddInLicenseStatusAvailable  =76290      # from enum AddInLicenseStatusEnum
	kAddInLicenseStatusUnavailable=76291      # from enum AddInLicenseStatusEnum
	kAddInLicenseStatusUnlicensed =76289      # from enum AddInLicenseStatusEnum
	kLoadBehaviorUnknown          =94727      # from enum AddInLoadBehaviorEnum
	kLoadImmediately              =94721      # from enum AddInLoadBehaviorEnum
	kLoadOnDemand                 =94726      # from enum AddInLoadBehaviorEnum
	kLoadWithAssemblies           =94723      # from enum AddInLoadBehaviorEnum
	kLoadWithDrawings             =94725      # from enum AddInLoadBehaviorEnum
	kLoadWithParts                =94722      # from enum AddInLoadBehaviorEnum
	kLoadWithPresentations        =94724      # from enum AddInLoadBehaviorEnum
	kHorizontalAlignment          =64257      # from enum AlignmentTypeEnum
	kVerticalAlignment            =64258      # from enum AlignmentTypeEnum
	kAdjacent                     =73473      # from enum AlternateUnitsDisplayTypeEnum
	kAdjacentWithBracketsForAlternate=73475      # from enum AlternateUnitsDisplayTypeEnum
	kAdjacentWithBracketsForPrimary=73474      # from enum AlternateUnitsDisplayTypeEnum
	kCrossSectionAnalysis         =73986      # from enum AnalysisTypeEnum
	kCurvatureAnalysis            =73987      # from enum AnalysisTypeEnum
	kDraftAnalysis                =73988      # from enum AnalysisTypeEnum
	kNoAnalysis                   =73985      # from enum AnalysisTypeEnum
	kSurfaceAnalysis              =73989      # from enum AnalysisTypeEnum
	kZebraAnalysis                =73990      # from enum AnalysisTypeEnum
	kDirectedSolution             =78593      # from enum AngleConstraintSolutionTypeEnum
	kReferenceVectorSolution      =78595      # from enum AngleConstraintSolutionTypeEnum
	kUndirectedSolution           =78594      # from enum AngleConstraintSolutionTypeEnum
	kDegreesAngularPrecision      =42250      # from enum AngularPrecisionEnum
	kEightDecimalPlacesAngularPrecision=42249      # from enum AngularPrecisionEnum
	kFiveDecimalPlacesAngularPrecision=42246      # from enum AngularPrecisionEnum
	kFourDecimalPlacesAngularPrecision=42245      # from enum AngularPrecisionEnum
	kMinutesAngularPrecision      =42251      # from enum AngularPrecisionEnum
	kOneDecimalPlaceAngularPrecision=42242      # from enum AngularPrecisionEnum
	kSecondsAngularPrecision      =42252      # from enum AngularPrecisionEnum
	kSecondsFourDecimalPlaceAngularPrecision=42256      # from enum AngularPrecisionEnum
	kSecondsOneDecimalPlaceAngularPrecision=42253      # from enum AngularPrecisionEnum
	kSecondsThreeDecimalPlaceAngularPrecision=42255      # from enum AngularPrecisionEnum
	kSecondsTwoDecimalPlaceAngularPrecision=42254      # from enum AngularPrecisionEnum
	kSevenDecimalPlacesAngularPrecision=42248      # from enum AngularPrecisionEnum
	kSixDecimalPlacesAngularPrecision=42247      # from enum AngularPrecisionEnum
	kThreeDecimalPlacesAngularPrecision=42244      # from enum AngularPrecisionEnum
	kTwoDecimalPlacesAngularPrecision=42243      # from enum AngularPrecisionEnum
	kZeroDecimalPlaceAngularPrecision=42241      # from enum AngularPrecisionEnum
	kBodyAppearance               =100611     # from enum AppearanceSourceTypeEnum
	kComponentOccurrenceAppearance=100615     # from enum AppearanceSourceTypeEnum
	kDefaultAppearance            =100616     # from enum AppearanceSourceTypeEnum
	kFeatureAppearance            =100610     # from enum AppearanceSourceTypeEnum
	kMaterialAppearance           =100614     # from enum AppearanceSourceTypeEnum
	kMeshFeatureAppearance        =100617     # from enum AppearanceSourceTypeEnum
	kOverrideAppearance           =100609     # from enum AppearanceSourceTypeEnum
	kPartAppearance               =100612     # from enum AppearanceSourceTypeEnum
	kWeldsAppearance              =100613     # from enum AppearanceSourceTypeEnum
	kPlugInApplicationAddIn       =1796       # from enum ApplicationAddInTypeEnum
	kStandardApplicationAddIn     =1794       # from enum ApplicationAddInTypeEnum
	kTranslationApplicationAddIn  =1795       # from enum ApplicationAddInTypeEnum
	kUnknownApplicationAddIn      =1793       # from enum ApplicationAddInTypeEnum
	kDarkColorTheme               =87042      # from enum ApplicationFrameColorTypeEnum
	kLightColorTheme              =87041      # from enum ApplicationFrameColorTypeEnum
	kAngleArcDimension            =65539      # from enum ArcDimensionTypeEnum
	kArcLengthArcDimension        =65540      # from enum ArcDimensionTypeEnum
	kChordLengthArcDimension      =65541      # from enum ArcDimensionTypeEnum
	kDiametricArcDimension        =65538      # from enum ArcDimensionTypeEnum
	kRadialArcDimension           =65537      # from enum ArcDimensionTypeEnum
	kAsStyleArrowheadType         =71937      # from enum ArrowheadTypeEnum
	kBlankArrowheadType           =71939      # from enum ArrowheadTypeEnum
	kCircleArrowheadType          =71947      # from enum ArrowheadTypeEnum
	kClosedArrowheadType          =71940      # from enum ArrowheadTypeEnum
	kDatum45BlankArrowheadType    =71956      # from enum ArrowheadTypeEnum
	kDatum45FilledArrowheadType   =71957      # from enum ArrowheadTypeEnum
	kDatum60BlankArrowheadType    =71954      # from enum ArrowheadTypeEnum
	kDatum60FilledArrowheadType   =71955      # from enum ArrowheadTypeEnum
	kFilledArrowheadType          =71941      # from enum ArrowheadTypeEnum
	kFlaredArrowheadType          =71944      # from enum ArrowheadTypeEnum
	kHalf1FilledArrowheadType     =71942      # from enum ArrowheadTypeEnum
	kHalf1FlaredArrowheadType     =71945      # from enum ArrowheadTypeEnum
	kHalf2FilledArrowheadType     =71943      # from enum ArrowheadTypeEnum
	kHalf2FlaredArrowheadType     =71946      # from enum ArrowheadTypeEnum
	kLargeDotArrowheadType        =71950      # from enum ArrowheadTypeEnum
	kNoneArrowheadType            =71948      # from enum ArrowheadTypeEnum
	kObliqueArrowheadType         =71951      # from enum ArrowheadTypeEnum
	kOpenArrowheadType            =71938      # from enum ArrowheadTypeEnum
	kOriginArrowheadType          =71952      # from enum ArrowheadTypeEnum
	kSmallDotArrowheadType        =71949      # from enum ArrowheadTypeEnum
	kThickLineArrowheadType       =71953      # from enum ArrowheadTypeEnum
	kBetweenTwoFacesOriginDefinitionType=106499     # from enum AssemblyJointOriginDefinitionTypeEnum
	kInferOriginDefinitionType    =106497     # from enum AssemblyJointOriginDefinitionTypeEnum
	kOffsetOriginDefinitionType   =106498     # from enum AssemblyJointOriginDefinitionTypeEnum
	kBallJointType                =102406     # from enum AssemblyJointTypeEnum
	kCylindricalJointType         =102404     # from enum AssemblyJointTypeEnum
	kPlanarJointType              =102405     # from enum AssemblyJointTypeEnum
	kRigidJointType               =102401     # from enum AssemblyJointTypeEnum
	kRotationalJointType          =102402     # from enum AssemblyJointTypeEnum
	kSlideJointType               =102403     # from enum AssemblyJointTypeEnum
	kTextureTypeBitmap            =99588      # from enum AssetTextureTypeEnum
	kTextureTypeChecker           =99585      # from enum AssetTextureTypeEnum
	kTextureTypeGradient          =99586      # from enum AssetTextureTypeEnum
	kTextureTypeMarble            =99589      # from enum AssetTextureTypeEnum
	kTextureTypeNoise             =99590      # from enum AssetTextureTypeEnum
	kTextureTypeSpeckle           =99591      # from enum AssetTextureTypeEnum
	kTextureTypeTile              =99587      # from enum AssetTextureTypeEnum
	kTextureTypeUnknown           =99594      # from enum AssetTextureTypeEnum
	kTextureTypeWave              =99592      # from enum AssetTextureTypeEnum
	kTextureTypeWood              =99593      # from enum AssetTextureTypeEnum
	kAssetTypeAppearance          =99073      # from enum AssetTypeEnum
	kAssetTypeMaterial            =99074      # from enum AssetTypeEnum
	kAssetTypePhysicalProperties  =99075      # from enum AssetTypeEnum
	kAssetTypeUnknown             =99076      # from enum AssetTypeEnum
	kAssetValueTextureType        =99336      # from enum AssetValueTypeEnum
	kAssetValueTypeBoolean        =99329      # from enum AssetValueTypeEnum
	kAssetValueTypeChoice         =99331      # from enum AssetValueTypeEnum
	kAssetValueTypeColor          =99335      # from enum AssetValueTypeEnum
	kAssetValueTypeFilename       =99334      # from enum AssetValueTypeEnum
	kAssetValueTypeFloat          =99332      # from enum AssetValueTypeEnum
	kAssetValueTypeInteger        =99330      # from enum AssetValueTypeEnum
	kAssetValueTypeReference      =99337      # from enum AssetValueTypeEnum
	kAssetValueTypeString         =99333      # from enum AssetValueTypeEnum
	kAssetValueUnknownType        =99338      # from enum AssetValueTypeEnum
	kElectricallyBondedConnectionType=93169      # from enum BIMCableTrayConnectionTypeEnum
	kUndefinedConnectionType      =93170      # from enum BIMCableTrayConnectionTypeEnum
	kModelOriginOrientationType   =103682     # from enum BIMComponentOrientationTypeEnum
	kUserCoordinateSystemOrientationType=103683     # from enum BIMComponentOrientationTypeEnum
	kViewCubeOrientationType      =103681     # from enum BIMComponentOrientationTypeEnum
	kCompressionConduitConnectionType=93153      # from enum BIMConduitConnectionTypeEnum
	kGluedConduitConnectionType   =93154      # from enum BIMConduitConnectionTypeEnum
	kSetScrewConduitConnectionType=93155      # from enum BIMConduitConnectionTypeEnum
	kThreadedConduitConnectionType=93156      # from enum BIMConduitConnectionTypeEnum
	kUndefinedConduitConnectionType=93157      # from enum BIMConduitConnectionTypeEnum
	kBIMCableTrayConnectorType    =92929      # from enum BIMConnectorDefinitionTypeEnum
	kBIMConduitConnectorType      =92930      # from enum BIMConnectorDefinitionTypeEnum
	kBIMDuctConnectorType         =92931      # from enum BIMConnectorDefinitionTypeEnum
	kBIMElectricalConnectorType   =92932      # from enum BIMConnectorDefinitionTypeEnum
	kBIMPipeConnectorType         =92933      # from enum BIMConnectorDefinitionTypeEnum
	kCircularShapeConnector       =92675      # from enum BIMConnectorShapeEnum
	kOvalShapeConnector           =92676      # from enum BIMConnectorShapeEnum
	kRectangularShapeConnector    =92674      # from enum BIMConnectorShapeEnum
	kUndefinedShapeConnector      =92673      # from enum BIMConnectorShapeEnum
	kBandedDuctConnectionType     =93137      # from enum BIMDuctConnectionTypeEnum
	kClippedDuctConnectionType    =93138      # from enum BIMDuctConnectionTypeEnum
	kFlangeDuctConnectionType     =93139      # from enum BIMDuctConnectionTypeEnum
	kMasticDuctConnectionType     =93140      # from enum BIMDuctConnectionTypeEnum
	kOverCollarDuctConnectionType =93141      # from enum BIMDuctConnectionTypeEnum
	kRawEdgeDuctConnectionType    =93142      # from enum BIMDuctConnectionTypeEnum
	kSlipDriveDuctConnectionType  =93143      # from enum BIMDuctConnectionTypeEnum
	kSlipJointDuctConnectionType  =93144      # from enum BIMDuctConnectionTypeEnum
	kUndefinedDuctConnectionType  =93145      # from enum BIMDuctConnectionTypeEnum
	kVanStoneDuctConnectionType   =93146      # from enum BIMDuctConnectionTypeEnum
	kCalculatedDuctFlowConfigurationType=93105      # from enum BIMDuctFlowConfigurationEnum
	kPresetDuctFlowConfigurationType=93106      # from enum BIMDuctFlowConfigurationEnum
	kSystemDuctFlowConfigurationType=93107      # from enum BIMDuctFlowConfigurationEnum
	kKCoefficientDuctLossMethodType=93122      # from enum BIMDuctLossMethodEnum
	kNoneDuctLossMethodType       =93121      # from enum BIMDuctLossMethodEnum
	kSpecificLossDuctLossMethodType=93123      # from enum BIMDuctLossMethodEnum
	kExhaustDuctSystemType        =93089      # from enum BIMDuctSystemTypeEnum
	kOtherDuctSystemType          =93090      # from enum BIMDuctSystemTypeEnum
	kReturnDuctSystemType         =93091      # from enum BIMDuctSystemTypeEnum
	kSupplyDuctSystemType         =93092      # from enum BIMDuctSystemTypeEnum
	kUndefinedDuctSystemType      =93093      # from enum BIMDuctSystemTypeEnum
	kLaggingPowerFactorStateType  =93057      # from enum BIMElectricalPowerFactorStateEnum
	kLeadingPowerFactorStateType  =93058      # from enum BIMElectricalPowerFactorStateEnum
	kCommunicationElectricalSystemType=93073      # from enum BIMElectricalSystemTypeEnum
	kControlsElectricalSystemType =93074      # from enum BIMElectricalSystemTypeEnum
	kDataElectricalSystemType     =93075      # from enum BIMElectricalSystemTypeEnum
	kFireAlarmElectricalSystemType=93076      # from enum BIMElectricalSystemTypeEnum
	kNurseCallElectricalSystemType=93077      # from enum BIMElectricalSystemTypeEnum
	kPowerBalancedElectricalSystemType=93078      # from enum BIMElectricalSystemTypeEnum
	kPowerUnbalancedElectricalSystemType=93079      # from enum BIMElectricalSystemTypeEnum
	kSecurityElectricalSystemType =93080      # from enum BIMElectricalSystemTypeEnum
	kTelephoneElectricalSystemType=93081      # from enum BIMElectricalSystemTypeEnum
	kUndefinedElectricalSystemType=93082      # from enum BIMElectricalSystemTypeEnum
	kBiDirectionalFlowDirectionType=93041      # from enum BIMFlowDirectionEnum
	kInFlowDirectionType          =93042      # from enum BIMFlowDirectionEnum
	kOutFlowDirectionType         =93043      # from enum BIMFlowDirectionEnum
	kBrazedPipeConnectionType     =93009      # from enum BIMPipeConnectionTypeEnum
	kButtWeldedPipeConnectionType =93010      # from enum BIMPipeConnectionTypeEnum
	kCapillaryPipeConnectionType  =93011      # from enum BIMPipeConnectionTypeEnum
	kCompressionPipeConnectionType=93012      # from enum BIMPipeConnectionTypeEnum
	kCouplingPipeConnectionType   =93013      # from enum BIMPipeConnectionTypeEnum
	kCrimpedPipeConnectionType    =93014      # from enum BIMPipeConnectionTypeEnum
	kFlangePipeConnectionType     =93015      # from enum BIMPipeConnectionTypeEnum
	kFusionPipeConnectionType     =93016      # from enum BIMPipeConnectionTypeEnum
	kGluedPipeConnectionType      =93017      # from enum BIMPipeConnectionTypeEnum
	kGroovedPipeConnectionType    =93018      # from enum BIMPipeConnectionTypeEnum
	kSlipJointPipeConnectionType  =93019      # from enum BIMPipeConnectionTypeEnum
	kSocketWeldedPipeConnectionType=93020      # from enum BIMPipeConnectionTypeEnum
	kSolderedPipeConnectionType   =93021      # from enum BIMPipeConnectionTypeEnum
	kThreadedPipeConnectionType   =93022      # from enum BIMPipeConnectionTypeEnum
	kUndefinedPipeConnectionType  =93023      # from enum BIMPipeConnectionTypeEnum
	kCalculatedFlowConfigurationType=92993      # from enum BIMPipeFlowConfigurationEnum
	kFixtureUnitsFlowConfigurationType=92996      # from enum BIMPipeFlowConfigurationEnum
	kPresetFlowConfigurationType  =92994      # from enum BIMPipeFlowConfigurationEnum
	kSystemFlowConfigurationType  =92995      # from enum BIMPipeFlowConfigurationEnum
	kKCoefficientPipeLossMethodType=92978      # from enum BIMPipeLossMethodEnum
	kNonePipeLossMethodType       =92977      # from enum BIMPipeLossMethodEnum
	kSpecificLossPipeLossMethodType=92979      # from enum BIMPipeLossMethodEnum
	kDomesticColdWaterPipeSystemType=92945      # from enum BIMPipeSystemTypeEnum
	kDomesticHotWaterPipeSystemType=92946      # from enum BIMPipeSystemTypeEnum
	kFireProtectionDryPipeSystemType=92947      # from enum BIMPipeSystemTypeEnum
	kFireProtectionOtherPipeSystemType=92948      # from enum BIMPipeSystemTypeEnum
	kFireProtectionPreActionPipeSystemType=92949      # from enum BIMPipeSystemTypeEnum
	kFireProtectionWetPipeSystemType=92950      # from enum BIMPipeSystemTypeEnum
	kHydronicReturnPipeSystemType =92951      # from enum BIMPipeSystemTypeEnum
	kHydronicSupplyPipeSystemType =92952      # from enum BIMPipeSystemTypeEnum
	kOtherPipeSystemType          =92953      # from enum BIMPipeSystemTypeEnum
	kSanitaryPipeSystemType       =92954      # from enum BIMPipeSystemTypeEnum
	kUndefinedPipeSystemType      =92955      # from enum BIMPipeSystemTypeEnum
	kEachBOMQuantity              =52225      # from enum BOMQuantityTypeEnum
	kParameterBOMQuantity         =52226      # from enum BOMQuantityTypeEnum
	kDefaultBOMStructure          =51969      # from enum BOMStructureEnum
	kInseparableBOMStructure      =51974      # from enum BOMStructureEnum
	kNormalBOMStructure           =51970      # from enum BOMStructureEnum
	kPhantomBOMStructure          =51971      # from enum BOMStructureEnum
	kPurchasedBOMStructure        =51973      # from enum BOMStructureEnum
	kReferenceBOMStructure        =51972      # from enum BOMStructureEnum
	kVariesBOMStructure           =51975      # from enum BOMStructureEnum
	kModelDataBOMViewType         =62465      # from enum BOMViewTypeEnum
	kPartsOnlyBOMViewType         =62467      # from enum BOMViewTypeEnum
	kStructuredBOMViewType        =62466      # from enum BOMViewTypeEnum
	kCullCCW                      =96771      # from enum BackFaceCullingEnum
	kCullCW                       =96770      # from enum BackFaceCullingEnum
	kCullNone                     =96769      # from enum BackFaceCullingEnum
	kGradientBackgroundType       =52738      # from enum BackgroundTypeEnum
	kImageBackgroundType          =52739      # from enum BackgroundTypeEnum
	kOneColorBackgroundType       =52737      # from enum BackgroundTypeEnum
	kBottomDirection              =48386      # from enum BalloonDirectionEnum
	kLeftDirection                =48387      # from enum BalloonDirectionEnum
	kRightDirection               =48388      # from enum BalloonDirectionEnum
	kTopDirection                 =48385      # from enum BalloonDirectionEnum
	kCircularWithOneEntryBalloonType=48129      # from enum BalloonTypeEnum
	kCircularWithTwoEntriesBalloonType=48130      # from enum BalloonTypeEnum
	kHexagonBalloonType           =48131      # from enum BalloonTypeEnum
	kLinearBalloonType            =48132      # from enum BalloonTypeEnum
	kNoneBalloonType              =48133      # from enum BalloonTypeEnum
	kRectangleBalloonType         =48135      # from enum BalloonTypeEnum
	kSketchedSymbolBalloonType    =48134      # from enum BalloonTypeEnum
	kBarControlButton             =22785      # from enum BarControlTypeEnum
	kBarControlPopUp              =22786      # from enum BarControlTypeEnum
	kCompositeOutputType          =90115      # from enum BaseFeatureOutputTypeEnum
	kSolidOutputType              =90114      # from enum BaseFeatureOutputTypeEnum
	kSurfaceOutputType            =90113      # from enum BaseFeatureOutputTypeEnum
	kBendingAngleType             =81665      # from enum BendAngleTypeEnum
	kDefaultAngleType             =81667      # from enum BendAngleTypeEnum
	kOpenAngleType                =81666      # from enum BendAngleTypeEnum
	kCenterlineOfBend             =75777      # from enum BendLocationEnum
	kEndOfBend                    =75779      # from enum BendLocationEnum
	kStartOfBend                  =75778      # from enum BendLocationEnum
	kDefaultBendOrder             =151021569  # from enum BendOrderSourceTypeEnum
	kDuplicateOverrideBendOrder   =151021571  # from enum BendOrderSourceTypeEnum
	kOverrideBendOrder            =151021570  # from enum BendOrderSourceTypeEnum
	kArcLengthAndAngleBendPart    =83457      # from enum BendPartTypeEnum
	kRadiusAndAngleBendPart       =83458      # from enum BendPartTypeEnum
	kRadiusAndArcLengthBendPart   =83459      # from enum BendPartTypeEnum
	kBendPositionAdjacentFace     =75010      # from enum BendPositionEnum
	kBendPositionInnerEdgeOffset  =75013      # from enum BendPositionEnum
	kBendPositionInsideBendFace   =75011      # from enum BendPositionEnum
	kBendPositionOuterEdgeOffset  =75014      # from enum BendPositionEnum
	kBendPositionOutsideBaseFace  =75009      # from enum BendPositionEnum
	kBendPositionTangentToSideFace=75012      # from enum BendPositionEnum
	kDefaultBendReliefShape       =27907      # from enum BendReliefShapeEnum
	kRoundBendReliefShape         =27906      # from enum BendReliefShapeEnum
	kStraightBendReliefShape      =27905      # from enum BendReliefShapeEnum
	kTearBendReliefShape          =27908      # from enum BendReliefShapeEnum
	kArcBendTransition            =28164      # from enum BendTransitionEnum
	kDefaultBendTransition        =28165      # from enum BendTransitionEnum
	kIntersectionBendTransition   =28162      # from enum BendTransitionEnum
	kNoBendTransition             =28161      # from enum BendTransitionEnum
	kStraightLineBendTransition   =28163      # from enum BendTransitionEnum
	kTrimToBendBendTransition     =28166      # from enum BendTransitionEnum
	kBooleanTypeDifference        =74241      # from enum BooleanTypeEnum
	kBooleanTypeIntersect         =74243      # from enum BooleanTypeEnum
	kBooleanTypeUnion             =74242      # from enum BooleanTypeEnum
	kBorderLabelModeAlphabetical  =29953      # from enum BorderLabelModeEnum
	kBorderLabelModeNone          =29955      # from enum BorderLabelModeEnum
	kBorderLabelModeNumeric       =29954      # from enum BorderLabelModeEnum
	kHeadBossType                 =94210      # from enum BossTypeEnum
	kThreadBossType               =94209      # from enum BossTypeEnum
	kContinuousBoundaryPatchCondition=63491      # from enum BoundaryPatchConditionEnum
	kFreeBoundaryPatchCondition   =63489      # from enum BoundaryPatchConditionEnum
	kTangentBoundaryPatchCondition=63490      # from enum BoundaryPatchConditionEnum
	kHorizontalBreakOrientation   =84225      # from enum BreakOrientationEnum
	kVerticalBreakOrientation     =84226      # from enum BreakOrientationEnum
	kFromPointBreakOutType        =117492737  # from enum BreakOutDepthTypeEnum
	kThroughPartBreakOutType      =117492740  # from enum BreakOutDepthTypeEnum
	kToHoleBreakOutType           =117492739  # from enum BreakOutDepthTypeEnum
	kToSketchBreakOutType         =117492738  # from enum BreakOutDepthTypeEnum
	kRectangularBreakStyle        =84481      # from enum BreakStyleEnum
	kStructuralBreakStyle         =84482      # from enum BreakStyleEnum
	kActivateDisplayState         =46850      # from enum BrowserNodeDisplayStateEnum
	kAdaptiveDisplayState         =46858      # from enum BrowserNodeDisplayStateEnum
	kAdaptiveErrorDisplayState    =46860      # from enum BrowserNodeDisplayStateEnum
	kAdaptiveWarningDisplayState  =46859      # from enum BrowserNodeDisplayStateEnum
	kBoldDisplayState             =46868      # from enum BrowserNodeDisplayStateEnum
	kCheckBoxDisplayState         =46855      # from enum BrowserNodeDisplayStateEnum
	kComatoseDisplayState         =46853      # from enum BrowserNodeDisplayStateEnum
	kContactSetDisplayState       =46861      # from enum BrowserNodeDisplayStateEnum
	kCyclicDisplayState           =46865      # from enum BrowserNodeDisplayStateEnum
	kDefaultDisplayState          =46849      # from enum BrowserNodeDisplayStateEnum
	kExcludeDisplayState          =46866      # from enum BrowserNodeDisplayStateEnum
	kGrayCheckBoxDisplayState     =46867      # from enum BrowserNodeDisplayStateEnum
	kGreenCheckDisplayState       =46869      # from enum BrowserNodeDisplayStateEnum
	kIndependantAdaptivityDisplayState=46863      # from enum BrowserNodeDisplayStateEnum
	kReferencedDocNeedsUpdateDisplayState=46864      # from enum BrowserNodeDisplayStateEnum
	kRollbackEditDisplayState     =46851      # from enum BrowserNodeDisplayStateEnum
	kSickDisplayState             =46852      # from enum BrowserNodeDisplayStateEnum
	kSuppressDisplayState         =46854      # from enum BrowserNodeDisplayStateEnum
	kUnresolvedDisplayState       =46856      # from enum BrowserNodeDisplayStateEnum
	kUpdateRequiredDisplayState   =46857      # from enum BrowserNodeDisplayStateEnum
	kYellowCheckBoxDisplayState   =46862      # from enum BrowserNodeDisplayStateEnum
	kAlwaysDisplayText            =43010      # from enum ButtonDisplayEnum
	kDisplayTextInLearningMode    =43011      # from enum ButtonDisplayEnum
	kNoTextWithIcon               =43009      # from enum ButtonDisplayEnum
	kAcceptButtonType             =2          # from enum ButtonTypeEnum
	kCancelButtonType             =1          # from enum ButtonTypeEnum
	kEditButtonType               =4          # from enum ButtonTypeEnum
	kNoneCachedGraphics           =103169     # from enum CachedGraphicsStatusEnum
	kOutOfDateCachedGraphics      =103170     # from enum CachedGraphicsStatusEnum
	kUpToDateCachedGraphics       =103171     # from enum CachedGraphicsStatusEnum
	kBisectorCenterlineType       =62978      # from enum CenterlineTypeEnum
	kCenteredPatternCenterlineType=62980      # from enum CenterlineTypeEnum
	kRegularCenterlineType        =62977      # from enum CenterlineTypeEnum
	kWorkFeatureCenterlineType    =62979      # from enum CenterlineTypeEnum
	kCenterOfGravityCentermarkType=63237      # from enum CentermarkTypeEnum
	kPunchFeatureCentermarkType   =63238      # from enum CentermarkTypeEnum
	kRecoveredPunchFeatureCentermarkType=63239      # from enum CentermarkTypeEnum
	kRegularCentermarkType        =63233      # from enum CentermarkTypeEnum
	kWorkFeatureCentermarkType    =63234      # from enum CentermarkTypeEnum
	kDistance                     =26881      # from enum ChamferDefinitionTypeEnum
	kDistanceAndAngle             =26882      # from enum ChamferDefinitionTypeEnum
	kTwoDistances                 =26883      # from enum ChamferDefinitionTypeEnum
	kDiametricCircleDimension     =65793      # from enum CircleDimensionTypeEnum
	kRadialCircleDimension        =65794      # from enum CircleDimensionTypeEnum
	kPreviewClientGraphics        =45314      # from enum ClientGraphicsTypeEnum
	kTransientClientGraphics      =45313      # from enum ClientGraphicsTypeEnum
	kOverallColor                 =19460      # from enum ColorBindingEnum
	kPerItemColors                =19459      # from enum ColorBindingEnum
	kPerStripColors               =19458      # from enum ColorBindingEnum
	kPerVertexColors              =19457      # from enum ColorBindingEnum
	kAutomaticColorSource         =79106      # from enum ColorSourceTypeEnum
	kLayerColorSource             =79107      # from enum ColorSourceTypeEnum
	kOverrideColorSource          =79105      # from enum ColorSourceTypeEnum
	kSheetColorSource             =79108      # from enum ColorSourceTypeEnum
	kBlueTutorialIndicator        =50454562   # from enum ColorStyleEnum
	kRedTutorialIndicator         =50454563   # from enum ColorStyleEnum
	kYellowTutorialIndicator      =50454561   # from enum ColorStyleEnum
	kButtonPopupCommandBar        =43269      # from enum CommandBarTypeEnum
	kPopUpCommandBar              =43266      # from enum CommandBarTypeEnum
	kRegularCommandBar            =43265      # from enum CommandBarTypeEnum
	kSplitButtonCommandBar        =43267      # from enum CommandBarTypeEnum
	kSplitButtonMRUCommandBar     =43268      # from enum CommandBarTypeEnum
	kAddParametersCommand         =2342       # from enum CommandIDEnum
	kAddPointCommand              =2080       # from enum CommandIDEnum
	kAddPolygonCommand            =2059       # from enum CommandIDEnum
	kAnimateCommand               =2196       # from enum CommandIDEnum
	kCenterPointArcCommand        =2073       # from enum CommandIDEnum
	kCenterPointCircleCommand     =2068       # from enum CommandIDEnum
	kConsCoincidentCommand        =2097       # from enum CommandIDEnum
	kConsCollinearCommand         =2099       # from enum CommandIDEnum
	kConsConcentricCommand        =2098       # from enum CommandIDEnum
	kConsEqualCommand             =2102       # from enum CommandIDEnum
	kConsFixCommand               =2103       # from enum CommandIDEnum
	kConsHorizontalCommand        =2100       # from enum CommandIDEnum
	kConsParallelCommand          =2089       # from enum CommandIDEnum
	kConsPerpendicularCommand     =2088       # from enum CommandIDEnum
	kConsSymmetricCommand         =2371       # from enum CommandIDEnum
	kConsTangentCommand           =2096       # from enum CommandIDEnum
	kConsVerticalCommand          =2101       # from enum CommandIDEnum
	kCreate3DBendCommand          =2361       # from enum CommandIDEnum
	kCreate3DLineCommand          =2360       # from enum CommandIDEnum
	kCreate3DSketchCommand        =2167       # from enum CommandIDEnum
	kCreate3QuarterSectionViewCommand=2183       # from enum CommandIDEnum
	kCreateAreaFillCommand        =2108       # from enum CommandIDEnum
	kCreateAutoDimCommand         =2162       # from enum CommandIDEnum
	kCreateAuxiliaryViewCommand   =2199       # from enum CommandIDEnum
	kCreateBaselineDimensionCommand=2079       # from enum CommandIDEnum
	kCreateBendCommand            =2150       # from enum CommandIDEnum
	kCreateBreakoutViewCommand    =2122       # from enum CommandIDEnum
	kCreateBrokenViewCommand      =2076       # from enum CommandIDEnum
	kCreateCaterpillarCommand     =2111       # from enum CommandIDEnum
	kCreateCenterLineBisectorCommand=2313       # from enum CommandIDEnum
	kCreateCenterLineCommand      =2310       # from enum CommandIDEnum
	kCreateCenterMarkCommand      =2309       # from enum CommandIDEnum
	kCreateCenteredPatternCommand =2320       # from enum CommandIDEnum
	kCreateChamferCommand         =2117       # from enum CommandIDEnum
	kCreateCircularPatternCommand =2131       # from enum CommandIDEnum
	kCreateCoilCommand            =2115       # from enum CommandIDEnum
	kCreateComponentCommand       =2168       # from enum CommandIDEnum
	kCreateContourFlangeCommand   =2161       # from enum CommandIDEnum
	kCreateCornerChamferCommand   =2152       # from enum CommandIDEnum
	kCreateCornerRoundCommand     =2151       # from enum CommandIDEnum
	kCreateCornerSeamCommand      =2149       # from enum CommandIDEnum
	kCreateCutCommand             =2147       # from enum CommandIDEnum
	kCreateDecalCommand           =2107       # from enum CommandIDEnum
	kCreateDerivedPartCommand     =2129       # from enum CommandIDEnum
	kCreateDesignElementCommand   =2121       # from enum CommandIDEnum
	kCreateDetailViewCommand      =2201       # from enum CommandIDEnum
	kCreateDraftViewCommand       =2304       # from enum CommandIDEnum
	kCreateDrawingViewCommand     =2197       # from enum CommandIDEnum
	kCreateEmbossCommand          =2094       # from enum CommandIDEnum
	kCreateEndTreatmentCommand    =2123       # from enum CommandIDEnum
	kCreateEquationParamCommand   =2061       # from enum CommandIDEnum
	kCreateExtrudeCommand         =2050       # from enum CommandIDEnum
	kCreateFaceCommand            =2146       # from enum CommandIDEnum
	kCreateFaceDraftCommand       =2118       # from enum CommandIDEnum
	kCreateFilletCommand          =2116       # from enum CommandIDEnum
	kCreateFlangeCommand          =2148       # from enum CommandIDEnum
	kCreateFlatPatternCommand     =2145       # from enum CommandIDEnum
	kCreateFoldCommand            =2160       # from enum CommandIDEnum
	kCreateGeneralDimensionCommand=2306       # from enum CommandIDEnum
	kCreateGroundedWorkPointCommand=2095       # from enum CommandIDEnum
	kCreateHalfSectionViewCommand =2182       # from enum CommandIDEnum
	kCreateHemCommand             =2153       # from enum CommandIDEnum
	kCreateHoleCommand            =2113       # from enum CommandIDEnum
	kCreateHoleTableFromViewCommand=2077       # from enum CommandIDEnum
	kCreateHoleTableGroupCommand  =2210       # from enum CommandIDEnum
	kCreateInterfaceCommand       =2178       # from enum CommandIDEnum
	kCreateIntersectionCurveCommand=2372       # from enum CommandIDEnum
	kCreateKnitSurfaceCommand     =2092       # from enum CommandIDEnum
	kCreateLoftCommand            =2053       # from enum CommandIDEnum
	kCreateMateConstraintCommand  =2078       # from enum CommandIDEnum
	kCreateMirrorCommand          =2132       # from enum CommandIDEnum
	kCreateNewSheetCommand        =2305       # from enum CommandIDEnum
	kCreateOrdinateDimensionCommand=2307       # from enum CommandIDEnum
	kCreatePresentationViewCommand=2193       # from enum CommandIDEnum
	kCreateProjectedViewCommand   =2198       # from enum CommandIDEnum
	kCreatePunchCommand           =2075       # from enum CommandIDEnum
	kCreateQuarterSectionViewCommand=2181       # from enum CommandIDEnum
	kCreateRectPatternCommand     =2130       # from enum CommandIDEnum
	kCreateRevisionTableCommand   =2125       # from enum CommandIDEnum
	kCreateRevisionTagCommand     =2126       # from enum CommandIDEnum
	kCreateRevolveCommand         =2051       # from enum CommandIDEnum
	kCreateRibCommand             =2064       # from enum CommandIDEnum
	kCreateSectionViewCommand     =2200       # from enum CommandIDEnum
	kCreateSelectedHoleTableCommand=2226       # from enum CommandIDEnum
	kCreateShellCommand           =2114       # from enum CommandIDEnum
	kCreateSingleOrdinateDimCommand=2369       # from enum CommandIDEnum
	kCreateSketchChamferCommand   =2163       # from enum CommandIDEnum
	kCreateSketchCommand          =2049       # from enum CommandIDEnum
	kCreateSketchMirrorCommand    =2060       # from enum CommandIDEnum
	kCreateSplitCommand           =2119       # from enum CommandIDEnum
	kCreateSweepCommand           =2052       # from enum CommandIDEnum
	kCreateTextCommand            =2106       # from enum CommandIDEnum
	kCreateTextStylesCommand      =2062       # from enum CommandIDEnum
	kCreateThreadCommand          =2164       # from enum CommandIDEnum
	kCreateUnsectionedViewCommand =2184       # from enum CommandIDEnum
	kCreateWeldSymbolCommand      =2322       # from enum CommandIDEnum
	kCreateWorkAxisCommand        =2134       # from enum CommandIDEnum
	kCreateWorkPlaneCommand       =2133       # from enum CommandIDEnum
	kCreateWorkPointCommand       =2135       # from enum CommandIDEnum
	kDefaultCommand               =2048       # from enum CommandIDEnum
	kDeleteFaceCommand            =2090       # from enum CommandIDEnum
	kDeselAuthorCommand           =2359       # from enum CommandIDEnum
	kDesignViewsCommand           =2192       # from enum CommandIDEnum
	kEditFixedWorkPointCommand    =2127       # from enum CommandIDEnum
	kEditSketchCoordCommand       =2065       # from enum CommandIDEnum
	kEditThreadCommand            =2165       # from enum CommandIDEnum
	kEditTweaksCommand            =2312       # from enum CommandIDEnum
	kEditViewCommand              =2124       # from enum CommandIDEnum
	kEllipseCommand               =2070       # from enum CommandIDEnum
	kExtendBodyCommand            =2137       # from enum CommandIDEnum
	kFileOpenCommand              =2057       # from enum CommandIDEnum
	kFileSaveCommand              =2140       # from enum CommandIDEnum
	kFileSaveCopyAsCommand        =2056       # from enum CommandIDEnum
	kFillHatchSketchRegionCommand =2166       # from enum CommandIDEnum
	kFormatDimStylesCommand       =2370       # from enum CommandIDEnum
	kIncludeGeometry3DCommand     =2368       # from enum CommandIDEnum
	kInsertBalloonAllCommand      =2340       # from enum CommandIDEnum
	kInsertBalloonCommand         =2339       # from enum CommandIDEnum
	kInsertDatumIdentifierCommand =2325       # from enum CommandIDEnum
	kInsertDatumTargetCircleCommand=2327       # from enum CommandIDEnum
	kInsertDatumTargetLeaderCommand=2326       # from enum CommandIDEnum
	kInsertDatumTargetLineCommand =2328       # from enum CommandIDEnum
	kInsertDatumTargetPointCommand=2329       # from enum CommandIDEnum
	kInsertDatumTargetRectCommand =2336       # from enum CommandIDEnum
	kInsertDesignElementCommand   =2128       # from enum CommandIDEnum
	kInsertFeatureControlFrameCommand=2323       # from enum CommandIDEnum
	kInsertFeatureIdentifierCommand=2324       # from enum CommandIDEnum
	kInsertHoleNotesCommand       =2308       # from enum CommandIDEnum
	kInsertImageCommand           =2109       # from enum CommandIDEnum
	kInsertImportCommand          =2074       # from enum CommandIDEnum
	kInsertLeaderTextCommand      =2338       # from enum CommandIDEnum
	kInsertPartsListCommand       =2341       # from enum CommandIDEnum
	kInsertSurfaceTextureCommand  =2321       # from enum CommandIDEnum
	kInsertTableCommand           =2373       # from enum CommandIDEnum
	kInsertTextCommand            =2337       # from enum CommandIDEnum
	kLineCommand                  =2066       # from enum CommandIDEnum
	kLookAtViewCommand            =2355       # from enum CommandIDEnum
	kMeasureCommand               =2058       # from enum CommandIDEnum
	kModifyStandardSettingsCommand=2242       # from enum CommandIDEnum
	kMoveComponentCommand         =2179       # from enum CommandIDEnum
	kMoveFaceCommand              =2136       # from enum CommandIDEnum
	kPanCommand                   =2353       # from enum CommandIDEnum
	kPatternComponentCommand      =2169       # from enum CommandIDEnum
	kPlaceComponentCommand        =2054       # from enum CommandIDEnum
	kPlaceConstraintCommand       =2176       # from enum CommandIDEnum
	kPopupBrowserFiltersCommand   =2185       # from enum CommandIDEnum
	kPreciseViewRotationCommand   =2195       # from enum CommandIDEnum
	kProjectCutEdgesCommand       =2112       # from enum CommandIDEnum
	kProjectGeometryCommand       =2105       # from enum CommandIDEnum
	kProjectViewEdgesCommand      =2110       # from enum CommandIDEnum
	kPushBackLocalBOMItemNumbersCommand=2139       # from enum CommandIDEnum
	kRebuildPartCommand           =2055       # from enum CommandIDEnum
	kRefreshViewCommand           =2138       # from enum CommandIDEnum
	kReplaceAllComponentsCommand  =2170       # from enum CommandIDEnum
	kReplaceComponentCommand      =2177       # from enum CommandIDEnum
	kReplaceFaceCommand           =2091       # from enum CommandIDEnum
	kRotateCommand                =2354       # from enum CommandIDEnum
	kRotateComponentCommand       =2180       # from enum CommandIDEnum
	kRotateViewCommand            =2311       # from enum CommandIDEnum
	kSheetMetalSettingsCommand    =2144       # from enum CommandIDEnum
	kShowConstraintsCommand       =2104       # from enum CommandIDEnum
	kSketchExtendCommand          =2084       # from enum CommandIDEnum
	kSketchFilletCommand          =2083       # from enum CommandIDEnum
	kSketchGeneralDimCommand      =2087       # from enum CommandIDEnum
	kSketchOffsetCommand          =2086       # from enum CommandIDEnum
	kSketchTrimCommand            =2085       # from enum CommandIDEnum
	kSplineCommand                =2067       # from enum CommandIDEnum
	kTangentArcCommand            =2072       # from enum CommandIDEnum
	kTangentCircleCommand         =2069       # from enum CommandIDEnum
	kThickenCommand               =2093       # from enum CommandIDEnum
	kThreePointArcCommand         =2071       # from enum CommandIDEnum
	kThreePointRectangleCommand   =2082       # from enum CommandIDEnum
	kTweakComponentsCommand       =2194       # from enum CommandIDEnum
	kTwoPointRectangleCommand     =2081       # from enum CommandIDEnum
	kViewCatalogCommand           =2120       # from enum CommandIDEnum
	kViewHiddenEdgeCommand        =2357       # from enum CommandIDEnum
	kViewShadedCommand            =2358       # from enum CommandIDEnum
	kViewWireframeCommand         =2356       # from enum CommandIDEnum
	kZoomAllCommand               =2344       # from enum CommandIDEnum
	kZoomCommand                  =2343       # from enum CommandIDEnum
	kZoomSelectCommand            =2352       # from enum CommandIDEnum
	kZoomWindowCommand            =2345       # from enum CommandIDEnum
	kEditMaskCmdType              =57         # from enum CommandTypesEnum
	kFileOperationsCmdType        =4          # from enum CommandTypesEnum
	kFilePropertyEditCmdType      =8          # from enum CommandTypesEnum
	kNonShapeEditCmdType          =32         # from enum CommandTypesEnum
	kQueryOnlyCmdType             =2          # from enum CommandTypesEnum
	kReferencesChangeCmdType      =64         # from enum CommandTypesEnum
	kSchemaChangeCmdType          =128        # from enum CommandTypesEnum
	kShapeEditCmdType             =1          # from enum CommandTypesEnum
	kUpdateWithReferencesCmdType  =16         # from enum CommandTypesEnum
	kEqualToComparisonType        =60417      # from enum ComparisonTypeEnum
	kGreaterThanComparisonType    =60420      # from enum ComparisonTypeEnum
	kGreaterThanOrEqualToComparisonType=60422      # from enum ComparisonTypeEnum
	kLessThanComparisonType       =60419      # from enum ComparisonTypeEnum
	kLessThanOrEqualToComparisonType=60421      # from enum ComparisonTypeEnum
	kNotEqualToComparisonType     =60418      # from enum ComparisonTypeEnum
	kIncrementAsAmountOfValue     =94465      # from enum ConstraintIncrementTypeEnum
	kIncrementAsNumberOfSteps     =94466      # from enum ConstraintIncrementTypeEnum
	kHorizontalAndVertical        =104962     # from enum ConstraintInferencePriorityEnum
	kParallelAndPerpendicular     =104961     # from enum ConstraintInferencePriorityEnum
	kHorizontalAndVerticalPriority=50434      # from enum ConstraintPriorityEnum
	kNonePriority                 =50435      # from enum ConstraintPriorityEnum
	kParallelAndPerpendicularPriority=50433      # from enum ConstraintPriorityEnum
	kFullyConstrainedConstraintStatus=51713      # from enum ConstraintStatusEnum
	kOverConstrainedConstraintStatus=51715      # from enum ConstraintStatusEnum
	kUnderConstrainedConstraintStatus=51714      # from enum ConstraintStatusEnum
	kUnknownConstraintStatus      =51716      # from enum ConstraintStatusEnum
	kInsideContainment            =30978      # from enum ContainmentEnum
	kOnContainment                =30979      # from enum ContainmentEnum
	kOutsideContainment           =30980      # from enum ContainmentEnum
	kUnknownContainment           =30977      # from enum ContainmentEnum
	kInventorDesktopAccess        =81153      # from enum ContentCenterAccessOptionEnum
	kVaultOrProductstreamServerAccess=81154      # from enum ContentCenterAccessOptionEnum
	kCCDecimalMarkerOptionComma   =82435      # from enum ContentCenterDecimalMarkerOptionEnum
	kCCDecimalMarkerOptionDefault =82433      # from enum ContentCenterDecimalMarkerOptionEnum
	kCCDecimalMarkerOptionPeriod  =82434      # from enum ContentCenterDecimalMarkerOptionEnum
	kNewer                        =2          # from enum ContentCenterInstanceStatusEnum
	kNotFound                     =8          # from enum ContentCenterInstanceStatusEnum
	kOlder                        =1          # from enum ContentCenterInstanceStatusEnum
	kUpToDate                     =4          # from enum ContentCenterInstanceStatusEnum
	kRSCFamilyHealthMissingCatParamMap=80179      # from enum ContentCenterRSCResultEnum
	kRSCFamilyHealthOutOfDateWithAuthorTableAndCategory=80183      # from enum ContentCenterRSCResultEnum
	kRSCFamilyHealthOutOfDateWithCategory=80181      # from enum ContentCenterRSCResultEnum
	kRSCFamilyHealthOutOfDateWithTable=80180      # from enum ContentCenterRSCResultEnum
	kRSCFamilyHealthOutOfDateWithTableAndCategory=80182      # from enum ContentCenterRSCResultEnum
	kRSCFamilyHealthRequiresReAuthor=80177      # from enum ContentCenterRSCResultEnum
	kRSCFamilyHealthTableUpdateIncomplete=80178      # from enum ContentCenterRSCResultEnum
	kRSCInstancingDifferentFamily =80195      # from enum ContentCenterRSCResultEnum
	kRSCInstancingDifferentMember =80196      # from enum ContentCenterRSCResultEnum
	kRSCInstancingFeatureSuppressFail=80199      # from enum ContentCenterRSCResultEnum
	kRSCInstancingInvalidMemberValue=80202      # from enum ContentCenterRSCResultEnum
	kRSCInstancingLongFilename    =80198      # from enum ContentCenterRSCResultEnum
	kRSCInstancingMaterialNotFound=80197      # from enum ContentCenterRSCResultEnum
	kRSCInstancingMissingFileWritePermission=80194      # from enum ContentCenterRSCResultEnum
	kRSCInstancingThreadCreateFail=80201      # from enum ContentCenterRSCResultEnum
	kRSCInstancingThreadFeatureNotFound=80200      # from enum ContentCenterRSCResultEnum
	kRSCInstancingUnknownError    =80193      # from enum ContentCenterRSCResultEnum
	kRSCNoError                   =80129      # from enum ContentCenterRSCResultEnum
	kRSCNoTPAddInLoadedForTPPart  =80162      # from enum ContentCenterRSCResultEnum
	kRSCPartIsTPPipe              =80161      # from enum ContentCenterRSCResultEnum
	kRSCReplaceFailed             =80209      # from enum ContentCenterRSCResultEnum
	kRSCUnknownFailed             =80145      # from enum ContentCenterRSCResultEnum
	kContentFeatureFamily         =2          # from enum ContentFamilyTypeEnum
	kContentPartFamily            =1          # from enum ContentFamilyTypeEnum
	kContentCategoryType          =57089      # from enum ContentItemTypeEnum
	kContentFamilyType            =57090      # from enum ContentItemTypeEnum
	kContentMemberType            =57091      # from enum ContentItemTypeEnum
	kCustomContent                =2          # from enum ContentLibraryComponentTypeBits
	kStandardContent              =1          # from enum ContentLibraryComponentTypeBits
	kDoNotRefreshOutOfDateParts   =3          # from enum ContentMemberRefreshEnum
	kRefreshOutOfDateParts        =2          # from enum ContentMemberRefreshEnum
	kUseDefaultRefreshSetting     =1          # from enum ContentMemberRefreshEnum
	kContentConsumer              =0          # from enum ContentUserRoleEnum
	kContentEditor                =1          # from enum ContentUserRoleEnum
	kContentPublisher             =2          # from enum ContentUserRoleEnum
	kCurvatureContinuity          =61954      # from enum ContinuityTypeEnum
	kTangentContinuity            =61953      # from enum ContinuityTypeEnum
	kButtonDefinition             =42753      # from enum ControlDefinitionTypeEnum
	kComboBoxDefinition           =42754      # from enum ControlDefinitionTypeEnum
	kMacroControlDefinition       =42755      # from enum ControlDefinitionTypeEnum
	kButtonControl                =45061      # from enum ControlTypeEnum
	kButtonPopupControl           =45058      # from enum ControlTypeEnum
	kComboBoxControl              =45062      # from enum ControlTypeEnum
	kGalleryControl               =45066      # from enum ControlTypeEnum
	kMacroControl                 =45063      # from enum ControlTypeEnum
	kPopupControl                 =45057      # from enum ControlTypeEnum
	kSeparatorControl             =45065      # from enum ControlTypeEnum
	kSplitButtonControl           =45060      # from enum ControlTypeEnum
	kSplitButtonMRUControl        =45059      # from enum ControlTypeEnum
	kTogglePopupControl           =45067      # from enum ControlTypeEnum
	kUnknownControl               =45064      # from enum ControlTypeEnum
	kXYPlane                      =87297      # from enum CoordinateSystemPlaneEnum
	kXZPlane                      =87298      # from enum CoordinateSystemPlaneEnum
	kYZPlane                      =87299      # from enum CoordinateSystemPlaneEnum
	kCartesian                    =98561      # from enum CoordinateSystemTypeEnum
	kCylindrical                  =98563      # from enum CoordinateSystemTypeEnum
	kPolar                        =98562      # from enum CoordinateSystemTypeEnum
	kSpherical                    =98564      # from enum CoordinateSystemTypeEnum
	kCornerFaceEdgeDistance       =79106      # from enum CornerDefinitionTypeEnum
	kCornerMaxDistance            =79105      # from enum CornerDefinitionTypeEnum
	kRoundCornerReliefAtIntersection=110593     # from enum CornerReliefPlacementEnum
	kRoundCornerReliefAtVertex    =110595     # from enum CornerReliefPlacementEnum
	kRoundCornerReliefTangent     =110594     # from enum CornerReliefPlacementEnum
	kSquareCornerReliefAtIntersection=110596     # from enum CornerReliefPlacementEnum
	kSquareCornerReliefAtVertex   =110597     # from enum CornerReliefPlacementEnum
	kArcWeldCornerReliefShape     =28425      # from enum CornerReliefShapeEnum
	kDefaultCornerReliefShape     =28422      # from enum CornerReliefShapeEnum
	kFullRoundCornerReliefShape   =28428      # from enum CornerReliefShapeEnum
	kIntersectionCornerReliefShape=28427      # from enum CornerReliefShapeEnum
	kLaserWeldReliefShape         =28430      # from enum CornerReliefShapeEnum
	kLinearWeldReliefShape        =28421      # from enum CornerReliefShapeEnum
	kNoReplacementCornerReliefShape=28426      # from enum CornerReliefShapeEnum
	kRoundCornerReliefShape       =28417      # from enum CornerReliefShapeEnum
	kRoundWithRadiusCornerReliefShape=28429      # from enum CornerReliefShapeEnum
	kSquareCornerReliefShape      =28418      # from enum CornerReliefShapeEnum
	kTearCornerReliefShape        =28419      # from enum CornerReliefShapeEnum
	kTrimToBendReliefShape        =28420      # from enum CornerReliefShapeEnum
	kCornerNoOverlap              =76034      # from enum CornerTypeEnum
	kCornerOverlap                =76033      # from enum CornerTypeEnum
	kCornerReverseOverlap         =76035      # from enum CornerTypeEnum
	kCursorHotSpotBottomCenter    =47880      # from enum CursorHotSpotEnum
	kCursorHotSpotBottomLeft      =47879      # from enum CursorHotSpotEnum
	kCursorHotSpotBottomRight     =47881      # from enum CursorHotSpotEnum
	kCursorHotSpotDefault         =47882      # from enum CursorHotSpotEnum
	kCursorHotSpotMiddleCenter    =47877      # from enum CursorHotSpotEnum
	kCursorHotSpotMiddleLeft      =47876      # from enum CursorHotSpotEnum
	kCursorHotSpotMiddleRight     =47878      # from enum CursorHotSpotEnum
	kCursorHotSpotTopCenter       =47874      # from enum CursorHotSpotEnum
	kCursorHotSpotTopLeft         =47873      # from enum CursorHotSpotEnum
	kCursorHotSpotTopRight        =47875      # from enum CursorHotSpotEnum
	kCursorBuiltInArrow           =47621      # from enum CursorTypeEnum
	kCursorBuiltInArrowCursor     =47622      # from enum CursorTypeEnum
	kCursorBuiltInCommonSketchDrag=47636      # from enum CursorTypeEnum
	kCursorBuiltInCrosshair       =47623      # from enum CursorTypeEnum
	kCursorBuiltInCursorSelComp   =47624      # from enum CursorTypeEnum
	kCursorBuiltInCursorSelTrail  =47625      # from enum CursorTypeEnum
	kCursorBuiltInDynpan          =47626      # from enum CursorTypeEnum
	kCursorBuiltInDynzoom         =47627      # from enum CursorTypeEnum
	kCursorBuiltInLineCursor      =47628      # from enum CursorTypeEnum
	kCursorBuiltInLookat          =47629      # from enum CursorTypeEnum
	kCursorBuiltInMeasureCmd      =47630      # from enum CursorTypeEnum
	kCursorBuiltInPushpinCursor   =47631      # from enum CursorTypeEnum
	kCursorBuiltInSelectArrow     =47633      # from enum CursorTypeEnum
	kCursorBuiltInSelectView      =47634      # from enum CursorTypeEnum
	kCursorBuiltInSketch          =47635      # from enum CursorTypeEnum
	kCursorBuiltInSketch3DEditCursor=47632      # from enum CursorTypeEnum
	kCursorBuiltInZoom            =47637      # from enum CursorTypeEnum
	kCursorBuiltInZoomSel         =47638      # from enum CursorTypeEnum
	kCursorTypeCustom             =47619      # from enum CursorTypeEnum
	kCursorTypeDefault            =47617      # from enum CursorTypeEnum
	kCursorTypeWindows            =47618      # from enum CursorTypeEnum
	kBSplineCurve2d               =5256       # from enum Curve2dTypeEnum
	kCircleCurve2d                =5252       # from enum Curve2dTypeEnum
	kCircularArcCurve2d           =5253       # from enum Curve2dTypeEnum
	kEllipseFullCurve2d           =5254       # from enum Curve2dTypeEnum
	kEllipticalArcCurve2d         =5255       # from enum Curve2dTypeEnum
	kLineCurve2d                  =5250       # from enum Curve2dTypeEnum
	kLineSegmentCurve2d           =5251       # from enum Curve2dTypeEnum
	kPolylineCurve2d              =5257       # from enum Curve2dTypeEnum
	kUnknownCurve2d               =5249       # from enum Curve2dTypeEnum
	kExplicit                     =98306      # from enum CurveEquationTypeEnum
	kParametric                   =98305      # from enum CurveEquationTypeEnum
	CurveGeometryForm_NURBS       =1          # from enum CurveGeometryFormEnum
	CurveGeometryForm_Not_NURBS   =2          # from enum CurveGeometryFormEnum
	kBSplineCurve                 =5128       # from enum CurveTypeEnum
	kCircleCurve                  =5124       # from enum CurveTypeEnum
	kCircularArcCurve             =5125       # from enum CurveTypeEnum
	kEllipseFullCurve             =5126       # from enum CurveTypeEnum
	kEllipticalArcCurve           =5127       # from enum CurveTypeEnum
	kLineCurve                    =5122       # from enum CurveTypeEnum
	kLineSegmentCurve             =5123       # from enum CurveTypeEnum
	kPolylineCurve                =5129       # from enum CurveTypeEnum
	kUnknownCurve                 =5121       # from enum CurveTypeEnum
	kDegreesAnglePrecision        =85522      # from enum CustomPropertyPrecisionEnum
	kEightDecimalPlacesPrecision  =85513      # from enum CustomPropertyPrecisionEnum
	kEighthsFractionalLengthPrecision=85517      # from enum CustomPropertyPrecisionEnum
	kFiveDecimalPlacesPrecision   =85510      # from enum CustomPropertyPrecisionEnum
	kFourDecimalPlacesPrecision   =85509      # from enum CustomPropertyPrecisionEnum
	kHalfFractionalLengthPrecision=85515      # from enum CustomPropertyPrecisionEnum
	kMinutesAnglePrecision        =85523      # from enum CustomPropertyPrecisionEnum
	kOneDecimalPlacePrecision     =85506      # from enum CustomPropertyPrecisionEnum
	kOneTwentyEighthsFractionalLengthPrecision=85521      # from enum CustomPropertyPrecisionEnum
	kQuarterFractionalLengthPrecision=85516      # from enum CustomPropertyPrecisionEnum
	kSecondsAnglePrecision        =85524      # from enum CustomPropertyPrecisionEnum
	kSecondsFourDecimalPlaceAnglePrecision=85528      # from enum CustomPropertyPrecisionEnum
	kSecondsOneDecimalPlaceAnglePrecision=85525      # from enum CustomPropertyPrecisionEnum
	kSecondsThreeDecimalPlaceAnglePrecision=85527      # from enum CustomPropertyPrecisionEnum
	kSecondsTwoDecimalPlaceAnglePrecision=85526      # from enum CustomPropertyPrecisionEnum
	kSevenDecimalPlacesPrecision  =85512      # from enum CustomPropertyPrecisionEnum
	kSixDecimalPlacesPrecision    =85511      # from enum CustomPropertyPrecisionEnum
	kSixteenthsFractionalLengthPrecision=85518      # from enum CustomPropertyPrecisionEnum
	kSixtyFourthsFractionalLengthPrecision=85520      # from enum CustomPropertyPrecisionEnum
	kThirtySecondsFractionalLengthPrecision=85519      # from enum CustomPropertyPrecisionEnum
	kThreeDecimalPlacesPrecision  =85508      # from enum CustomPropertyPrecisionEnum
	kTwoDecimalPlacesPrecision    =85507      # from enum CustomPropertyPrecisionEnum
	kZeroDecimalPlacePrecision    =85505      # from enum CustomPropertyPrecisionEnum
	kZeroFractionalLengthPrecision=85514      # from enum CustomPropertyPrecisionEnum
	kNumberPropertyType           =85250      # from enum CustomPropertyTypeEnum
	kTextPropertyType             =85249      # from enum CustomPropertyTypeEnum
	kApplicationOptions           =116225     # from enum CustomSettingsTypeEnum
	kCommandPresets               =116228     # from enum CustomSettingsTypeEnum
	kCommandSettings              =116229     # from enum CustomSettingsTypeEnum
	kUserCustomizationSettings    =116226     # from enum CustomSettingsTypeEnum
	kiLogicSettings               =116227     # from enum CustomSettingsTypeEnum
	kAccelerationImposeMotion     =96515      # from enum DSDOFImposedMotionTypeEnum
	kNoImposeMotion               =96516      # from enum DSDOFImposedMotionTypeEnum
	kPositionImposeMotion         =96513      # from enum DSDOFImposedMotionTypeEnum
	kVelocityImposeMotion         =96514      # from enum DSDOFImposedMotionTypeEnum
	kRotationDegreeOfFreedomType  =98049      # from enum DSDegreeOfFreedomTypeEnum
	kTranslationDegreeOfFreedomType=98050      # from enum DSDegreeOfFreedomTypeEnum
	kCubicRampInterpolationType   =96258      # from enum DSGraphInterpolationTypeEnum
	kCycloidInterpolationType     =96259      # from enum DSGraphInterpolationTypeEnum
	kFormulaInterpolationType     =96266      # from enum DSGraphInterpolationTypeEnum
	kHarmonicInterpolationType    =96262      # from enum DSGraphInterpolationTypeEnum
	kLinearRampInterpolationType  =96257      # from enum DSGraphInterpolationTypeEnum
	kModifiedSineInterpolationType=96263      # from enum DSGraphInterpolationTypeEnum
	kModifiedTrapezoidInterpolationType=96264      # from enum DSGraphInterpolationTypeEnum
	kPolynomialInterpolationType  =96261      # from enum DSGraphInterpolationTypeEnum
	kSineInterpolationType        =96260      # from enum DSGraphInterpolationTypeEnum
	kSplineInterpolationType      =96265      # from enum DSGraphInterpolationTypeEnum
	kDSJointType3DPointInCyl      =92981      # from enum DSJointTypeEnum
	kDSJointType3DPointInSphere   =92979      # from enum DSJointTypeEnum
	kDSJointType3DPointOnCyl      =92980      # from enum DSJointTypeEnum
	kDSJointType3DPointOnSphere   =92978      # from enum DSJointTypeEnum
	kDSJointType3DPointPlane      =92977      # from enum DSJointTypeEnum
	kDSJointType3DSphereInCyl     =92976      # from enum DSJointTypeEnum
	kDSJointType3DSphereInSphere  =92974      # from enum DSJointTypeEnum
	kDSJointType3DSphereOnCyl     =92975      # from enum DSJointTypeEnum
	kDSJointType3DSphereOnSphere  =92973      # from enum DSJointTypeEnum
	kDSJointType3DSpherePlane     =92972      # from enum DSJointTypeEnum
	kDSJointTypeAcuator           =92983      # from enum DSJointTypeEnum
	kDSJointTypeBelt1C            =92947      # from enum DSJointTypeEnum
	kDSJointTypeCurveCurveJct     =92971      # from enum DSJointTypeEnum
	kDSJointTypeCylindrical       =92939      # from enum DSJointTypeEnum
	kDSJointTypeDiscInDiscJct     =92967      # from enum DSJointTypeEnum
	kDSJointTypeDiscLineJct       =92964      # from enum DSJointTypeEnum
	kDSJointTypeDiscOnDiscJct     =92965      # from enum DSJointTypeEnum
	kDSJointTypeDiscSegmentJct    =92970      # from enum DSJointTypeEnum
	kDSJointTypeHeliCouple        =92958      # from enum DSJointTypeEnum
	kDSJointTypeHeliScrew1C       =92946      # from enum DSJointTypeEnum
	kDSJointTypeImpact3D          =92982      # from enum DSJointTypeEnum
	kDSJointTypeLinePlane         =92932      # from enum DSJointTypeEnum
	kDSJointTypeLinePlaneInv      =92938      # from enum DSJointTypeEnum
	kDSJointTypePivot             =92940      # from enum DSJointTypeEnum
	kDSJointTypePlanar3D          =92934      # from enum DSJointTypeEnum
	kDSJointTypePointInDiscJct    =92968      # from enum DSJointTypeEnum
	kDSJointTypePointLine         =92933      # from enum DSJointTypeEnum
	kDSJointTypePointLineInv      =92937      # from enum DSJointTypeEnum
	kDSJointTypePointLineJct      =92963      # from enum DSJointTypeEnum
	kDSJointTypePointOnDiscJct    =92966      # from enum DSJointTypeEnum
	kDSJointTypePointPlane        =92931      # from enum DSJointTypeEnum
	kDSJointTypePointPlaneInv     =92936      # from enum DSJointTypeEnum
	kDSJointTypePointSegmentJct   =92969      # from enum DSJointTypeEnum
	kDSJointTypePrismatic         =92941      # from enum DSJointTypeEnum
	kDSJointTypeRigidity          =92929      # from enum DSJointTypeEnum
	kDSJointTypeRollConeInCone1C  =92952      # from enum DSJointTypeEnum
	kDSJointTypeRollConeOnCone1C  =92951      # from enum DSJointTypeEnum
	kDSJointTypeRollConeOnPlane1C =92950      # from enum DSJointTypeEnum
	kDSJointTypeRollDiscInDisc1C  =92949      # from enum DSJointTypeEnum
	kDSJointTypeRollDiscInDisc2C  =92945      # from enum DSJointTypeEnum
	kDSJointTypeRollDiscLine1C    =92953      # from enum DSJointTypeEnum
	kDSJointTypeRollDiscLine2C    =92943      # from enum DSJointTypeEnum
	kDSJointTypeRollDiscOnDisc1C  =92948      # from enum DSJointTypeEnum
	kDSJointTypeRollDiscOnDisc2C  =92944      # from enum DSJointTypeEnum
	kDSJointTypeRollDiskCurve2C   =92961      # from enum DSJointTypeEnum
	kDSJointTypeSlidDiscCurve1C   =92962      # from enum DSJointTypeEnum
	kDSJointTypeSlidDiscInDisc1C  =92954      # from enum DSJointTypeEnum
	kDSJointTypeSlidDiscLine1C    =92956      # from enum DSJointTypeEnum
	kDSJointTypeSlidDiscOnDisc1C  =92955      # from enum DSJointTypeEnum
	kDSJointTypeSlidPointCurve1C  =92960      # from enum DSJointTypeEnum
	kDSJointTypeSlidPointDisk1C   =92957      # from enum DSJointTypeEnum
	kDSJointTypeSpatial           =92930      # from enum DSJointTypeEnum
	kDSJointTypeSpherical         =92935      # from enum DSJointTypeEnum
	kDSJointTypeUndefined         =92942      # from enum DSJointTypeEnum
	kDSJointTypeWormGearCouple    =92959      # from enum DSJointTypeEnum
	kForceLoadType                =96002      # from enum DSLoadTypeEnum
	kTorqueLoadType               =96001      # from enum DSLoadTypeEnum
	kAcceleration1ResultType      =96771      # from enum DSResultTypeEnum
	kDrivingForceUImposed1ResultType=96772      # from enum DSResultTypeEnum
	kExtentLengthResultType       =96773      # from enum DSResultTypeEnum
	kExtentVelocityResultType     =96774      # from enum DSResultTypeEnum
	kForceResultType              =96775      # from enum DSResultTypeEnum
	kForceXResultType             =96776      # from enum DSResultTypeEnum
	kForceYResultType             =96777      # from enum DSResultTypeEnum
	kForceZResultType             =96778      # from enum DSResultTypeEnum
	kMomentResultType             =96779      # from enum DSResultTypeEnum
	kMomentXResultType            =96780      # from enum DSResultTypeEnum
	kMomentYResultType            =96781      # from enum DSResultTypeEnum
	kMomentZResultType            =96782      # from enum DSResultTypeEnum
	kPosition1ResultType          =96769      # from enum DSResultTypeEnum
	kTraceAccelerationResultType  =96783      # from enum DSResultTypeEnum
	kTraceAccelerationXResultType =96784      # from enum DSResultTypeEnum
	kTraceAccelerationYResultType =96785      # from enum DSResultTypeEnum
	kTraceAccelerationZResultType =96786      # from enum DSResultTypeEnum
	kTracePositionResultType      =96787      # from enum DSResultTypeEnum
	kTracePositionXResultType     =96788      # from enum DSResultTypeEnum
	kTracePositionYResultType     =96789      # from enum DSResultTypeEnum
	kTracePositionZResultType     =96790      # from enum DSResultTypeEnum
	kTraceVelocityResultType      =96791      # from enum DSResultTypeEnum
	kTraceVelocityXResultType     =96792      # from enum DSResultTypeEnum
	kTraceVelocityYResultType     =96793      # from enum DSResultTypeEnum
	kTraceVelocityZResultType     =96794      # from enum DSResultTypeEnum
	kVelocity1ResultType          =96770      # from enum DSResultTypeEnum
	kBasicDWFPublish              =62721      # from enum DWFPublishModeEnum
	kCompleteDWFPublish           =62722      # from enum DWFPublishModeEnum
	kCustomDWFPublish             =62723      # from enum DWFPublishModeEnum
	kAutoCAD2000                  =86529      # from enum DWGFileVersionEnum
	kAutoCAD2004                  =86530      # from enum DWGFileVersionEnum
	kAutoCAD2007                  =86531      # from enum DWGFileVersionEnum
	kAutoCAD2010                  =86532      # from enum DWGFileVersionEnum
	kAutoCAD2013                  =86533      # from enum DWGFileVersionEnum
	kAutoCAD2018                  =86534      # from enum DWGFileVersionEnum
	kAddRefWatchType              =1          # from enum DebugWatchType
	kNoneWatchType                =0          # from enum DebugWatchType
	kQueryInterfaceWatchType      =4          # from enum DebugWatchType
	kReleaseWatchType             =2          # from enum DebugWatchType
	kCommaDecimalMarker           =41474      # from enum DecimalMarkerTypeEnum
	kPeriodDecimalMarker          =41473      # from enum DecimalMarkerTypeEnum
	kDWGDefaultDrawingFileType    =69633      # from enum DefaultDrawingFileTypeEnum
	kIDWDefaultDrawingFileType    =69634      # from enum DefaultDrawingFileTypeEnum
	kLastUsedDefaultLayerStyle    =69890      # from enum DefaultLayerStyleEnum
	kStandardDefaultLayerStyle    =69889      # from enum DefaultLayerStyleEnum
	kImportNonInventorDWGFile     =70146      # from enum DefaultNonInventorDWGFileOpenBehaviorEnum
	kRegularOpenNonInventorDWGFile=70145      # from enum DefaultNonInventorDWGFileOpenBehaviorEnum
	kLastUsedDefaultObjectStyle   =70402      # from enum DefaultObjectStyleEnum
	kStandardDefaultObjectStyle   =70401      # from enum DefaultObjectStyleEnum
	kDerivedBoundingBox           =27141      # from enum DerivedComponentOptionEnum
	kDerivedExcludeAll            =27138      # from enum DerivedComponentOptionEnum
	kDerivedIncludeAll            =27137      # from enum DerivedComponentOptionEnum
	kDerivedIndividualDefined     =27140      # from enum DerivedComponentOptionEnum
	kDerivedIntersect             =27142      # from enum DerivedComponentOptionEnum
	kDerivedSubtractAll           =27139      # from enum DerivedComponentOptionEnum
	kDeriveAsMultipleBodies       =80643      # from enum DerivedComponentStyleEnum
	kDeriveAsSingleBodyNoSeams    =80642      # from enum DerivedComponentStyleEnum
	kDeriveAsSingleBodyWithSeams  =80641      # from enum DerivedComponentStyleEnum
	kDeriveAsWorkSurface          =80644      # from enum DerivedComponentStyleEnum
	kDerivedRemoveNone            =88577      # from enum DerivedGeometryRemovalEnum
	kDerivedRemovePartsAndFaces   =88579      # from enum DerivedGeometryRemovalEnum
	kDerivedRemovePartsOnly       =88578      # from enum DerivedGeometryRemovalEnum
	kDerivedPatchAll              =88322      # from enum DerivedHolePatchEnum
	kDerivedPatchNone             =88321      # from enum DerivedHolePatchEnum
	kDerivedPatchRange            =88323      # from enum DerivedHolePatchEnum
	kDerivedPartMirrorPlaneXY     =27393      # from enum DerivedPartMirrorPlaneEnum
	kDerivedPartMirrorPlaneXZ     =27395      # from enum DerivedPartMirrorPlaneEnum
	kDerivedPartMirrorPlaneYZ     =27394      # from enum DerivedPartMirrorPlaneEnum
	kDerivedPartNoMirrorPlane     =27396      # from enum DerivedPartMirrorPlaneEnum
	kDerivedDrawingFilename       =29700      # from enum DerivedPropertyTypeEnum
	kDerivedDrawingFilenameAndPath=29701      # from enum DerivedPropertyTypeEnum
	kDerivedDrawingVersion        =29702      # from enum DerivedPropertyTypeEnum
	kDerivedInitialViewScale      =29707      # from enum DerivedPropertyTypeEnum
	kDerivedModelFilename         =29697      # from enum DerivedPropertyTypeEnum
	kDerivedModelFilenameAndPath  =29698      # from enum DerivedPropertyTypeEnum
	kDerivedModelVersion          =29699      # from enum DerivedPropertyTypeEnum
	kDerivedNumberOfSheets        =29703      # from enum DerivedPropertyTypeEnum
	kDerivedSheetNumber           =29704      # from enum DerivedPropertyTypeEnum
	kDerivedSheetRevision         =29706      # from enum DerivedPropertyTypeEnum
	kDerivedSheetSize             =29705      # from enum DerivedPropertyTypeEnum
	kAllVisibleDesignViewType     =57349      # from enum DesignViewTypeEnum
	kLastActiveDesignViewType     =57351      # from enum DesignViewTypeEnum
	kMasterDesignViewType         =57345      # from enum DesignViewTypeEnum
	kNothingVisibleDesignViewType =57350      # from enum DesignViewTypeEnum
	kPrivateDesignViewType        =57346      # from enum DesignViewTypeEnum
	kPublicDesignViewType         =57347      # from enum DesignViewTypeEnum
	kTransientDesignViewType      =57348      # from enum DesignViewTypeEnum
	_kEditDialogStyle             =56836      # from enum DialogStyleEnum
	kFullyDockedDialogStyle       =56833      # from enum DialogStyleEnum
	kNoButtonsDialogStyle         =56835      # from enum DialogStyleEnum
	kNoTitleBarDialogStyle        =56834      # from enum DialogStyleEnum
	kAmericanEnglish              =117249     # from enum DictionaryLanguageTypeEnum
	kBritishEnglish               =117250     # from enum DictionaryLanguageTypeEnum
	kCanadianEnglish              =117251     # from enum DictionaryLanguageTypeEnum
	kCatalan                      =117252     # from enum DictionaryLanguageTypeEnum
	kCzech                        =117253     # from enum DictionaryLanguageTypeEnum
	kDanish                       =117254     # from enum DictionaryLanguageTypeEnum
	kDutch                        =117255     # from enum DictionaryLanguageTypeEnum
	kFinnish                      =117256     # from enum DictionaryLanguageTypeEnum
	kFrench                       =117257     # from enum DictionaryLanguageTypeEnum
	kGermanPostReform             =117258     # from enum DictionaryLanguageTypeEnum
	kGermanPreReform              =117259     # from enum DictionaryLanguageTypeEnum
	kItalian                      =117260     # from enum DictionaryLanguageTypeEnum
	kNorwegian                    =117261     # from enum DictionaryLanguageTypeEnum
	kPortugueseBrazil             =117262     # from enum DictionaryLanguageTypeEnum
	kPortuguesePortugal           =117263     # from enum DictionaryLanguageTypeEnum
	kRussian                      =117264     # from enum DictionaryLanguageTypeEnum
	kSpanish                      =117265     # from enum DictionaryLanguageTypeEnum
	kSwedish                      =117266     # from enum DictionaryLanguageTypeEnum
	kUnknownLanguage              =117267     # from enum DictionaryLanguageTypeEnum
	kAlignedAlignmentType         =50178      # from enum DimensionAlignmentTypeEnum
	kDefaultAlignmentType         =50177      # from enum DimensionAlignmentTypeEnum
	kHorizontalAlignmentType      =50179      # from enum DimensionAlignmentTypeEnum
	kVerticalAlignmentType        =50180      # from enum DimensionAlignmentTypeEnum
	kAlwaysRelaxDimensionConstraints=58115      # from enum DimensionConstraintsRelaxationEnum
	kNeverRelaxDimensionConstraints=58113      # from enum DimensionConstraintsRelaxationEnum
	kNoEquationRelaxDimensionConstraints=58114      # from enum DimensionConstraintsRelaxationEnum
	kPromptRelaxDimensionConstraints=58116      # from enum DimensionConstraintsRelaxationEnum
	kDimensionDisplayAsExpession  =34819      # from enum DimensionDisplayTypeEnum
	kDimensionDisplayAsExpression =34819      # from enum DimensionDisplayTypeEnum
	kDimensionDisplayAsName       =34818      # from enum DimensionDisplayTypeEnum
	kDimensionDisplayAsPreciseValue=34821      # from enum DimensionDisplayTypeEnum
	kDimensionDisplayAsToerance   =34820      # from enum DimensionDisplayTypeEnum
	kDimensionDisplayAsTolerance  =34820      # from enum DimensionDisplayTypeEnum
	kDimensionDisplayAsValue      =34817      # from enum DimensionDisplayTypeEnum
	kAlignedDim                   =19203      # from enum DimensionOrientationEnum
	kHorizontalDim                =19201      # from enum DimensionOrientationEnum
	kVerticalDim                  =19202      # from enum DimensionOrientationEnum
	kAdjacentFormat               =41985      # from enum DimensionStyleFormatEnum
	kAdjacentWithBracketsForAlternateFormat=41987      # from enum DimensionStyleFormatEnum
	kAdjacentWithBracketsForPrimaryFormat=41986      # from enum DimensionStyleFormatEnum
	kBelowFormat                  =41988      # from enum DimensionStyleFormatEnum
	kBelowWithBracketsForAlternateFormat=41990      # from enum DimensionStyleFormatEnum
	kBelowWithBracketsForPrimaryFormat=41989      # from enum DimensionStyleFormatEnum
	kNoAlternateUnits             =41991      # from enum DimensionStyleFormatEnum
	kMaintainAllTextAlignment     =55555      # from enum DimensionTextAlignmentEnum
	kMaintainCenteredTextAlignment=55554      # from enum DimensionTextAlignmentEnum
	kMaintainViewPositionAlignment=55553      # from enum DimensionTextAlignmentEnum
	kAboveForHorizontal           =101377     # from enum DimensionTextModifierEnum
	kNoModifier                   =101379     # from enum DimensionTextModifierEnum
	kOutsideDimensionLine         =101378     # from enum DimensionTextModifierEnum
	kOutsideForAngles30to210      =101380     # from enum DimensionTextModifierEnum
	kInlineAlignedDimensionText   =101123     # from enum DimensionTextOrientationEnum
	kInlineHorizontalDimensionText=101122     # from enum DimensionTextOrientationEnum
	kParallelAllAboveDimensionText=101124     # from enum DimensionTextOrientationEnum
	kParallelDimensionText        =101121     # from enum DimensionTextOrientationEnum
	kParallelFirstAboveDimensionText=101125     # from enum DimensionTextOrientationEnum
	kParallelHorizontalDimensionText=101126     # from enum DimensionTextOrientationEnum
	kAlignedDimensionType         =60161      # from enum DimensionTypeEnum
	kAngularDimensionType         =60169      # from enum DimensionTypeEnum
	kAngularForeshortenedDimensionType=60170      # from enum DimensionTypeEnum
	kArcLengthDimensionType       =60164      # from enum DimensionTypeEnum
	kArcLengthForeshortenedDimensionType=60168      # from enum DimensionTypeEnum
	kDiametricDimensionType       =60166      # from enum DimensionTypeEnum
	kHorizontalDimensionType      =60162      # from enum DimensionTypeEnum
	kLinearForeshortenedDimensionType=60167      # from enum DimensionTypeEnum
	kSymmetricDimensionType       =60165      # from enum DimensionTypeEnum
	kVerticalDimensionType        =60163      # from enum DimensionTypeEnum
	kZeroToleranceDisplayFull     =101889     # from enum DimensionZeroToleranceDisplayEnum
	kZeroToleranceDisplayNoTrailingZeros=101890     # from enum DimensionZeroToleranceDisplayEnum
	kZeroToleranceDisplayNoTrailingZerosNoSign=101891     # from enum DimensionZeroToleranceDisplayEnum
	kZeroToleranceDisplaySuppressDisplay=101892     # from enum DimensionZeroToleranceDisplayEnum
	kDirectEditDeleteOperationType=105732     # from enum DirectEditOperationTypeEnum
	kDirectEditMoveOperationType  =105729     # from enum DirectEditOperationTypeEnum
	kDirectEditRotateOperationType=105731     # from enum DirectEditOperationTypeEnum
	kDirectEditScaleOperationType =105734     # from enum DirectEditOperationTypeEnum
	kDirectEditSizeOperationType  =105730     # from enum DirectEditOperationTypeEnum
	kDirectEditUnknownOperationType=105733     # from enum DirectEditOperationTypeEnum
	kBothDirections               =771        # from enum DirectionEnum
	kInwardDirection              =770        # from enum DirectionEnum
	kOutwardDirection             =769        # from enum DirectionEnum
	kDecimalFormat                =78340      # from enum DisplayFormatEnum
	kFractionalDiagonalStackedFormat=78339      # from enum DisplayFormatEnum
	kFractionalHorizontalStackedFormat=78338      # from enum DisplayFormatEnum
	kFractionalNotStackedFormat   =78337      # from enum DisplayFormatEnum
	kHiddenEdgeRendering          =8707       # from enum DisplayModeEnum
	kIllustrationRendering        =8715       # from enum DisplayModeEnum
	kMonochromeRendering          =8713       # from enum DisplayModeEnum
	kRealisticRendering           =8709       # from enum DisplayModeEnum
	kShadedRendering              =8708       # from enum DisplayModeEnum
	kShadedWithEdgesRendering     =8710       # from enum DisplayModeEnum
	kShadedWithHiddenEdgesRendering=8707       # from enum DisplayModeEnum
	kTechnicalIllustrationRendering=8716       # from enum DisplayModeEnum
	kWatercolorRendering          =8714       # from enum DisplayModeEnum
	kWireframeNoHiddenEdges       =8711       # from enum DisplayModeEnum
	kWireframeRendering           =8706       # from enum DisplayModeEnum
	kWireframeWithHiddenEdgesRendering=8712       # from enum DisplayModeEnum
	kDefaultDisplayMode           =54273      # from enum DisplayModeSourceTypeEnum
	kOverrideDisplayMode          =54274      # from enum DisplayModeSourceTypeEnum
	kMediumDisplayQuality         =58882      # from enum DisplayQualityEnum
	kRoughDisplayQuality          =58883      # from enum DisplayQualityEnum
	kSmoothDisplayQuality         =58881      # from enum DisplayQualityEnum
	kSmootherDisplayQuality       =58884      # from enum DisplayQualityEnum
	kFrontFacing                  =26113      # from enum DisplayTransformBehaviorEnum
	kFrontFacingAndPixelScaling   =26115      # from enum DisplayTransformBehaviorEnum
	kNoTransformBehaviors         =26116      # from enum DisplayTransformBehaviorEnum
	kPixelScaling                 =26114      # from enum DisplayTransformBehaviorEnum
	kDockBottom                   =1          # from enum DockingStateEnum
	kDockLastKnown                =32         # from enum DockingStateEnum
	kDockLeft                     =2          # from enum DockingStateEnum
	kDockRight                    =4          # from enum DockingStateEnum
	kDockTop                      =8          # from enum DockingStateEnum
	kFloat                        =16         # from enum DockingStateEnum
	kInterested                   =68866      # from enum DocumentInterestTypeEnum
	kNotInterested                =68865      # from enum DocumentInterestTypeEnum
	kDocumentExpressLoadState     =103938     # from enum DocumentLoadStateEnum
	kDocumentFullLoadState        =103939     # from enum DocumentLoadStateEnum
	kDocumentLiteLoadState        =103938     # from enum DocumentLoadStateEnum
	kDocumentPartialLoadState     =103940     # from enum DocumentLoadStateEnum
	kDocumentUnknownLoadState     =103937     # from enum DocumentLoadStateEnum
	kAssemblyDocumentObject       =12291      # from enum DocumentTypeEnum
	kDesignElementDocumentObject  =12294      # from enum DocumentTypeEnum
	kDrawingDocumentObject        =12292      # from enum DocumentTypeEnum
	kForeignModelDocumentObject   =12295      # from enum DocumentTypeEnum
	kNoDocument                   =12297      # from enum DocumentTypeEnum
	kPartDocumentObject           =12290      # from enum DocumentTypeEnum
	kPresentationDocumentObject   =12293      # from enum DocumentTypeEnum
	kSATFileDocumentObject        =12296      # from enum DocumentTypeEnum
	kUnknownDocumentObject        =12289      # from enum DocumentTypeEnum
	kDoubleBend45Degree           =74754      # from enum DoubleBendTypeEnum
	kDoubleBend90Degree           =74755      # from enum DoubleBendTypeEnum
	kDoubleBendFixedEdges         =74753      # from enum DoubleBendTypeEnum
	kDoubleBendFullRadius         =74756      # from enum DoubleBendTypeEnum
	kDoubleBendNoBend             =74758      # from enum DoubleBendTypeEnum
	kDoubleBendSingle             =74757      # from enum DoubleBendTypeEnum
	kAsymmetricDraftAngles        =108291     # from enum DraftAngleConstraintTypeEnum
	kBothSidesMinDraftAngle       =108294     # from enum DraftAngleConstraintTypeEnum
	kOneWayDraftAngle             =108289     # from enum DraftAngleConstraintTypeEnum
	kSideOneMinDraftAngle         =108292     # from enum DraftAngleConstraintTypeEnum
	kSideTwoMinDraftAngle         =108293     # from enum DraftAngleConstraintTypeEnum
	kSymmetricDraftAngles         =108290     # from enum DraftAngleConstraintTypeEnum
	kANSI_DraftingStandard        =9731       # from enum DraftingStandardEnum
	kBSI_DraftingStandard         =9732       # from enum DraftingStandardEnum
	kDIN_DraftingStandard         =9733       # from enum DraftingStandardEnum
	kDefault_DraftingStandard     =9729       # from enum DraftingStandardEnum
	kGB_DraftingStandard          =9734       # from enum DraftingStandardEnum
	kGOST_DraftingStandard        =9737       # from enum DraftingStandardEnum
	kISO_DraftingStandard         =9735       # from enum DraftingStandardEnum
	kJIS_DraftingStandard         =9736       # from enum DraftingStandardEnum
	kLegacyBSI_DraftingStandard   =9738       # from enum DraftingStandardEnum
	kLegacyDIN_DraftingStandard   =9739       # from enum DraftingStandardEnum
	kLegacyGB_DraftingStandard    =9740       # from enum DraftingStandardEnum
	kLegacyISO_DraftingStandard   =9741       # from enum DraftingStandardEnum
	kLegacyJIS_DraftingStandard   =9742       # from enum DraftingStandardEnum
	kOther_DraftingStandard       =9730       # from enum DraftingStandardEnum
	kDragStateCancelDrag          =37895      # from enum DragStateEnum
	kDragStateDragHandlerSelection=37889      # from enum DragStateEnum
	kDragStateEndDrag             =37892      # from enum DragStateEnum
	kDragStateOnDrag              =37891      # from enum DragStateEnum
	kDragStateResumeDrag          =37894      # from enum DragStateEnum
	kDragStateStartDrag           =37890      # from enum DragStateEnum
	kDragStateSuspendDrag         =37893      # from enum DragStateEnum
	kBendDownEdge                 =82691      # from enum DrawingEdgeTypeEnum
	kBendExtentEdge               =82692      # from enum DrawingEdgeTypeEnum
	kBendUpEdge                   =82690      # from enum DrawingEdgeTypeEnum
	kContourRollEdge              =82697      # from enum DrawingEdgeTypeEnum
	kPunchDownEdge                =82693      # from enum DrawingEdgeTypeEnum
	kPunchUpEdge                  =82696      # from enum DrawingEdgeTypeEnum
	kTangentEdge                  =82694      # from enum DrawingEdgeTypeEnum
	kThreadEdge                   =82689      # from enum DrawingEdgeTypeEnum
	kUnknownEdge                  =82695      # from enum DrawingEdgeTypeEnum
	k12x18InDrawingSheetSize      =9999       # from enum DrawingSheetSizeEnum
	k18x24InDrawingSheetSize      =10000      # from enum DrawingSheetSizeEnum
	k24x36InDrawingSheetSize      =10001      # from enum DrawingSheetSizeEnum
	k30x42InDrawingSheetSize      =10003      # from enum DrawingSheetSizeEnum
	k36x48InDrawingSheetSize      =10002      # from enum DrawingSheetSizeEnum
	k9x12InDrawingSheetSize       =9998       # from enum DrawingSheetSizeEnum
	kA0DrawingSheetSize           =9993       # from enum DrawingSheetSizeEnum
	kA1DrawingSheetSize           =9994       # from enum DrawingSheetSizeEnum
	kA2DrawingSheetSize           =9995       # from enum DrawingSheetSizeEnum
	kA3DrawingSheetSize           =9996       # from enum DrawingSheetSizeEnum
	kA4DrawingSheetSize           =9997       # from enum DrawingSheetSizeEnum
	kADrawingSheetSize            =9987       # from enum DrawingSheetSizeEnum
	kBDrawingSheetSize            =9988       # from enum DrawingSheetSizeEnum
	kCDrawingSheetSize            =9989       # from enum DrawingSheetSizeEnum
	kCustomDrawingSheetSize       =9986       # from enum DrawingSheetSizeEnum
	kDDrawingSheetSize            =9990       # from enum DrawingSheetSizeEnum
	kDefaultDrawingSheetSize      =9985       # from enum DrawingSheetSizeEnum
	kEDrawingSheetSize            =9991       # from enum DrawingSheetSizeEnum
	kFDrawingSheetSize            =9992       # from enum DrawingSheetSizeEnum
	kAssyCompositionOutOfDateDrawingSheet=4          # from enum DrawingSheetStatusBits
	kAssyPositionOutOfDateDrawingSheet=2          # from enum DrawingSheetStatusBits
	kGeomOutOfDateDrawingSheet    =1          # from enum DrawingSheetStatusBits
	kNoDataDrawingSheet           =128        # from enum DrawingSheetStatusBits
	kParameterizedTextOutOfDateDrawingSheet=32         # from enum DrawingSheetStatusBits
	kProcessingPreciseDisplayDrawingSheet=256        # from enum DrawingSheetStatusBits
	kResourceTemplateOutOfDateDrawingSheet=16         # from enum DrawingSheetStatusBits
	kStandardOutOfDateDrawingSheet=8          # from enum DrawingSheetStatusBits
	kUnknownOutOfDateDrawingSheet =64         # from enum DrawingSheetStatusBits
	kUpToDateDrawingSheet         =0          # from enum DrawingSheetStatusBits
	kHorizontalViewAlignment      =80641      # from enum DrawingViewAlignmentEnum
	kInPositionViewAlignment      =80643      # from enum DrawingViewAlignmentEnum
	kVerticalViewAlignment        =80642      # from enum DrawingViewAlignmentEnum
	kFromBaseDrawingViewStyle     =32260      # from enum DrawingViewStyleEnum
	kHiddenLineDrawingViewStyle   =32257      # from enum DrawingViewStyleEnum
	kHiddenLineRemovedDrawingViewStyle=32258      # from enum DrawingViewStyleEnum
	kShadedDrawingViewStyle       =32259      # from enum DrawingViewStyleEnum
	kShadedHiddenLineDrawingViewStyle=32261      # from enum DrawingViewStyleEnum
	kAssociativeDraftDrawingViewType=10506      # from enum DrawingViewTypeEnum
	kAuxiliaryDrawingViewType     =10499      # from enum DrawingViewTypeEnum
	kCustomDrawingViewType        =10498      # from enum DrawingViewTypeEnum
	kDefaultDrawingViewType       =10497      # from enum DrawingViewTypeEnum
	kDetailDrawingViewType        =10502      # from enum DrawingViewTypeEnum
	kDraftDrawingViewType         =10505      # from enum DrawingViewTypeEnum
	kOLEAttachmentDrawingViewType =10500      # from enum DrawingViewTypeEnum
	kOverlayDrawingViewType       =10507      # from enum DrawingViewTypeEnum
	kProjectedDrawingViewType     =10504      # from enum DrawingViewTypeEnum
	kSectionDrawingViewType       =10503      # from enum DrawingViewTypeEnum
	kStandardDrawingViewType      =10501      # from enum DrawingViewTypeEnum
	kDriveAngleType               =100865     # from enum DriveTypeEnum
	kDriveAngularPositionType     =100868     # from enum DriveTypeEnum
	kDriveLinearPositionType      =100866     # from enum DriveTypeEnum
	kDriveOffsetType              =100867     # from enum DriveTypeEnum
	kAllConcave                   =27650      # from enum EdgeCollectionEnum
	kAllConvex                    =27651      # from enum EdgeCollectionEnum
	kTangentiallyConnected        =27649      # from enum EdgeCollectionEnum
	kUndefined                    =27652      # from enum EdgeCollectionEnum
	kEmbossEngraveFromPlane       =67331      # from enum EmbossTypeEnum
	kEmbossFromFace               =67329      # from enum EmbossTypeEnum
	kEngraveFromFace              =67330      # from enum EmbossTypeEnum
	kActivateEnvironmentState     =50945      # from enum EnvironmentStateEnum
	kRequestActivateEnvironmentState=50949      # from enum EnvironmentStateEnum
	kResumeEnvironmentState       =50947      # from enum EnvironmentStateEnum
	kSuspendEnvironmentState      =50946      # from enum EnvironmentStateEnum
	kTerminateEnvironmentState    =50948      # from enum EnvironmentStateEnum
	kAbort                        =4099       # from enum EventTimingEnum
	kAfter                        =4098       # from enum EventTimingEnum
	kBefore                       =4097       # from enum EventTimingEnum
	kExitToParent                 =63746      # from enum ExitTypeEnum
	kExitToPrevious               =63745      # from enum ExitTypeEnum
	kExitToTop                    =63747      # from enum ExitTypeEnum
	kFaceTangentiallyConnected    =40961      # from enum FaceCollectionEnum
	kFaceUndefined                =40962      # from enum FaceCollectionEnum
	kFixedEdgeFaceDraftDefinitionType=108033     # from enum FaceDraftDefinitionTypeEnum
	kFixedPlaneFaceDraftDefinitionType=108034     # from enum FaceDraftDefinitionTypeEnum
	kPartingToolFaceDraftDefinitionType=108035     # from enum FaceDraftDefinitionTypeEnum
	kFileNameMemberNameType       =81922      # from enum FactoryOptionsMemberNameTypeEnum
	kPartNumberMemberNameType     =81921      # from enum FactoryOptionsMemberNameTypeEnum
	kValueMemberNameType          =81923      # from enum FactoryOptionsMemberNameTypeEnum
	kNonePartNumberType           =82177      # from enum FactoryOptionsPartNumberTypeEnum
	kValuePartNumberType          =82178      # from enum FactoryOptionsPartNumberTypeEnum
	kConstantFamilyParameterValue =51457      # from enum FamilyParameterValueTypeEnum
	kCustomFamilyParameterValue   =51458      # from enum FamilyParameterValueTypeEnum
	kExpressionFamilyParameterValue=51459      # from enum FamilyParameterValueTypeEnum
	kCloseFitType                 =84072097   # from enum FastenerFitType
	kLooseFitType                 =84072098   # from enum FastenerFitType
	kNormalFitType                =84072099   # from enum FastenerFitType
	kMeanApproximation            =60674      # from enum FeatureApproximationTypeEnum
	kNeverTooThickApproximation   =60675      # from enum FeatureApproximationTypeEnum
	kNeverTooThinApproximation    =60676      # from enum FeatureApproximationTypeEnum
	kNoApproximation              =60673      # from enum FeatureApproximationTypeEnum
	kAnyCrossSection              =107027     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kAnyLongitudinalSection       =107028     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kAreaDiameter                 =107041     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kAverageSize                  =107045     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kCircumferenceDiameter        =107040     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kClosingQuote                 =107014     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kCommonZone                   =107020     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kContactingFeature            =107029     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kDegree                       =107010     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kLeastSquaresAssociationCriterion=107037     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kLineElement                  =107024     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kLocalSizeDefinedByASphere    =107036     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kMajorDiameter                =107022     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kMaximumInscribedAssociationCriterion=107038     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kMaximumSize                  =107043     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kMedianSize                   =107046     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kMidRangeSize                 =107047     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kMinimumCircumscribedAssociationCriterion=107039     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kMinimumSize                  =107044     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kMinorDiameter                =107021     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kNotConvex                    =107025     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kNumero                       =107015     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kOpeningQuote                 =107013     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kOrientationConstraintOnly    =107034     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kPitchDiameter                =107023     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kPlaneSymbol                  =107033     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kPlusMinus                    =107011     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kPointSymbol                  =107031     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kRangeOfSizes                 =107048     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kSection                      =107012     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kSlopeLeft                    =107016     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kSlopeRight                   =107017     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kStraightLine                 =107032     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kTOver2                       =107009     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kTaperLeft                    =107018     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kTaperRight                   =107019     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kTwoPointSize                 =107035     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kUnequallyDisposedToleranceZone=107026     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kVariableDistance             =107030     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kVolumeDiameter               =107042     # from enum FeatureControlFrameAdditionalSymbolsEnum
	kAlongEdgeFeatureDimension    =93191      # from enum FeatureDimensionTypeEnum
	kAngleFeatureDimension        =93185      # from enum FeatureDimensionTypeEnum
	kCircularCountFeatureDimension=93186      # from enum FeatureDimensionTypeEnum
	kHoleFeatureDimension         =93187      # from enum FeatureDimensionTypeEnum
	kLinearFeatureDimension       =93188      # from enum FeatureDimensionTypeEnum
	kRadialFeatureDimension       =93189      # from enum FeatureDimensionTypeEnum
	kRectangularCountFeatureDimension=93190      # from enum FeatureDimensionTypeEnum
	kMicrosoftAccessFormat        =74497      # from enum FileFormatEnum
	kMicrosoftExcelFormat         =74498      # from enum FileFormatEnum
	kTextFileCommaDelimitedFormat =74502      # from enum FileFormatEnum
	kTextFileTabDelimitedFormat   =74501      # from enum FileFormatEnum
	kUnicodeTextFileCommaDelimitedFormat=74504      # from enum FileFormatEnum
	kUnicodeTextFileTabDelimitedFormat=74503      # from enum FileFormatEnum
	kdBASEIIIFormat               =74499      # from enum FileFormatEnum
	kdBASEIVFormat                =74500      # from enum FileFormatEnum
	kCopyFileMask                 =224        # from enum FileManagementEnum
	kDeleteFileMask               =1          # from enum FileManagementEnum
	kForceFile                    =1          # from enum FileManagementEnum
	kMoveFileMask                 =225        # from enum FileManagementEnum
	kNoForceFile                  =0          # from enum FileManagementEnum
	kOverwriteExistingFile        =32         # from enum FileManagementEnum
	kOverwriteReadOnlyFile        =128        # from enum FileManagementEnum
	kOverwriteReservedFile        =64         # from enum FileManagementEnum
	kExclusiveOwnership           =68611      # from enum FileOwnershipEnum
	kNoOwnership                  =68609      # from enum FileOwnershipEnum
	kSaveOwnership                =68610      # from enum FileOwnershipEnum
	kAssemblyFileType             =56323      # from enum FileTypeEnum
	kAssociativeCADFileType       =56328      # from enum FileTypeEnum
	kDesignElementFileType        =56326      # from enum FileTypeEnum
	kDrawingFileType              =56324      # from enum FileTypeEnum
	kForeignFileType              =56327      # from enum FileTypeEnum
	kPartFileType                 =56322      # from enum FileTypeEnum
	kPresentationFileType         =56325      # from enum FileTypeEnum
	kUnknownFileType              =56321      # from enum FileTypeEnum
	kOpenCurrentVersion           =57858      # from enum FileVersionEnum
	kOpenOldVersion               =57857      # from enum FileVersionEnum
	kRestoreOldVersionToCurrent   =57859      # from enum FileVersionEnum
	kEdgeFillet                   =61697      # from enum FilletTypeEnum
	kFaceFillet                   =61698      # from enum FilletTypeEnum
	kFullRoundFillet              =61699      # from enum FilletTypeEnum
	kBendDownFlatPatternEdge      =64005      # from enum FlatPatternEdgeTypeEnum
	kBendUpFlatPatternEdge        =64004      # from enum FlatPatternEdgeTypeEnum
	kTangentFlatPatternEdge       =64001      # from enum FlatPatternEdgeTypeEnum
	kFlatPatternBackFace          =106755     # from enum FlatPatternFaceTypeEnum
	kFlatPatternDetailFace        =106756     # from enum FlatPatternFaceTypeEnum
	kFlatPatternFrontFace         =106754     # from enum FlatPatternFaceTypeEnum
	kFlatPatternUnknownFace       =106753     # from enum FlatPatternFaceTypeEnum
	kFrontViewFromModel           =80388      # from enum FrontViewPlaneEnum
	kFrontViewXYPlane             =80385      # from enum FrontViewPlaneEnum
	kFrontViewXZPlane             =80387      # from enum FrontViewPlaneEnum
	kFrontViewYZPlane             =80386      # from enum FrontViewPlaneEnum
	kGDTArcLength                 =104211     # from enum GDTSymbolEnum
	kGDTBetween                   =104213     # from enum GDTSymbolEnum
	kGDTControlledRadius          =104209     # from enum GDTSymbolEnum
	kGDTDiameter                  =104199     # from enum GDTSymbolEnum
	kGDTFreeState                 =104197     # from enum GDTSymbolEnum
	kGDTLeastMaterialCondition    =104195     # from enum GDTSymbolEnum
	kGDTMaximumMaterialCondition  =104194     # from enum GDTSymbolEnum
	kGDTNoSymbol                  =104193     # from enum GDTSymbolEnum
	kGDTProjectedToleranceZone    =104196     # from enum GDTSymbolEnum
	kGDTRadius                    =104201     # from enum GDTSymbolEnum
	kGDTReference                 =104210     # from enum GDTSymbolEnum
	kGDTSphericalDiameter         =104200     # from enum GDTSymbolEnum
	kGDTSphericalRadius           =104208     # from enum GDTSymbolEnum
	kGDTStatisticalTolerance      =104212     # from enum GDTSymbolEnum
	kGDTTangentPlane              =104198     # from enum GDTSymbolEnum
	kBooleanGeneralData           =52481      # from enum GeneralDataTypeEnum
	kCollectionGeneralData        =52482      # from enum GeneralDataTypeEnum
	kDoubleGeneralData            =52483      # from enum GeneralDataTypeEnum
	kIDispatchGeneralData         =52486      # from enum GeneralDataTypeEnum
	kIntegerGeneralData           =52484      # from enum GeneralDataTypeEnum
	kStringGeneralData            =52485      # from enum GeneralDataTypeEnum
	kVTableGeneralData            =52487      # from enum GeneralDataTypeEnum
	kProjectedGeneralDimension    =72194      # from enum GeneralDimensionTypeEnum
	kTrueGeneralDimension         =72193      # from enum GeneralDimensionTypeEnum
	kAngularity                   =32         # from enum GeometricCharacteristicEnum
	kAxiality                     =524288     # from enum GeometricCharacteristicEnum
	kAxisIntersection             =32768      # from enum GeometricCharacteristicEnum
	kCircularRunout               =1024       # from enum GeometricCharacteristicEnum
	kCircularRunoutFilled         =65536      # from enum GeometricCharacteristicEnum
	kCircularity                  =4          # from enum GeometricCharacteristicEnum
	kConcentricityAndCoaxiality   =512        # from enum GeometricCharacteristicEnum
	kCylindricity                 =8192       # from enum GeometricCharacteristicEnum
	kFlatness                     =2          # from enum GeometricCharacteristicEnum
	kParallelProfile              =16384      # from enum GeometricCharacteristicEnum
	kParallelism                  =128        # from enum GeometricCharacteristicEnum
	kPerpendicularity             =64         # from enum GeometricCharacteristicEnum
	kPosition                     =256        # from enum GeometricCharacteristicEnum
	kProfileOfASection            =262144     # from enum GeometricCharacteristicEnum
	kProfileOfAnyLine             =8          # from enum GeometricCharacteristicEnum
	kProfileOfAnySurface          =16         # from enum GeometricCharacteristicEnum
	kStraightness                 =1          # from enum GeometricCharacteristicEnum
	kSymmetry                     =2048       # from enum GeometricCharacteristicEnum
	kTotalRunout                  =4096       # from enum GeometricCharacteristicEnum
	kTotalRunoutFilled            =131072     # from enum GeometricCharacteristicEnum
	kAlwaysBreakGeometricConstraints=58370      # from enum GeometricConstraintsBreakageEnum
	kNeverBreakGeometricConstraints=58369      # from enum GeometricConstraintsBreakageEnum
	kPromptBreakGeometricConstraints=58371      # from enum GeometricConstraintsBreakageEnum
	kFixedGeometryMoveableStatus  =53507      # from enum GeometryMoveableStatusEnum
	kFreeToMoveGeometryMoveableStatus=53505      # from enum GeometryMoveableStatusEnum
	kMoveableByDimensionChangeGeometryMoveableStatus=53506      # from enum GeometryMoveableStatusEnum
	kUnknownGeometryMoveableStatus=53508      # from enum GeometryMoveableStatusEnum
	kConservativeOpenGLGraphicsDriver=61443      # from enum GraphicsDriverTypeEnum
	kDirect3D10GraphicsDriver     =61445      # from enum GraphicsDriverTypeEnum
	kDirect3D11GraphicsDriver     =61446      # from enum GraphicsDriverTypeEnum
	kDirect3DGraphicsDriver       =61441      # from enum GraphicsDriverTypeEnum
	kOpenGLGraphicsDriver         =61442      # from enum GraphicsDriverTypeEnum
	kSoftwareGraphics             =61444      # from enum GraphicsDriverTypeEnum
	kCoarseRes                    =128        # from enum GraphicsLevelsOfDetailEnum
	kFullScreenHighRes            =2048       # from enum GraphicsLevelsOfDetailEnum
	kMediumRes                    =512        # from enum GraphicsLevelsOfDetailEnum
	kMereDotRes                   =8          # from enum GraphicsLevelsOfDetailEnum
	kVeryCoarseRes                =32         # from enum GraphicsLevelsOfDetailEnum
	kZoomedInHighRes              =8192       # from enum GraphicsLevelsOfDetailEnum
	kConservativeGraphicsOptimization=55299      # from enum GraphicsOptimizationEnum
	kDriverGraphicsOptimization   =55300      # from enum GraphicsOptimizationEnum
	kFullGraphicsOptimization     =55298      # from enum GraphicsOptimizationEnum
	kRecommendedGraphicsOptimization=55297      # from enum GraphicsOptimizationEnum
	kAllGraphicsSelectable        =25347      # from enum GraphicsSelectabilityEnum
	kNoGraphicsSelectable         =25345      # from enum GraphicsSelectabilityEnum
	kSomeGraphicsSelectable       =25346      # from enum GraphicsSelectabilityEnum
	kCompatibilityGraphicsSetting =91651      # from enum GraphicsSettingTypeEnum
	kConservativeGraphicsSetting  =91652      # from enum GraphicsSettingTypeEnum
	kPerformanceGraphicsSetting   =91650      # from enum GraphicsSettingTypeEnum
	kQualityGraphicsSetting       =91649      # from enum GraphicsSettingTypeEnum
	kAllGraphicsVisible           =25091      # from enum GraphicsVisibilityEnum
	kNoGraphicsVisible            =25089      # from enum GraphicsVisibilityEnum
	kSomeGraphicsVisible          =25090      # from enum GraphicsVisibilityEnum
	kGroundShadow                 =69122      # from enum GroundShadowEnum
	kNoGroundShadow               =69121      # from enum GroundShadowEnum
	kXRayGroundShadow             =69123      # from enum GroundShadowEnum
	kEventCanceled                =515        # from enum HandlingCodeEnum
	kEventHandled                 =513        # from enum HandlingCodeEnum
	kEventNotHandled              =514        # from enum HandlingCodeEnum
	kHeadingAtBottom              =46338      # from enum HeadingPlacementEnum
	kHeadingAtTop                 =46337      # from enum HeadingPlacementEnum
	kNoHeading                    =46339      # from enum HeadingPlacementEnum
	kBeyondStopNodeHealth         =11785      # from enum HealthStatusEnum
	kCannotComputeHealth          =11783      # from enum HealthStatusEnum
	kDeletedHealth                =11782      # from enum HealthStatusEnum
	kDriverLostHealth             =11780      # from enum HealthStatusEnum
	kInErrorHealth                =11781      # from enum HealthStatusEnum
	kInconsistentHealth           =11786      # from enum HealthStatusEnum
	kInvalidLimitsHealth          =11789      # from enum HealthStatusEnum
	kJointDOFLockedHealth         =11790      # from enum HealthStatusEnum
	kNewlyAddedHealth             =11788      # from enum HealthStatusEnum
	kOutOfDateHealth              =11779      # from enum HealthStatusEnum
	kRedundantHealth              =11787      # from enum HealthStatusEnum
	kSuppressedHealth             =11784      # from enum HealthStatusEnum
	kUnknownHealth                =11777      # from enum HealthStatusEnum
	kUpToDateHealth               =11778      # from enum HealthStatusEnum
	kHeightDatumInner             =75522      # from enum HeightDatumTypeEnum
	kHeightDatumInnerOrtho        =75525      # from enum HeightDatumTypeEnum
	kHeightDatumOuter             =75521      # from enum HeightDatumTypeEnum
	kHeightDatumOuterOrtho        =75524      # from enum HeightDatumTypeEnum
	kHeightDatumTangent           =75523      # from enum HeightDatumTypeEnum
	kPitchAndHeightShapeType      =115714     # from enum HelicalShapeDefinitionTypeEnum
	kPitchAndRevolutionShapeType  =115713     # from enum HelicalShapeDefinitionTypeEnum
	kRevolutionAndHeightShapeType =115715     # from enum HelicalShapeDefinitionTypeEnum
	kSpiralShapeType              =115716     # from enum HelicalShapeDefinitionTypeEnum
	kFlatEndType                  =115970     # from enum HelixEndTypeEnum
	kNaturalEndType               =115969     # from enum HelixEndTypeEnum
	kDoubleHemType                =75268      # from enum HemTypeEnum
	kRolledHemType                =75267      # from enum HemTypeEnum
	kSingleHemType                =75265      # from enum HemTypeEnum
	kTeardropHemType              =75266      # from enum HemTypeEnum
	kNumberOfHolesInFeature       =83969      # from enum HoleNoteQuantityEnum
	kNumberOfLikeHolesNormalToView=83970      # from enum HoleNoteQuantityEnum
	kConcentricPlacementType      =48899      # from enum HolePlacementTypeEnum
	kLinearPlacementType          =48898      # from enum HolePlacementTypeEnum
	kPointPlacementType           =48900      # from enum HolePlacementTypeEnum
	kSketchPlacementType          =48897      # from enum HolePlacementTypeEnum
	kCBoreDepthHoleProperty       =77569      # from enum HolePropertyEnum
	kCBoreDiameterHoleProperty    =77570      # from enum HolePropertyEnum
	kCSinkAngleHoleProperty       =77571      # from enum HolePropertyEnum
	kCSinkDepthHoleProperty       =77572      # from enum HolePropertyEnum
	kCSinkDiameterHoleProperty    =77573      # from enum HolePropertyEnum
	kCustomDesignationHoleProperty=77574      # from enum HolePropertyEnum
	kCustomHoleProperty           =77594      # from enum HolePropertyEnum
	kDescriptionHoleProperty      =77575      # from enum HolePropertyEnum
	kFastenerTypeHoleProperty     =77578      # from enum HolePropertyEnum
	kFasternerFitHoleProperty     =77576      # from enum HolePropertyEnum
	kFasternerSizeHoleProperty    =77577      # from enum HolePropertyEnum
	kHoleDepthHoleProperty        =77580      # from enum HolePropertyEnum
	kHoleDiameterHoleProperty     =77581      # from enum HolePropertyEnum
	kHoleHoleProperty             =77579      # from enum HolePropertyEnum
	kPunchAngleHoleProperty       =77582      # from enum HolePropertyEnum
	kPunchDepthHoleProperty       =77583      # from enum HolePropertyEnum
	kPunchDirectionHoleProperty   =77584      # from enum HolePropertyEnum
	kPunchIdHoleProperty          =77585      # from enum HolePropertyEnum
	kQuantityHoleProperty         =77586      # from enum HolePropertyEnum
	kTapDrillDiameterHoleProperty =77587      # from enum HolePropertyEnum
	kThreadClassHoleProperty      =77588      # from enum HolePropertyEnum
	kThreadDepthHoleProperty      =77589      # from enum HolePropertyEnum
	kThreadDesignationHoleProperty=77590      # from enum HolePropertyEnum
	kThreadPitchHoleProperty      =77591      # from enum HolePropertyEnum
	kXDIMHoleProperty             =77592      # from enum HolePropertyEnum
	kYDIMHoleProperty             =77593      # from enum HolePropertyEnum
	kFeatureTypeHoleTable         =77827      # from enum HoleTableTypeEnum
	kSelectionTypeHoleTable       =77826      # from enum HoleTableTypeEnum
	kViewTypeHoleTable            =77825      # from enum HoleTableTypeEnum
	kCounterBoreHole              =21507      # from enum HoleTypeEnum
	kCounterSinkHole              =21506      # from enum HoleTypeEnum
	kDrilledHole                  =21505      # from enum HoleTypeEnum
	kSpotFaceHole                 =21508      # from enum HoleTypeEnum
	kAlignTextCenter              =19969      # from enum HorizontalTextAlignmentEnum
	kAlignTextLeft                =19970      # from enum HorizontalTextAlignmentEnum
	kAlignTextRight               =19971      # from enum HorizontalTextAlignmentEnum
	kDataDropIOMechanism          =13058      # from enum IOMechanismEnum
	kFileBrowseIOMechanism        =13059      # from enum IOMechanismEnum
	kPasteSpecialIOMechanism      =13060      # from enum IOMechanismEnum
	kUnspecifiedIOMechanism       =13057      # from enum IOMechanismEnum
	kAmberColorTheme              =87554      # from enum IconsColorTypeEnum
	kCobaltColorTheme             =87553      # from enum IconsColorTypeEnum
	kIgnoreDWGBodies              =113921     # from enum ImportDWGBodyStyleEnum
	kImportDWGBodiesAsWireframe   =113922     # from enum ImportDWGBodyStyleEnum
	kCentimeterUnitsType          =110084     # from enum ImportUnitsTypeEnum
	kFootUnitsType                =110083     # from enum ImportUnitsTypeEnum
	kInchUnitsType                =110082     # from enum ImportUnitsTypeEnum
	kMeterUnitsType               =110086     # from enum ImportUnitsTypeEnum
	kMicronUnitsType              =110087     # from enum ImportUnitsTypeEnum
	kMillimeterUnitsType          =110085     # from enum ImportUnitsTypeEnum
	kSourceUnitsType              =110081     # from enum ImportUnitsTypeEnum
	kAImportedAsMultibodyPart     =108546     # from enum ImportedAssemblyOrganizationTypeEnum
	kImportedAsAssembly           =108545     # from enum ImportedAssemblyOrganizationTypeEnum
	kImportedAsCompositeFeaturePart=108547     # from enum ImportedAssemblyOrganizationTypeEnum
	kImportedAsMultibodyPart      =108546     # from enum ImportedAssemblyOrganizationTypeEnum
	kAExcludedStatus              =109570     # from enum ImportedModelEntityStatusEnum
	kExcludedStatus               =109570     # from enum ImportedModelEntityStatusEnum
	kImportedAsIndividualSurfacesStatus=109571     # from enum ImportedModelEntityStatusEnum
	kIncludedStatus               =109569     # from enum ImportedModelEntityStatusEnum
	kAliasEntityType              =109825     # from enum ImportedModelEntityTypeEnum
	kAliasLayerEntityType         =109826     # from enum ImportedModelEntityTypeEnum
	kAliasSurfaceEntityType       =109827     # from enum ImportedModelEntityTypeEnum
	kAssemblyEntityType           =109828     # from enum ImportedModelEntityTypeEnum
	kPartEntityType               =109829     # from enum ImportedModelEntityTypeEnum
	kSolidEntityType              =109830     # from enum ImportedModelEntityTypeEnum
	kSurfaceEntityType            =109831     # from enum ImportedModelEntityTypeEnum
	kMeshesModelGeometryType      =4          # from enum ImportedModelGeometryTypeEnum
	kSolidsModelGeometryType      =1          # from enum ImportedModelGeometryTypeEnum
	kSurfacesModelGeometryType    =2          # from enum ImportedModelGeometryTypeEnum
	kWiresModelGeometryType       =8          # from enum ImportedModelGeometryTypeEnum
	kImportedAsCompositeFeatures  =108802     # from enum ImportedSurfaceOrganizationTypeEnum
	kImportedAsSingleCompositeFeature=108803     # from enum ImportedSurfaceOrganizationTypeEnum
	kImportedAsSurfaceBodies      =108801     # from enum ImportedSurfaceOrganizationTypeEnum
	kWorkAxesWorkGeometryType     =4          # from enum ImportedWorkGeometryTypeEnum
	kWorkPlanesWorkGeometryType   =1          # from enum ImportedWorkGeometryTypeEnum
	kWorkPointsWorkGeometryType   =2          # from enum ImportedWorkGeometryTypeEnum
	kAmountOfValueIncrement       =102913     # from enum IncrementTypeEnum
	kNumberOfStepsIncrement       =102914     # from enum IncrementTypeEnum
	kInferredLine                 =24834      # from enum InferredTypeEnum
	kInferredPoint                =24835      # from enum InferredTypeEnum
	kNoInference                  =24833      # from enum InferredTypeEnum
	kInsertAfter                  =1          # from enum InsertionLocationTypeEnum
	kInsertBefore                 =0          # from enum InsertionLocationTypeEnum
	kInsertUnder                  =2          # from enum InsertionLocationTypeEnum
	kAngularEndsInspectionBorder  =79362      # from enum InspectionDimensionShapeEnum
	kNoInspectionBorder           =79361      # from enum InspectionDimensionShapeEnum
	kRoundedEndsInspectionBorder  =79363      # from enum InspectionDimensionShapeEnum
	kGeometryIntent               =58116      # from enum IntentTypeEnum
	kNoPointIntent                =58117      # from enum IntentTypeEnum
	kParameterIntent              =58115      # from enum IntentTypeEnum
	kPoint2dIntent                =58114      # from enum IntentTypeEnum
	kPointEnumIntent              =58113      # from enum IntentTypeEnum
	kPointIntent                  =58118      # from enum IntentTypeEnum
	kKeyboardInteraction          =4          # from enum InteractionEventsEnum
	kMouseAndKeyboardInteraction  =6          # from enum InteractionEventsEnum
	kMouseInteraction             =2          # from enum InteractionEventsEnum
	kNoInteraction                =0          # from enum InteractionEventsEnum
	kSelectAndKeyboardInteraction =5          # from enum InteractionEventsEnum
	kSelectInteraction            =1          # from enum InteractionEventsEnum
	kAllComponentsInteractiveContact=64770      # from enum InteractiveContactAnalysisEnum
	kContactSetOnlyInteractiveContact=64769      # from enum InteractiveContactAnalysisEnum
	kSolverOffInteractiveContact  =64771      # from enum InteractiveContactAnalysisEnum
	kAllSurfacesInteractiveContact=65025      # from enum InteractiveContactSurfacesEnum
	kGeneralSurfacesInteractiveContact=65026      # from enum InteractiveContactSurfacesEnum
	kSimpleSurfacesInteractiveContact=65027      # from enum InteractiveContactSurfacesEnum
	kClassicInterface             =87810      # from enum InterfaceStyleEnum
	kRibbonInterface              =87809      # from enum InterfaceStyleEnum
	kAngularInBothDirections      =4          # from enum LayDirectionTypeEnum
	kCircularRelativeToCenter     =16         # from enum LayDirectionTypeEnum
	kMultidirectional             =8          # from enum LayDirectionTypeEnum
	kParallelToPlaneOfProjection  =1          # from enum LayDirectionTypeEnum
	kParticulateNondirectional    =64         # from enum LayDirectionTypeEnum
	kPerpendicularToPlaneOfProjection=2          # from enum LayDirectionTypeEnum
	kRadialRelativeToCenter       =32         # from enum LayDirectionTypeEnum
	kAllComponentsSuppressedLevelOfDetail=56066      # from enum LevelOfDetailEnum
	kAllContentSuppressedLevelOfDetail=56068      # from enum LevelOfDetailEnum
	kAllPartsSuppressedLevelOfDetail=56067      # from enum LevelOfDetailEnum
	kCustomLevelOfDetail          =56072      # from enum LevelOfDetailEnum
	kLastActiveLevelOfDetail      =56073      # from enum LevelOfDetailEnum
	kMasterLevelOfDetail          =56065      # from enum LevelOfDetailEnum
	kSandboxLevelOfDetail         =56069      # from enum LevelOfDetailEnum
	kSubstituteLevelOfDetail      =56071      # from enum LevelOfDetailEnum
	kTransientLevelOfDetail       =56070      # from enum LevelOfDetailEnum
	kDirectionalLight             =53249      # from enum LightDefinitionTypeEnum
	kPointLight                   =53250      # from enum LightDefinitionTypeEnum
	kSpotLight                    =53251      # from enum LightDefinitionTypeEnum
	kGroundPlaneSpaceLight        =52995      # from enum LightTypeEnum
	kModelSpaceLight              =52993      # from enum LightTypeEnum
	kViewSpaceLight               =52994      # from enum LightTypeEnum
	kHybridSpace                  =49923      # from enum LineDefinitionSpaceEnum
	kModelSpace                   =49922      # from enum LineDefinitionSpaceEnum
	kScreenSpace                  =49921      # from enum LineDefinitionSpaceEnum
	kDoubleLineSpacing            =45826      # from enum LineSpacingEnum
	kSingleLineSpacing            =45825      # from enum LineSpacingEnum
	kTripleLineSpacing            =45827      # from enum LineSpacingEnum
	kChainLineType                =37644      # from enum LineTypeEnum
	kContinuousLineType           =37633      # from enum LineTypeEnum
	kCustomLineType               =37649      # from enum LineTypeEnum
	kDashDottedLineType           =37638      # from enum LineTypeEnum
	kDashedDoubleDottedLineType   =37645      # from enum LineTypeEnum
	kDashedHiddenLineType         =37641      # from enum LineTypeEnum
	kDashedLineType               =37634      # from enum LineTypeEnum
	kDashedTripleDottedLineType   =37647      # from enum LineTypeEnum
	kDefaultLineType              =37648      # from enum LineTypeEnum
	kDottedLineType               =37636      # from enum LineTypeEnum
	kDoubleDashDoubleDottedLineType=37639      # from enum LineTypeEnum
	kDoubleDashedChainLineType    =37637      # from enum LineTypeEnum
	kDoubleDashedDottedLineType   =37646      # from enum LineTypeEnum
	kDoubleDashedTripleDottedLineType=37640      # from enum LineTypeEnum
	kLongDashDottedLineType       =37642      # from enum LineTypeEnum
	kLongDashTripleDottedLineType =37643      # from enum LineTypeEnum
	kLongDashedDoubleDottedLineType=37635      # from enum LineTypeEnum
	kRangeLineWeight              =66050      # from enum LineWeightTypeEnum
	kTrueLineWeight               =66049      # from enum LineWeightTypeEnum
	kDiametricLinearDimension     =66306      # from enum LinearDimensionTypeEnum
	kRegularLinearDimension       =66305      # from enum LinearDimensionTypeEnum
	kSymmetricLinearDimension     =66307      # from enum LinearDimensionTypeEnum
	kEightDecimalPlacesLinearPrecision=41737      # from enum LinearPrecisionEnum
	kEighthsFractionalLinearPrecision=41741      # from enum LinearPrecisionEnum
	kFiveDecimalPlacesLinearPrecision=41734      # from enum LinearPrecisionEnum
	kFourDecimalPlacesLinearPrecision=41733      # from enum LinearPrecisionEnum
	kHalfFractionalLinearPrecision=41739      # from enum LinearPrecisionEnum
	kOneDecimalPlaceLinearPrecision=41730      # from enum LinearPrecisionEnum
	kOneTwentyEighthsFractionalLinearPrecision=41745      # from enum LinearPrecisionEnum
	kQuarterFractionalLinearPrecision=41740      # from enum LinearPrecisionEnum
	kSevenDecimalPlacesLinearPrecision=41736      # from enum LinearPrecisionEnum
	kSixDecimalPlacesLinearPrecision=41735      # from enum LinearPrecisionEnum
	kSixteenthsFractionalLinearPrecision=41742      # from enum LinearPrecisionEnum
	kSixtyFourthsFractionalLinearPrecision=41744      # from enum LinearPrecisionEnum
	kThirtySecondsFractionalLinearPrecision=41743      # from enum LinearPrecisionEnum
	kThreeDecimalPlacesLinearPrecision=41732      # from enum LinearPrecisionEnum
	kTwoDecimalPlacesLinearPrecision=41731      # from enum LinearPrecisionEnum
	kZeroDecimalPlaceLinearPrecision=41729      # from enum LinearPrecisionEnum
	kZeroFractionalLinearPrecision=41738      # from enum LinearPrecisionEnum
	kAmbiguousStatus              =16         # from enum LinkStatusEnum
	kMissingStatus                =1          # from enum LinkStatusEnum
	kOutOfDateStatus              =4          # from enum LinkStatusEnum
	kSourceNewerStatus            =8          # from enum LinkStatusEnum
	kUpToDateStatus               =2          # from enum LinkStatusEnum
	kLibraryLocation              =45060      # from enum LocationTypeEnum
	kLocalLocation                =45058      # from enum LocationTypeEnum
	kOwnerDirectoryLocation       =45062      # from enum LocationTypeEnum
	kUnknownLocation              =45061      # from enum LocationTypeEnum
	kWorkgroupLocation            =45059      # from enum LocationTypeEnum
	kWorkspaceLocation            =45057      # from enum LocationTypeEnum
	kAngleLoftCondition           =34307      # from enum LoftConditionEnum
	kDirectionLoftCondition       =34307      # from enum LoftConditionEnum
	kFreeLoftCondition            =34305      # from enum LoftConditionEnum
	kSharpPointLoftCondition      =34309      # from enum LoftConditionEnum
	kSmoothLoftCondition          =34308      # from enum LoftConditionEnum
	kTangentLoftCondition         =34306      # from enum LoftConditionEnum
	kTangentToPlaneLoftCondition  =34310      # from enum LoftConditionEnum
	kLoftWithAreaGraphSections    =60932      # from enum LoftTypeEnum
	kLoftWithCenterline           =60931      # from enum LoftTypeEnum
	kLoftWithRails                =60930      # from enum LoftTypeEnum
	kRegularLoft                  =60929      # from enum LoftTypeEnum
	kDieFormedLoftedFlange        =91137      # from enum LoftedFlangeOutputTypeEnum
	kPressBrakeChordToleranceLoftedFlange=91138      # from enum LoftedFlangeOutputTypeEnum
	kPressBrakeFacetAngleLoftedFlange=91139      # from enum LoftedFlangeOutputTypeEnum
	kPressBrakeFacetDistanceLoftedFlange=91140      # from enum LoftedFlangeOutputTypeEnum
	kAllManipulatorElements       =0          # from enum ManipulatorElementEnum
	kManipulatorOriginScaleElement=1024       # from enum ManipulatorElementEnum
	kManipulatorOriginTranslationElement=1          # from enum ManipulatorElementEnum
	kManipulatorXRotationElement  =128        # from enum ManipulatorElementEnum
	kManipulatorXScaleElement     =2048       # from enum ManipulatorElementEnum
	kManipulatorXTranslationElement=2          # from enum ManipulatorElementEnum
	kManipulatorXYScaleElement    =16384      # from enum ManipulatorElementEnum
	kManipulatorXYTranslationElement=16         # from enum ManipulatorElementEnum
	kManipulatorXZScaleElement    =32768      # from enum ManipulatorElementEnum
	kManipulatorXZTranslationElement=32         # from enum ManipulatorElementEnum
	kManipulatorYRotationElement  =256        # from enum ManipulatorElementEnum
	kManipulatorYScaleElement     =4096       # from enum ManipulatorElementEnum
	kManipulatorYTranslationElement=4          # from enum ManipulatorElementEnum
	kManipulatorYZScaleElement    =65536      # from enum ManipulatorElementEnum
	kManipulatorYZTranslationElement=64         # from enum ManipulatorElementEnum
	kManipulatorZRotationElement  =512        # from enum ManipulatorElementEnum
	kManipulatorZScaleElement     =8192       # from enum ManipulatorElementEnum
	kManipulatorZTranslationElement=8          # from enum ManipulatorElementEnum
	kMarkedViewAllDataType        =15         # from enum MarkedViewDataTypeEnum
	kMarkedViewAppearanceDataType =2          # from enum MarkedViewDataTypeEnum
	kMarkedViewNoneDataType       =0          # from enum MarkedViewDataTypeEnum
	kMarkedViewTrailDataType      =8          # from enum MarkedViewDataTypeEnum
	kMarkedViewTransformationDataType=4          # from enum MarkedViewDataTypeEnum
	kMarkedViewVisibilityDataType =1          # from enum MarkedViewDataTypeEnum
	k_High                        =24579      # from enum MassPropertiesAccuracyEnum
	k_Low                         =24577      # from enum MassPropertiesAccuracyEnum
	k_Medium                      =24578      # from enum MassPropertiesAccuracyEnum
	k_None                        =24581      # from enum MassPropertiesAccuracyEnum
	k_VeryHigh                    =24580      # from enum MassPropertiesAccuracyEnum
	kAlignedSolutionType          =115458     # from enum MateConstraintSolutionTypeEnum
	kNoSolutionType               =115460     # from enum MateConstraintSolutionTypeEnum
	kOpposedSolutionType          =115457     # from enum MateConstraintSolutionTypeEnum
	kUndirectedSolutionType       =115459     # from enum MateConstraintSolutionTypeEnum
	kLeastMaterialCondition       =114180     # from enum MaterialConditionEnum
	kMaterialConditionNotSpecified=114177     # from enum MaterialConditionEnum
	kMaximumMaterialCondition     =114179     # from enum MaterialConditionEnum
	kRegardlessOfFeatureSizeMaterialCondition=114178     # from enum MaterialConditionEnum
	kMaterialDisplayUnitsEnglishFoot=98824      # from enum MaterialDisplayUnitsEnum
	kMaterialDisplayUnitsEnglishInch=98823      # from enum MaterialDisplayUnitsEnum
	kMaterialDisplayUnitsEnglishStandard=98822      # from enum MaterialDisplayUnitsEnum
	kMaterialDisplayUnitsMetricCGS=98820      # from enum MaterialDisplayUnitsEnum
	kMaterialDisplayUnitsMetricMKS=98818      # from enum MaterialDisplayUnitsEnum
	kMaterialDisplayUnitsMetricMMNS=98819      # from enum MaterialDisplayUnitsEnum
	kMaterialDisplayUnitsMetricStandard=98817      # from enum MaterialDisplayUnitsEnum
	kMaterialDisplayUnitsMetricUMNS=98821      # from enum MaterialDisplayUnitsEnum
	kBetweenModifier              =128        # from enum MaterialRemovalModifierEnum
	kContinuousFeatureModifier    =8192       # from enum MaterialRemovalModifierEnum
	kDiameterModifier             =256        # from enum MaterialRemovalModifierEnum
	kEnvelopeRequirementModifier  =512        # from enum MaterialRemovalModifierEnum
	kFreeStateModifier            =16         # from enum MaterialRemovalModifierEnum
	kFromToModifier               =32768      # from enum MaterialRemovalModifierEnum
	kLeastMaterialConditionModifier=2          # from enum MaterialRemovalModifierEnum
	kMaximumMaterialConditionModifier=1          # from enum MaterialRemovalModifierEnum
	kMedianFeatureModifier        =16384      # from enum MaterialRemovalModifierEnum
	kProjectedToleranceZoneModifier=4          # from enum MaterialRemovalModifierEnum
	kReciprocityModifier          =1024       # from enum MaterialRemovalModifierEnum
	kRegardlessOfFeatureSizeModifier=32         # from enum MaterialRemovalModifierEnum
	kSquareModifier               =2048       # from enum MaterialRemovalModifierEnum
	kStatisticalToleranceModifier =64         # from enum MaterialRemovalModifierEnum
	kTangentPlaneModifier         =8          # from enum MaterialRemovalModifierEnum
	kUnequallyDisposedModifier    =4096       # from enum MaterialRemovalModifierEnum
	kAngleMeasure                 =72706      # from enum MeasureTypeEnum
	kDistanceMeasure              =72705      # from enum MeasureTypeEnum
	kDataObjectMedium             =56578      # from enum MediumTypeEnum
	kFileNameMedium               =56577      # from enum MediumTypeEnum
	kStreamMedium                 =56579      # from enum MediumTypeEnum
	kStringMedium                 =56580      # from enum MediumTypeEnum
	kEditActiveMember             =57601      # from enum MemberEditScopeEnum
	kEditAllMembers               =57602      # from enum MemberEditScopeEnum
	kMemberManagerDifferentFamily =50410517   # from enum MemberManagerErrorsEnum
	kMemberManagerDifferentMember =50410518   # from enum MemberManagerErrorsEnum
	kMemberManagerFeatureSuppressFail=50410521   # from enum MemberManagerErrorsEnum
	kMemberManagerInvalidMemberValue=50410524   # from enum MemberManagerErrorsEnum
	kMemberManagerLongFilename    =50410520   # from enum MemberManagerErrorsEnum
	kMemberManagerMaterialNotFound=50410519   # from enum MemberManagerErrorsEnum
	kMemberManagerMissingFileWritePermission=50410516   # from enum MemberManagerErrorsEnum
	kMemberManagerNoError         =50410511   # from enum MemberManagerErrorsEnum
	kMemberManagerThreadCreateFail=50410523   # from enum MemberManagerErrorsEnum
	kMemberManagerThreadFeatureNotFound=50410522   # from enum MemberManagerErrorsEnum
	kMemberManagerUnknown         =50410512   # from enum MemberManagerErrorsEnum
	kMemberManagerVaultCheckoutFail=50410514   # from enum MemberManagerErrorsEnum
	kMemberManagerVaultFileStatusFail=50410513   # from enum MemberManagerErrorsEnum
	kMemberManagerVaultGetLatestVersionFail=50410515   # from enum MemberManagerErrorsEnum
	kEventMember                  =30721      # from enum MemberTypeEnum
	kFunctionMember               =30723      # from enum MemberTypeEnum
	kPropertyMember               =30724      # from enum MemberTypeEnum
	kSubMember                    =30722      # from enum MemberTypeEnum
	kAlwaysSaveMemoryMode         =65282      # from enum MemorySavingModeEnum
	kNeverSaveMemoryMode          =65283      # from enum MemorySavingModeEnum
	kUseApplicationOptionsMemoryMode=65281      # from enum MemorySavingModeEnum
	kAllMeshEdgesVisible          =111361     # from enum MeshEdgesVisibilityEnum
	kNoMeshEdgesVisible           =111362     # from enum MeshEdgesVisibilityEnum
	kSomeMeshEdgesVisible         =111363     # from enum MeshEdgesVisibilityEnum
	kAllMeshFeaturesSuppressed    =111617     # from enum MeshFeaturesSuppressionEnum
	kNoMeshFeaturesSuppressed     =111618     # from enum MeshFeaturesSuppressionEnum
	kSomeMeshFeaturesSuppressed   =111619     # from enum MeshFeaturesSuppressionEnum
	kAllMeshFeaturesVisible       =111105     # from enum MeshFeaturesVisibilityEnum
	kNoMeshFeaturesVisible        =111106     # from enum MeshFeaturesVisibilityEnum
	kSomeMeshFeaturesVisible      =111107     # from enum MeshFeaturesVisibilityEnum
	kMigrateCustomSettingsFailed  =116481     # from enum MigrateCustomSettingsResultEnum
	kMigrateCustomSettingsSuccess =116482     # from enum MigrateCustomSettingsResultEnum
	kMigrateCustomSettingsSuccessRestart=116483     # from enum MigrateCustomSettingsResultEnum
	kButton                       =95233      # from enum MiniToolbarControlTypeEnum
	kCheckBox                     =95234      # from enum MiniToolbarControlTypeEnum
	kComboBox                     =95235      # from enum MiniToolbarControlTypeEnum
	kDropdown                     =95236      # from enum MiniToolbarControlTypeEnum
	kLabel                        =95237      # from enum MiniToolbarControlTypeEnum
	kSeparator                    =95239      # from enum MiniToolbarControlTypeEnum
	kSlider                       =95241      # from enum MiniToolbarControlTypeEnum
	kTextBox                      =95243      # from enum MiniToolbarControlTypeEnum
	kTextEditor                   =95242      # from enum MiniToolbarControlTypeEnum
	kValueEditor                  =95240      # from enum MiniToolbarControlTypeEnum
	kThreadMajorDiameter          =21761      # from enum ModelDiameterFromThreadEnum
	kThreadMinorDiameter          =21762      # from enum ModelDiameterFromThreadEnum
	kThreadPitchDiameter          =21763      # from enum ModelDiameterFromThreadEnum
	kThreadTapDrillDiameter       =21764      # from enum ModelDiameterFromThreadEnum
	kToleranceFeatureConstrained  =0          # from enum ModelToleranceFeatureConstrainedStatusEnum
	kToleranceFeatureConstrainedStatusUnknown=2          # from enum ModelToleranceFeatureConstrainedStatusEnum
	kToleranceFeatureUnConstrained=1          # from enum ModelToleranceFeatureConstrainedStatusEnum
	kArcToleranceFeature          =112903     # from enum ModelToleranceFeatureTypeEnum
	kBallToleranceFeature         =112923     # from enum ModelToleranceFeatureTypeEnum
	kBendSurfaceToleranceFeature  =112952     # from enum ModelToleranceFeatureTypeEnum
	kBlindHoleToleranceFeature    =112936     # from enum ModelToleranceFeatureTypeEnum
	kBlindThreadToleranceFeature  =112946     # from enum ModelToleranceFeatureTypeEnum
	kChamferToleranceFeature      =112927     # from enum ModelToleranceFeatureTypeEnum
	kCoaxialAxesToleranceFeature  =112961     # from enum ModelToleranceFeatureTypeEnum
	kCocylindricalGroupToleranceFeature=112940     # from enum ModelToleranceFeatureTypeEnum
	kConeToleranceFeature         =112904     # from enum ModelToleranceFeatureTypeEnum
	kCoplanarGroupToleranceFeature=112939     # from enum ModelToleranceFeatureTypeEnum
	kCounterboreToleranceFeature  =112943     # from enum ModelToleranceFeatureTypeEnum
	kCountersinkToleranceFeature  =112944     # from enum ModelToleranceFeatureTypeEnum
	kCurveToleranceFeature        =112908     # from enum ModelToleranceFeatureTypeEnum
	kCylinderToleranceFeature     =112899     # from enum ModelToleranceFeatureTypeEnum
	kCylindricalGroupToleranceFeature=112929     # from enum ModelToleranceFeatureTypeEnum
	kDraftedHoleToleranceFeature  =112920     # from enum ModelToleranceFeatureTypeEnum
	kDraftedShaftToleranceFeature =112919     # from enum ModelToleranceFeatureTypeEnum
	kDraftedSlotToleranceFeature  =112926     # from enum ModelToleranceFeatureTypeEnum
	kDraftedSlottedHoleToleranceFeature=112922     # from enum ModelToleranceFeatureTypeEnum
	kDraftedSquareToleranceFeature=112915     # from enum ModelToleranceFeatureTypeEnum
	kDraftedTabslotToleranceFeature=112916     # from enum ModelToleranceFeatureTypeEnum
	kDraftedWidthToleranceFeature =112914     # from enum ModelToleranceFeatureTypeEnum
	kDrilledHoleToleranceFeature  =112937     # from enum ModelToleranceFeatureTypeEnum
	kExtrudedGroupToleranceFeature=112930     # from enum ModelToleranceFeatureTypeEnum
	kGeneralGroupToleranceFeature =112932     # from enum ModelToleranceFeatureTypeEnum
	kHoleToleranceFeature         =112918     # from enum ModelToleranceFeatureTypeEnum
	kLineToleranceFeature         =112902     # from enum ModelToleranceFeatureTypeEnum
	kLinearPatternToleranceFeature=112933     # from enum ModelToleranceFeatureTypeEnum
	kMultiElementHoleToleranceFeature=112938     # from enum ModelToleranceFeatureTypeEnum
	kNonParallelAxesToleranceFeature=112963     # from enum ModelToleranceFeatureTypeEnum
	kNonParallelMidPlanesToleranceFeature=112965     # from enum ModelToleranceFeatureTypeEnum
	kOpposedConesToleranceFeature =112942     # from enum ModelToleranceFeatureTypeEnum
	kOpposedCylindersToleranceFeature=112941     # from enum ModelToleranceFeatureTypeEnum
	kParallelAxesToleranceFeature =112962     # from enum ModelToleranceFeatureTypeEnum
	kParallelMidPlanesToleranceFeature=112964     # from enum ModelToleranceFeatureTypeEnum
	kPipeToleranceFeature         =112909     # from enum ModelToleranceFeatureTypeEnum
	kPlanarGroupToleranceFeature  =112928     # from enum ModelToleranceFeatureTypeEnum
	kPlaneToleranceFeature        =112898     # from enum ModelToleranceFeatureTypeEnum
	kPointToleranceFeature        =112900     # from enum ModelToleranceFeatureTypeEnum
	kPolarPatternToleranceFeature =112934     # from enum ModelToleranceFeatureTypeEnum
	kPrismToleranceFeature        =112906     # from enum ModelToleranceFeatureTypeEnum
	kRadialPatternToleranceFeature=112935     # from enum ModelToleranceFeatureTypeEnum
	kRevolvedGroupToleranceFeature=112931     # from enum ModelToleranceFeatureTypeEnum
	kRevolvedToleranceFeature     =112905     # from enum ModelToleranceFeatureTypeEnum
	kRolledSurfaceToleranceFeature=112953     # from enum ModelToleranceFeatureTypeEnum
	kSMPairAnchoredAxialToleranceFeature=112958     # from enum ModelToleranceFeatureTypeEnum
	kSMPairAsymmetricToleranceFeature=112960     # from enum ModelToleranceFeatureTypeEnum
	kSMPairAxialToleranceFeature  =112956     # from enum ModelToleranceFeatureTypeEnum
	kSMPairPlanarToleranceFeature =112957     # from enum ModelToleranceFeatureTypeEnum
	kSMPairPrismaticToleranceFeature=112959     # from enum ModelToleranceFeatureTypeEnum
	kSMPairSphericalToleranceFeature=112955     # from enum ModelToleranceFeatureTypeEnum
	kSMWallToleranceFeature       =112954     # from enum ModelToleranceFeatureTypeEnum
	kShaftToleranceFeature        =112917     # from enum ModelToleranceFeatureTypeEnum
	kSlotToleranceFeature         =112925     # from enum ModelToleranceFeatureTypeEnum
	kSlottedHoleToleranceFeature  =112921     # from enum ModelToleranceFeatureTypeEnum
	kSocketToleranceFeature       =112924     # from enum ModelToleranceFeatureTypeEnum
	kSphereToleranceFeature       =112913     # from enum ModelToleranceFeatureTypeEnum
	kSplitDraftHoleToleranceFeature=112948     # from enum ModelToleranceFeatureTypeEnum
	kSplitDraftShaftToleranceFeature=112947     # from enum ModelToleranceFeatureTypeEnum
	kSplitDraftSlabToleranceFeature=112949     # from enum ModelToleranceFeatureTypeEnum
	kSplitDraftSlotToleranceFeature=112950     # from enum ModelToleranceFeatureTypeEnum
	kSplitDraftSlottedHoleToleranceFeature=112951     # from enum ModelToleranceFeatureTypeEnum
	kSquareToleranceFeature       =112912     # from enum ModelToleranceFeatureTypeEnum
	kSurfaceToleranceFeature      =112907     # from enum ModelToleranceFeatureTypeEnum
	kTabslotToleranceFeature      =112911     # from enum ModelToleranceFeatureTypeEnum
	kThruThreadToleranceFeature   =112945     # from enum ModelToleranceFeatureTypeEnum
	kTorusToleranceFeature        =112901     # from enum ModelToleranceFeatureTypeEnum
	kUnknownToleranceFeature      =112897     # from enum ModelToleranceFeatureTypeEnum
	kWidthToleranceFeature        =112910     # from enum ModelToleranceFeatureTypeEnum
	kLowerValue                   =31490      # from enum ModelValueTypeEnum
	kMedianValue                  =31492      # from enum ModelValueTypeEnum
	kNominalValue                 =31489      # from enum ModelValueTypeEnum
	kUpperValue                   =31491      # from enum ModelValueTypeEnum
	kLeftMouseButton              =1          # from enum MouseButtonEnum
	kMiddleMouseButton            =4          # from enum MouseButtonEnum
	kNoneMouseButton              =0          # from enum MouseButtonEnum
	kRightMouseButton             =2          # from enum MouseButtonEnum
	kDragEnter                    =15617      # from enum MouseDragStateEnum
	kDragLeave                    =15618      # from enum MouseDragStateEnum
	kDragOver                     =15619      # from enum MouseDragStateEnum
	kDragUnknown                  =15620      # from enum MouseDragStateEnum
	kDirectionAndDistanceMoveType =91393      # from enum MoveFaceTypeEnum
	kFreeMoveType                 =91395      # from enum MoveFaceTypeEnum
	kPlanarMoveType               =91394      # from enum MoveFaceTypeEnum
	kAllAboveLandingLine          =101634     # from enum MultiLineDimensionTextEnum
	kAllAboveLandingLineWithUnderline=101635     # from enum MultiLineDimensionTextEnum
	kFirstLineAboveLandingLine    =101636     # from enum MultiLineDimensionTextEnum
	kFirstLineCenteredOnLandingLine=101633     # from enum MultiLineDimensionTextEnum
	kJISAlignment                 =101637     # from enum MultiLineDimensionTextEnum
	kSemiIsolatedMode             =36355      # from enum MultiUserModeEnum
	kSemiIsolatedNoCheckoutMode   =36356      # from enum MultiUserModeEnum
	kSharedMode                   =36354      # from enum MultiUserModeEnum
	kSingleUserMode               =36353      # from enum MultiUserModeEnum
	kVaultMode                    =36357      # from enum MultiUserModeEnum
	kHomePageContentType          =107521     # from enum MyHomeContentTypeEnum
	kTeamWebContentType           =107522     # from enum MyHomeContentTypeEnum
	kOverallNormal                =19716      # from enum NormalBindingEnum
	kPerItemNormals               =19715      # from enum NormalBindingEnum
	kPerStripNormals              =19714      # from enum NormalBindingEnum
	kPerVertexNormals             =19713      # from enum NormalBindingEnum
	kLowercaseAlphaNumbering      =61186      # from enum NumberingSchemeEnum
	kNumericNumbering             =61185      # from enum NumberingSchemeEnum
	kUppercaseAlphaNumbering      =61187      # from enum NumberingSchemeEnum
	kCircularConicalFaceOGSGeometryType=100105     # from enum OGSGeometryTypeEnum
	kCircularCylindricalFaceOGSGeometryType=100103     # from enum OGSGeometryTypeEnum
	kCircularEdgeOGSGeometryType  =100099     # from enum OGSGeometryTypeEnum
	kEllipticCylindricalFaceOGSGeometryType=100104     # from enum OGSGeometryTypeEnum
	kEllipticalConicalFaceOGSGeometryType=100106     # from enum OGSGeometryTypeEnum
	kEllipticalEdgeOGSGeometryType=100100     # from enum OGSGeometryTypeEnum
	kLinearEdgeOGSGeometryType    =100098     # from enum OGSGeometryTypeEnum
	kPlanarFaceOGSGeometryType    =100102     # from enum OGSGeometryTypeEnum
	kSphericalFaceOGSGeometryType =100107     # from enum OGSGeometryTypeEnum
	kSplineEdgeOGSGeometryType    =100101     # from enum OGSGeometryTypeEnum
	kSplineFaceOGSGeometryType    =100108     # from enum OGSGeometryTypeEnum
	kToroidalFaceOGSGeometryType  =100109     # from enum OGSGeometryTypeEnum
	kUnknownOGSGeometryType       =100097     # from enum OGSGeometryTypeEnum
	kLineListOGSPrimitiveType     =99843      # from enum OGSPrimitiveTypeEnum
	kLineStripOGSPrimitiveType    =99844      # from enum OGSPrimitiveTypeEnum
	kNoneOGSPrimitiveType         =99841      # from enum OGSPrimitiveTypeEnum
	kPointListOGSPrimitiveType    =99842      # from enum OGSPrimitiveTypeEnum
	kTriangleListOGSPrimitiveType =99845      # from enum OGSPrimitiveTypeEnum
	kTriangleStripOGSPrimitiveType=99846      # from enum OGSPrimitiveTypeEnum
	kBodyOGSSceneNodeType         =100355     # from enum OGSSceneNodeTypeEnum
	kComponentOGSSceneNodeType    =100354     # from enum OGSSceneNodeTypeEnum
	kUnknownOGSSceneNodeType      =100353     # from enum OGSSceneNodeTypeEnum
	kOLEDocumentEmbeddingObject   =3330       # from enum OLEDocumentTypeEnum
	kOLEDocumentLinkObject        =3331       # from enum OLEDocumentTypeEnum
	kOLEDocumentUnknownObject     =3329       # from enum OLEDocumentTypeEnum
	kDefaultOLEVerb               =3076       # from enum OLEVerbEnum
	kEditOpenOLEVerb              =3073       # from enum OLEVerbEnum
	kHideOLEVerb                  =3075       # from enum OLEVerbEnum
	kShowOLEVerb                  =3074       # from enum OLEVerbEnum
	k3dAViewObject                =83956224   # from enum ObjectTypeEnum
	kASideDefinition              =151025152  # from enum ObjectTypeEnum
	kASideDefinitions             =151024896  # from enum ObjectTypeEnum
	kAliasFreeformFeatureObject   =84011264   # from enum ObjectTypeEnum
	kAliasFreeformFeatureProxyObject=84011008   # from enum ObjectTypeEnum
	kAliasFreeformFeaturesObject  =84011520   # from enum ObjectTypeEnum
	kAnalysisManagerObject        =50417152   # from enum ObjectTypeEnum
	kAnalyticEdgeWorkAxisDefObject=83979520   # from enum ObjectTypeEnum
	kAngleConstraintObject        =100665088  # from enum ObjectTypeEnum
	kAngleConstraintProxyObject   =100675584  # from enum ObjectTypeEnum
	kAngleExtentObject            =83918080   # from enum ObjectTypeEnum
	kAngleiMateDefinitionObject   =83947008   # from enum ObjectTypeEnum
	kAngleiMateDefinitionProxyObject=83947136   # from enum ObjectTypeEnum
	kAngularGeneralDimensionObject=117474816  # from enum ObjectTypeEnum
	kAngularModelDimensionDefinitionObject=84025600   # from enum ObjectTypeEnum
	kAngularModelDimensionObject  =84022784   # from enum ObjectTypeEnum
	kAngularModelDimensionProxyObject=84022896   # from enum ObjectTypeEnum
	kAngularModelDimensionsObject =84022016   # from enum ObjectTypeEnum
	kAnnotationPlaneDefinitionObject=84029696   # from enum ObjectTypeEnum
	kAnnotationPlaneDefinitionsEnumeratorObject=84029952   # from enum ObjectTypeEnum
	kAnnotationPlaneObject        =84027904   # from enum ObjectTypeEnum
	kAnnotationPlaneProxyObject   =84028016   # from enum ObjectTypeEnum
	kAnnotationPlanesObject       =84027648   # from enum ObjectTypeEnum
	kApplicationAddInObject       =50336000   # from enum ObjectTypeEnum
	kApplicationAddInSiteObject   =50336768   # from enum ObjectTypeEnum
	kApplicationAddInsObject      =50335744   # from enum ObjectTypeEnum
	kApplicationEventsObject      =50333184   # from enum ObjectTypeEnum
	kApplicationObject            =50331904   # from enum ObjectTypeEnum
	kApprenticeDrawingPrintManagerObject=50391040   # from enum ObjectTypeEnum
	kApprenticePrintManagerObject =50390784   # from enum ObjectTypeEnum
	kApprenticeServerDocumentObject=50340736   # from enum ObjectTypeEnum
	kApprenticeServerDocumentsObject=50340864   # from enum ObjectTypeEnum
	kApprenticeServerDrawingDocumentObject=117441024  # from enum ObjectTypeEnum
	kApprenticeServerObject       =50341120   # from enum ObjectTypeEnum
	kArcLengthDimConstraintObject =84014336   # from enum ObjectTypeEnum
	kArcLengthDimConstraintProxyObject=84014448   # from enum ObjectTypeEnum
	kAssemblyComponentDefinitionObject=100663808  # from enum ObjectTypeEnum
	kAssemblyComponentDefinitionsObject=100664576  # from enum ObjectTypeEnum
	kAssemblyConstraintsEnumeratorObject=100664832  # from enum ObjectTypeEnum
	kAssemblyConstraintsObject    =100664320  # from enum ObjectTypeEnum
	kAssemblyEventsObject         =100667392  # from enum ObjectTypeEnum
	kAssemblyJointDefinitionObject=100706304  # from enum ObjectTypeEnum
	kAssemblyJointObject          =100706560  # from enum ObjectTypeEnum
	kAssemblyJointProxyObject     =100707072  # from enum ObjectTypeEnum
	kAssemblyJointsEnumeratorObject=100707584  # from enum ObjectTypeEnum
	kAssemblyJointsObject         =100706048  # from enum ObjectTypeEnum
	kAssemblyOptionsObject        =50386176   # from enum ObjectTypeEnum
	kAssemblySolverNodeObject     =100671488  # from enum ObjectTypeEnum
	kAssemblySolverObject         =100671232  # from enum ObjectTypeEnum
	kAssemblySymmetryConstraintObject=100707840  # from enum ObjectTypeEnum
	kAssemblySymmetryConstraintProxyObject=100708096  # from enum ObjectTypeEnum
	kAssemblyWorkAxisDefObject    =100670720  # from enum ObjectTypeEnum
	kAssemblyWorkPlaneDefObject   =100670464  # from enum ObjectTypeEnum
	kAssemblyWorkPointDefObject   =100670976  # from enum ObjectTypeEnum
	kAssetCategoriesObject        =50449152   # from enum ObjectTypeEnum
	kAssetCategoryObject          =50449408   # from enum ObjectTypeEnum
	kAssetLibrariesObject         =50447616   # from enum ObjectTypeEnum
	kAssetLibraryObject           =50447872   # from enum ObjectTypeEnum
	kAssetObject                  =50448640   # from enum ObjectTypeEnum
	kAssetTextureObject           =50452480   # from enum ObjectTypeEnum
	kAssetValueObject             =50449664   # from enum ObjectTypeEnum
	kAssetsEnumeratorObject       =50448384   # from enum ObjectTypeEnum
	kAssetsObject                 =50448128   # from enum ObjectTypeEnum
	kAttributeManagerObject       =50351872   # from enum ObjectTypeEnum
	kAttributeObject              =50352640   # from enum ObjectTypeEnum
	kAttributeSetObject           =50352384   # from enum ObjectTypeEnum
	kAttributeSetsEnumeratorObject=50361344   # from enum ObjectTypeEnum
	kAttributeSetsObject          =50352128   # from enum ObjectTypeEnum
	kAttributesEnumeratorObject   =50361600   # from enum ObjectTypeEnum
	kAutoCADBlockDefinitionObject =117495296  # from enum ObjectTypeEnum
	kAutoCADBlockDefinitionsEnumeratorObject=117496064  # from enum ObjectTypeEnum
	kAutoCADBlockDefinitionsObject=117495040  # from enum ObjectTypeEnum
	kAutoCADBlockObject           =117495808  # from enum ObjectTypeEnum
	kAutoCADBlocksObject          =117495552  # from enum ObjectTypeEnum
	kAutomatedCenterlineSettingsObject=117489920  # from enum ObjectTypeEnum
	kBIMCableTrayConnectorDefinitionObject=50440448   # from enum ObjectTypeEnum
	kBIMComponentDescriptionObject=50437376   # from enum ObjectTypeEnum
	kBIMComponentObject           =50436864   # from enum ObjectTypeEnum
	kBIMComponentPropertyObject   =50438656   # from enum ObjectTypeEnum
	kBIMComponentPropertySetObject=50438400   # from enum ObjectTypeEnum
	kBIMComponentPropertySetsObject=50438144   # from enum ObjectTypeEnum
	kBIMConduitConnectorDefinitionObject=50440192   # from enum ObjectTypeEnum
	kBIMConnectorDefinitionObject =50439168   # from enum ObjectTypeEnum
	kBIMConnectorLinkObject       =50438032   # from enum ObjectTypeEnum
	kBIMConnectorLinksObject      =50437888   # from enum ObjectTypeEnum
	kBIMConnectorObject           =50438912   # from enum ObjectTypeEnum
	kBIMConnectorsObject          =50437632   # from enum ObjectTypeEnum
	kBIMDuctConnectorDefinitionObject=50439936   # from enum ObjectTypeEnum
	kBIMElectricalConnectorDefinitionObject=50439680   # from enum ObjectTypeEnum
	kBIMExchangeServerObject      =50437120   # from enum ObjectTypeEnum
	kBIMPipeConnectorDefinitionObject=50439424   # from enum ObjectTypeEnum
	kBOMObject                    =100673792  # from enum ObjectTypeEnum
	kBOMQuantityObject            =67131136   # from enum ObjectTypeEnum
	kBOMRowObject                 =100674816  # from enum ObjectTypeEnum
	kBOMRowsEnumeratorObject      =100681984  # from enum ObjectTypeEnum
	kBOMViewObject                =100674304  # from enum ObjectTypeEnum
	kBOMViewsObject               =100674048  # from enum ObjectTypeEnum
	kBSplineCurve2dDefinitionObject=67130880   # from enum ObjectTypeEnum
	kBSplineCurveDefinitionObject =67130624   # from enum ObjectTypeEnum
	kBalloonObject                =117463040  # from enum ObjectTypeEnum
	kBalloonStyleObject           =117480960  # from enum ObjectTypeEnum
	kBalloonStylesEnumeratorObject=117480704  # from enum ObjectTypeEnum
	kBalloonTipObject             =50441728   # from enum ObjectTypeEnum
	kBalloonTipsObject            =50441472   # from enum ObjectTypeEnum
	kBalloonValueSetObject        =117463808  # from enum ObjectTypeEnum
	kBalloonValueSetsObject       =117463552  # from enum ObjectTypeEnum
	kBalloonsObject               =117462784  # from enum ObjectTypeEnum
	kBaselineDimensionSetObject   =117488896  # from enum ObjectTypeEnum
	kBaselineDimensionSetsObject  =117488640  # from enum ObjectTypeEnum
	kBendConstraintObject         =83941888   # from enum ObjectTypeEnum
	kBendConstraintProxyObject    =83942000   # from enum ObjectTypeEnum
	kBendDefinitionObject         =151006976  # from enum ObjectTypeEnum
	kBendFeatureObject            =150997504  # from enum ObjectTypeEnum
	kBendFeatureProxyObject       =151003136  # from enum ObjectTypeEnum
	kBendFeaturesObject           =150997248  # from enum ObjectTypeEnum
	kBendNoteObject               =117487616  # from enum ObjectTypeEnum
	kBendNotesObject              =117490944  # from enum ObjectTypeEnum
	kBendObject                   =151019520  # from enum ObjectTypeEnum
	kBendOptionsObject            =151009792  # from enum ObjectTypeEnum
	kBendPartFeatureObject        =83991552   # from enum ObjectTypeEnum
	kBendPartFeatureProxyObject   =83991680   # from enum ObjectTypeEnum
	kBendPartFeaturesObject       =83991808   # from enum ObjectTypeEnum
	kBendsEnumeratorObject        =151019776  # from enum ObjectTypeEnum
	kBooleanAssetValueObject      =50450944   # from enum ObjectTypeEnum
	kBorderDefinitionObject       =117446400  # from enum ObjectTypeEnum
	kBorderDefinitionsObject      =117446144  # from enum ObjectTypeEnum
	kBorderObject                 =117446656  # from enum ObjectTypeEnum
	kBossFeatureObject            =84002304   # from enum ObjectTypeEnum
	kBossFeatureProxyObject       =84002416   # from enum ObjectTypeEnum
	kBossFeaturesObject           =84002560   # from enum ObjectTypeEnum
	kBossSetObject                =84013824   # from enum ObjectTypeEnum
	kBossSetsObject               =84013568   # from enum ObjectTypeEnum
	kBoundaryPatchDefinitionObject=83989760   # from enum ObjectTypeEnum
	kBoundaryPatchFeatureObject   =83964672   # from enum ObjectTypeEnum
	kBoundaryPatchFeatureProxyObject=83965184   # from enum ObjectTypeEnum
	kBoundaryPatchFeaturesObject  =83964928   # from enum ObjectTypeEnum
	kBoundaryPatchLoopObject      =83990016   # from enum ObjectTypeEnum
	kBoundaryPatchLoopsObject     =83992832   # from enum ObjectTypeEnum
	kBreakOperationObject         =117492224  # from enum ObjectTypeEnum
	kBreakOperationsObject        =117491968  # from enum ObjectTypeEnum
	kBreakOutOperationObject      =117492736  # from enum ObjectTypeEnum
	kBreakOutOperationsObject     =117492480  # from enum ObjectTypeEnum
	kBrowserFolderObject          =50427392   # from enum ObjectTypeEnum
	kBrowserFoldersEnumeratorObject=50426880   # from enum ObjectTypeEnum
	kBrowserNodeDefinitionObject  =50384896   # from enum ObjectTypeEnum
	kBrowserNodeObject            =50384384   # from enum ObjectTypeEnum
	kBrowserNodesEnumeratorObject =50384128   # from enum ObjectTypeEnum
	kBrowserPaneObject            =50363136   # from enum ObjectTypeEnum
	kBrowserPanesObject           =50362880   # from enum ObjectTypeEnum
	kButtonDefinitionHandlerObject=50374144   # from enum ObjectTypeEnum
	kButtonDefinitionObject       =50371584   # from enum ObjectTypeEnum
	kCallOutSymbolObject          =117473280  # from enum ObjectTypeEnum
	kCameraEventsObject           =50435328   # from enum ObjectTypeEnum
	kCameraObject                 =50345472   # from enum ObjectTypeEnum
	kCategoryManagerObject        =50409984   # from enum ObjectTypeEnum
	kCellObject                   =117462528  # from enum ObjectTypeEnum
	kCenteredWidthExtentObject    =83996672   # from enum ObjectTypeEnum
	kCenterlineObject             =117479680  # from enum ObjectTypeEnum
	kCenterlinesObject            =117479424  # from enum ObjectTypeEnum
	kCentermarkObject             =117479168  # from enum ObjectTypeEnum
	kCentermarkStyleObject        =117490432  # from enum ObjectTypeEnum
	kCentermarkStylesEnumeratorObject=117490176  # from enum ObjectTypeEnum
	kCentermarksObject            =117478912  # from enum ObjectTypeEnum
	kCentroidWorkPointDefObject   =83993088   # from enum ObjectTypeEnum
	kChainDimensionSetObject      =117493248  # from enum ObjectTypeEnum
	kChainDimensionSetsObject     =117492992  # from enum ObjectTypeEnum
	kChamferFeatureObject         =83909120   # from enum ObjectTypeEnum
	kChamferFeatureProxyObject    =83956480   # from enum ObjectTypeEnum
	kChamferFeaturesObject        =83909376   # from enum ObjectTypeEnum
	kChamferNoteObject            =117488384  # from enum ObjectTypeEnum
	kChamferNotesObject           =117490688  # from enum ObjectTypeEnum
	kChangeDefinitionObject       =50389248   # from enum ObjectTypeEnum
	kChangeDefinitionsObject      =50388992   # from enum ObjectTypeEnum
	kChangeManagerObject          =50388736   # from enum ObjectTypeEnum
	kChangeProcessorObject        =50389504   # from enum ObjectTypeEnum
	kCheckPointObject             =50354432   # from enum ObjectTypeEnum
	kCheckPointsEnumeratorObject  =50354688   # from enum ObjectTypeEnum
	kChoiceAssetValueObject       =50449920   # from enum ObjectTypeEnum
	kCircularOccurrencePatternObject=100669696  # from enum ObjectTypeEnum
	kCircularOccurrencePatternProxyObject=100669824  # from enum ObjectTypeEnum
	kCircularPatternFeatureDefinitionObject=84058880   # from enum ObjectTypeEnum
	kCircularPatternFeatureObject =83909632   # from enum ObjectTypeEnum
	kCircularPatternFeatureProxyObject=83956736   # from enum ObjectTypeEnum
	kCircularPatternFeaturesObject=83909888   # from enum ObjectTypeEnum
	kClientBrowserNodeDefinitionObject=50385152   # from enum ObjectTypeEnum
	kClientFeatureDefinitionObject=83988992   # from enum ObjectTypeEnum
	kClientFeatureElementObject   =83989504   # from enum ObjectTypeEnum
	kClientFeatureElementProxyObject=83989616   # from enum ObjectTypeEnum
	kClientFeatureElementsObject  =83989248   # from enum ObjectTypeEnum
	kClientFeatureObject          =83988736   # from enum ObjectTypeEnum
	kClientFeatureProxyObject     =83988848   # from enum ObjectTypeEnum
	kClientFeaturesObject         =83988480   # from enum ObjectTypeEnum
	kClientGraphicsCollectionObject=50356224   # from enum ObjectTypeEnum
	kClientGraphicsObject         =50356480   # from enum ObjectTypeEnum
	kClientNodeResourceObject     =50385664   # from enum ObjectTypeEnum
	kClientNodeResourcesObject    =50385920   # from enum ObjectTypeEnum
	kClientViewObject             =50368256   # from enum ObjectTypeEnum
	kClientViewsObject            =50368000   # from enum ObjectTypeEnum
	kCoilFeatureObject            =83910144   # from enum ObjectTypeEnum
	kCoilFeatureProxyObject       =83956992   # from enum ObjectTypeEnum
	kCoilFeaturesObject           =83910400   # from enum ObjectTypeEnum
	kCoincidentConstraint3DObject =83942144   # from enum ObjectTypeEnum
	kCoincidentConstraint3DProxyObject=83942256   # from enum ObjectTypeEnum
	kCoincidentConstraintObject   =83900160   # from enum ObjectTypeEnum
	kCoincidentConstraintProxyObject=83900272   # from enum ObjectTypeEnum
	kCollinearConstraint3DObject  =83966208   # from enum ObjectTypeEnum
	kCollinearConstraint3DProxyObject=83966320   # from enum ObjectTypeEnum
	kCollinearConstraintObject    =83900416   # from enum ObjectTypeEnum
	kCollinearConstraintProxyObject=83900528   # from enum ObjectTypeEnum
	kColorAssetValueObject        =50451200   # from enum ObjectTypeEnum
	kColorObject                  =50383104   # from enum ObjectTypeEnum
	kColorSchemeObject            =50399232   # from enum ObjectTypeEnum
	kColorSchemesObject           =50398976   # from enum ObjectTypeEnum
	kColumnObject                 =117461760  # from enum ObjectTypeEnum
	kColumnsObject                =117461504  # from enum ObjectTypeEnum
	kCombineFeatureObject         =84001536   # from enum ObjectTypeEnum
	kCombineFeatureProxyObject    =84001696   # from enum ObjectTypeEnum
	kCombineFeaturesObject        =84001280   # from enum ObjectTypeEnum
	kComboBoxDefinitionObject     =50372096   # from enum ObjectTypeEnum
	kCommandBarBaseCollectionObject=50375424   # from enum ObjectTypeEnum
	kCommandBarBaseObject         =50375680   # from enum ObjectTypeEnum
	kCommandBarButtonObject       =50365952   # from enum ObjectTypeEnum
	kCommandBarControlObject      =50365440   # from enum ObjectTypeEnum
	kCommandBarControlsObject     =50365184   # from enum ObjectTypeEnum
	kCommandBarListObject         =50376704   # from enum ObjectTypeEnum
	kCommandBarObject             =50364928   # from enum ObjectTypeEnum
	kCommandBarPopUpObject        =50365696   # from enum ObjectTypeEnum
	kCommandBarsObject            =50364672   # from enum ObjectTypeEnum
	kCommandCategoriesObject      =50370816   # from enum ObjectTypeEnum
	kCommandCategoryObject        =50370560   # from enum ObjectTypeEnum
	kCommandControlObject         =50425856   # from enum ObjectTypeEnum
	kCommandControlsEnumeratorObject=50426624   # from enum ObjectTypeEnum
	kCommandControlsObject        =50425600   # from enum ObjectTypeEnum
	kCommandManagerObject         =50344704   # from enum ObjectTypeEnum
	kCommandObject                =50344192   # from enum ObjectTypeEnum
	kComponentDefinitionObject    =67113264   # from enum ObjectTypeEnum
	kComponentDefinitionReferenceObject=67113520   # from enum ObjectTypeEnum
	kComponentDefinitionReferencesObject=67114800   # from enum ObjectTypeEnum
	kComponentDefinitionsEnumeratorObject=67114336   # from enum ObjectTypeEnum
	kComponentDefinitionsObject   =67114288   # from enum ObjectTypeEnum
	kComponentGraphicsObject      =50436608   # from enum ObjectTypeEnum
	kComponentOccurrenceObject    =67113776   # from enum ObjectTypeEnum
	kComponentOccurrenceProxyObject=67113888   # from enum ObjectTypeEnum
	kComponentOccurrencesEnumeratorObject=67126528   # from enum ObjectTypeEnum
	kComponentOccurrencesObject   =67114544   # from enum ObjectTypeEnum
	kCompositeConstraintObject    =100678144  # from enum ObjectTypeEnum
	kCompositeiMateDefinitionObject=83948800   # from enum ObjectTypeEnum
	kCompositeiMateDefinitionProxyObject=83948864   # from enum ObjectTypeEnum
	kConcentricConstraint3DObject =84008960   # from enum ObjectTypeEnum
	kConcentricConstraint3DProxyObject=84009072   # from enum ObjectTypeEnum
	kConcentricConstraintObject   =83900672   # from enum ObjectTypeEnum
	kConcentricConstraintProxyObject=83900784   # from enum ObjectTypeEnum
	kConcentricHolePlacementDefinitionObject=83967232   # from enum ObjectTypeEnum
	kConstraintLimitsObject       =100699904  # from enum ObjectTypeEnum
	kContentCenterConfigurationObject=50400256   # from enum ObjectTypeEnum
	kContentCenterDialogEventsObject=50409472   # from enum ObjectTypeEnum
	kContentCenterDialogObject    =50409216   # from enum ObjectTypeEnum
	kContentCenterEventsObject    =50420224   # from enum ObjectTypeEnum
	kContentCenterObject          =50392320   # from enum ObjectTypeEnum
	kContentCenterOptionsObject   =50421248   # from enum ObjectTypeEnum
	kContentFamiliesEnumeratorObject=50423296   # from enum ObjectTypeEnum
	kContentFamilyObject          =50421760   # from enum ObjectTypeEnum
	kContentQueryObject           =50393088   # from enum ObjectTypeEnum
	kContentTableCellObject       =50421504   # from enum ObjectTypeEnum
	kContentTableColumnObject     =50422528   # from enum ObjectTypeEnum
	kContentTableColumnsObject    =50423040   # from enum ObjectTypeEnum
	kContentTableRowObject        =50422016   # from enum ObjectTypeEnum
	kContentTableRowsObject       =50422272   # from enum ObjectTypeEnum
	kContentTreeViewNodeObject    =50423808   # from enum ObjectTypeEnum
	kContentTreeViewNodesEnumeratorObject=50423552   # from enum ObjectTypeEnum
	kContourFlangeDefinitionObject=151014144  # from enum ObjectTypeEnum
	kContourFlangeFeatureObject   =151001856  # from enum ObjectTypeEnum
	kContourFlangeFeatureProxyObject=151005184  # from enum ObjectTypeEnum
	kContourFlangeFeaturesObject  =151001600  # from enum ObjectTypeEnum
	kContourRollFeatureObject     =151020800  # from enum ObjectTypeEnum
	kContourRollFeatureProxyObject=151021056  # from enum ObjectTypeEnum
	kContourRollFeaturesObject    =151021312  # from enum ObjectTypeEnum
	kControlDefinitionEventsObject=50390016   # from enum ObjectTypeEnum
	kControlDefinitionsObject     =50371328   # from enum ObjectTypeEnum
	kCoreCavityDefinitionObject   =84009728   # from enum ObjectTypeEnum
	kCoreCavityFeatureObject      =84010240   # from enum ObjectTypeEnum
	kCoreCavityFeatureProxyObject =84009984   # from enum ObjectTypeEnum
	kCoreCavityFeaturesObject     =84010496   # from enum ObjectTypeEnum
	kCornerChamferDefinitionObject=151011584  # from enum ObjectTypeEnum
	kCornerChamferFeatureObject   =151000320  # from enum ObjectTypeEnum
	kCornerChamferFeatureProxyObject=151004416  # from enum ObjectTypeEnum
	kCornerChamferFeaturesObject  =151000064  # from enum ObjectTypeEnum
	kCornerDefinitionObject       =151010816  # from enum ObjectTypeEnum
	kCornerFeatureObject          =150996992  # from enum ObjectTypeEnum
	kCornerFeatureProxyObject     =151002880  # from enum ObjectTypeEnum
	kCornerFeaturesObject         =150996736  # from enum ObjectTypeEnum
	kCornerOptionsObject          =151010048  # from enum ObjectTypeEnum
	kCornerRoundDefinitionObject  =151011072  # from enum ObjectTypeEnum
	kCornerRoundEdgeSetObject     =151011328  # from enum ObjectTypeEnum
	kCornerRoundFeatureObject     =150999808  # from enum ObjectTypeEnum
	kCornerRoundFeatureProxyObject=151004160  # from enum ObjectTypeEnum
	kCornerRoundFeaturesObject    =150999552  # from enum ObjectTypeEnum
	kCosmeticBendFeatureObject    =151021824  # from enum ObjectTypeEnum
	kCosmeticBendFeatureProxyObject=151022080  # from enum ObjectTypeEnum
	kCosmeticBendFeaturesObject   =151022336  # from enum ObjectTypeEnum
	kCosmeticWeldDefinitionObject =100708352  # from enum ObjectTypeEnum
	kCosmeticWeldObject           =100673024  # from enum ObjectTypeEnum
	kCosmeticWeldsObject          =100672256  # from enum ObjectTypeEnum
	kCurveAndEntityWorkPointDefObject=83952128   # from enum ObjectTypeEnum
	kCurveGraphicsObject          =50414848   # from enum ObjectTypeEnum
	kCustomConstraint3DObject     =83973120   # from enum ObjectTypeEnum
	kCustomConstraint3DProxyObject=83973232   # from enum ObjectTypeEnum
	kCustomConstraintObject       =100673536  # from enum ObjectTypeEnum
	kCustomConstraintProxyObject  =100677632  # from enum ObjectTypeEnum
	kCustomDataEventsObject       =50462720   # from enum ObjectTypeEnum
	kCustomDictionariesObject     =50463744   # from enum ObjectTypeEnum
	kCustomDictionaryObject       =50463488   # from enum ObjectTypeEnum
	kCustomParameterGroupObject   =50401536   # from enum ObjectTypeEnum
	kCustomParameterGroupsObject  =50398464   # from enum ObjectTypeEnum
	kCustomPropertyFormat         =50430720   # from enum ObjectTypeEnum
	kCustomTableObject            =117461248  # from enum ObjectTypeEnum
	kCustomTablesObject           =117460992  # from enum ObjectTypeEnum
	kCutAcrossBendsExtentObject   =83993344   # from enum ObjectTypeEnum
	kCutDefinitionObject          =151010304  # from enum ObjectTypeEnum
	kCutFeatureObject             =150998016  # from enum ObjectTypeEnum
	kCutFeatureProxyObject        =151003392  # from enum ObjectTypeEnum
	kCutFeaturesObject            =150997760  # from enum ObjectTypeEnum
	kDSDegreeOfFreedomObject      =100703744  # from enum ObjectTypeEnum
	kDSDegreesOfFreedomObject     =100703488  # from enum ObjectTypeEnum
	kDSJointDefinitionObject      =100703232  # from enum ObjectTypeEnum
	kDSJointObject                =100701184  # from enum ObjectTypeEnum
	kDSJointsObject               =100700928  # from enum ObjectTypeEnum
	kDSLoadDefinitionObject       =100702464  # from enum ObjectTypeEnum
	kDSLoadObject                 =100702208  # from enum ObjectTypeEnum
	kDSLoadsObject                =100701952  # from enum ObjectTypeEnum
	kDSResultObject               =100704256  # from enum ObjectTypeEnum
	kDSResultsObject              =100704000  # from enum ObjectTypeEnum
	kDSSettingsObject             =100704512  # from enum ObjectTypeEnum
	kDSValueGraphObject           =100702976  # from enum ObjectTypeEnum
	kDSValueObject                =100702720  # from enum ObjectTypeEnum
	kDWGACMStandardPartObject     =84057600   # from enum ObjectTypeEnum
	kDWGACMStandardPartProxyObject=84057856   # from enum ObjectTypeEnum
	kDWGACMStandardPartsEnumeratorObject=84058112   # from enum ObjectTypeEnum
	kDWGAcadSupportedProxiesEnumeratorObject=84068864   # from enum ObjectTypeEnum
	kDWGAcadSupportedProxyObject  =84065792   # from enum ObjectTypeEnum
	kDWGAcadSupportedProxyProxyObject=84066048   # from enum ObjectTypeEnum
	kDWGArcObject                 =84041472   # from enum ObjectTypeEnum
	kDWGArcProxyObject            =84041728   # from enum ObjectTypeEnum
	kDWGArcsEnumeratorObject      =84041216   # from enum ObjectTypeEnum
	kDWGBlockDefinitionObject     =84040704   # from enum ObjectTypeEnum
	kDWGBlockDefinitionProxyObject=84040960   # from enum ObjectTypeEnum
	kDWGBlockReferenceObject      =84040192   # from enum ObjectTypeEnum
	kDWGBlockReferenceProxyObject =84040448   # from enum ObjectTypeEnum
	kDWGBlockReferencesEnumeratorObject=84039936   # from enum ObjectTypeEnum
	kDWGEllipticalArcObject       =84042240   # from enum ObjectTypeEnum
	kDWGEllipticalArcProxyObject  =84042496   # from enum ObjectTypeEnum
	kDWGEllipticalArcsEnumeratorObject=84041984   # from enum ObjectTypeEnum
	kDWGEntitiesEnumeratorObject  =84039168   # from enum ObjectTypeEnum
	kDWGEntityArcSegmentObject    =84070400   # from enum ObjectTypeEnum
	kDWGEntityArcSegmentProxyObject=84070656   # from enum ObjectTypeEnum
	kDWGEntityEllipticalArcSegmentObject=84070912   # from enum ObjectTypeEnum
	kDWGEntityEllipticalArcSegmentProxyObject=84071168   # from enum ObjectTypeEnum
	kDWGEntityLineSegmentObject   =84069888   # from enum ObjectTypeEnum
	kDWGEntityLineSegmentProxyObject=84070144   # from enum ObjectTypeEnum
	kDWGEntityObject              =84039424   # from enum ObjectTypeEnum
	kDWGEntityProxyObject         =84039680   # from enum ObjectTypeEnum
	kDWGEntitySegmentObject       =84069376   # from enum ObjectTypeEnum
	kDWGEntitySegmentProxyObject  =84069632   # from enum ObjectTypeEnum
	kDWGEntitySegmentsEnumeratorObject=84069120   # from enum ObjectTypeEnum
	kDWGEntitySplineSegmentObject =84071424   # from enum ObjectTypeEnum
	kDWGEntitySplineSegmentProxyObject=84071680   # from enum ObjectTypeEnum
	kDWGLineObject                =84043008   # from enum ObjectTypeEnum
	kDWGLineProxyObject           =84043264   # from enum ObjectTypeEnum
	kDWGLinesEnumeratorObject     =84042752   # from enum ObjectTypeEnum
	kDWGPointObject               =84043776   # from enum ObjectTypeEnum
	kDWGPointProxyObject          =84044032   # from enum ObjectTypeEnum
	kDWGPointsEnumeratorObject    =84043520   # from enum ObjectTypeEnum
	kDWGPolyline2DObject          =84046080   # from enum ObjectTypeEnum
	kDWGPolyline2DProxyObject     =84048128   # from enum ObjectTypeEnum
	kDWGPolyline3DObject          =84048640   # from enum ObjectTypeEnum
	kDWGPolyline3DProxyObject     =84048896   # from enum ObjectTypeEnum
	kDWGPolylineObject            =84044544   # from enum ObjectTypeEnum
	kDWGPolylineProxyObject       =84044800   # from enum ObjectTypeEnum
	kDWGPolylines2DEnumeratorObject=84045824   # from enum ObjectTypeEnum
	kDWGPolylines3DEnumeratorObject=84048384   # from enum ObjectTypeEnum
	kDWGPolylinesEnumeratorObject =84044288   # from enum ObjectTypeEnum
	kDWGSplineObject              =84045312   # from enum ObjectTypeEnum
	kDWGSplineProxyObject         =84045568   # from enum ObjectTypeEnum
	kDWGSplinesEnumeratorObject   =84045056   # from enum ObjectTypeEnum
	kDecalFeatureObject           =83952640   # from enum ObjectTypeEnum
	kDecalFeatureProxyObject      =83957248   # from enum ObjectTypeEnum
	kDecalFeaturesObject          =83952896   # from enum ObjectTypeEnum
	kDefaultBorderObject          =117449728  # from enum ObjectTypeEnum
	kDeleteFaceFeatureObject      =83953152   # from enum ObjectTypeEnum
	kDeleteFaceFeatureProxyObject =83957504   # from enum ObjectTypeEnum
	kDeleteFaceFeaturesObject     =83953408   # from enum ObjectTypeEnum
	kDerivedAliasComponentObject  =84007936   # from enum ObjectTypeEnum
	kDerivedAliasComponentProxyObject=84007938   # from enum ObjectTypeEnum
	kDerivedAliasComponentsObject =84007680   # from enum ObjectTypeEnum
	kDerivedAssemblyComponentObject=83930368   # from enum ObjectTypeEnum
	kDerivedAssemblyComponentProxyObject=83930480   # from enum ObjectTypeEnum
	kDerivedAssemblyComponentsObject=83930112   # from enum ObjectTypeEnum
	kDerivedAssemblyDefinitionObject=83930624   # from enum ObjectTypeEnum
	kDerivedAssemblyOccurrenceObject=83931136   # from enum ObjectTypeEnum
	kDerivedAssemblyOccurrencesObject=83934464   # from enum ObjectTypeEnum
	kDerivedFutureAssemblyComponentObject=84064512   # from enum ObjectTypeEnum
	kDerivedFutureAssemblyComponentProxyObject=84064624   # from enum ObjectTypeEnum
	kDerivedFutureAssemblyComponentsObject=84064768   # from enum ObjectTypeEnum
	kDerivedFutureAssemblyDefinitionObject=84065024   # from enum ObjectTypeEnum
	kDerivedFutureAssemblyOccurrenceObject=84065536   # from enum ObjectTypeEnum
	kDerivedFutureAssemblyOccurrencesObject=84065280   # from enum ObjectTypeEnum
	kDerivedFuturePartComponentObject=84063744   # from enum ObjectTypeEnum
	kDerivedFuturePartComponentProxyObject=84063856   # from enum ObjectTypeEnum
	kDerivedFuturePartComponentsObject=84064000   # from enum ObjectTypeEnum
	kDerivedFuturePartDefinitionObject=84064256   # from enum ObjectTypeEnum
	kDerivedParameterObject       =50412544   # from enum ObjectTypeEnum
	kDerivedParameterTableObject  =50412032   # from enum ObjectTypeEnum
	kDerivedParameterTablesObject =50411776   # from enum ObjectTypeEnum
	kDerivedParametersObject      =50412288   # from enum ObjectTypeEnum
	kDerivedPartComponentObject   =83928832   # from enum ObjectTypeEnum
	kDerivedPartComponentProxyObject=83928944   # from enum ObjectTypeEnum
	kDerivedPartComponentsObject  =83928576   # from enum ObjectTypeEnum
	kDerivedPartCoordinateSystemDefObject=83951360   # from enum ObjectTypeEnum
	kDerivedPartDefinitionObject  =83929600   # from enum ObjectTypeEnum
	kDerivedPartEntitiesObject    =83929088   # from enum ObjectTypeEnum
	kDerivedPartEntityObject      =83929344   # from enum ObjectTypeEnum
	kDerivedPartTransformDefObject=83951104   # from enum ObjectTypeEnum
	kDerivedPartUniformScaleDefObject=83950848   # from enum ObjectTypeEnum
	kDesignProjectManagerObject   =50401024   # from enum ObjectTypeEnum
	kDesignProjectObject          =50379008   # from enum ObjectTypeEnum
	kDesignProjectsObject         =50401280   # from enum ObjectTypeEnum
	kDesignViewRepresentationObject=100679424  # from enum ObjectTypeEnum
	kDesignViewRepresentationsObject=100679168  # from enum ObjectTypeEnum
	kDetailDrawingViewObject      =117474304  # from enum ObjectTypeEnum
	kDiameterDimConstraintObject  =83906560   # from enum ObjectTypeEnum
	kDiameterDimConstraintProxyObject=83906672   # from enum ObjectTypeEnum
	kDiameterGeneralDimensionObject=117475328  # from enum ObjectTypeEnum
	kDiameterModelDimensionDefinitionObject=84026112   # from enum ObjectTypeEnum
	kDiameterModelDimensionObject =84023296   # from enum ObjectTypeEnum
	kDiameterModelDimensionProxyObject=84023408   # from enum ObjectTypeEnum
	kDiameterModelDimensionsObject=84022528   # from enum ObjectTypeEnum
	kDimensionConstraints3DObject =83970560   # from enum ObjectTypeEnum
	kDimensionConstraintsObject   =83905280   # from enum ObjectTypeEnum
	kDimensionStyleObject         =117452800  # from enum ObjectTypeEnum
	kDimensionStylesEnumeratorObject=117453056  # from enum ObjectTypeEnum
	kDimensionTextObject          =117464320  # from enum ObjectTypeEnum
	kDirectEditDeleteOperationObject=84036096   # from enum ObjectTypeEnum
	kDirectEditDeleteOperationProxyObject=84036352   # from enum ObjectTypeEnum
	kDirectEditFeatureObject      =84033024   # from enum ObjectTypeEnum
	kDirectEditFeatureProxyObject =84033536   # from enum ObjectTypeEnum
	kDirectEditFeaturesObject     =84033280   # from enum ObjectTypeEnum
	kDirectEditMoveOperationObject=84034560   # from enum ObjectTypeEnum
	kDirectEditMoveOperationProxyObject=84034816   # from enum ObjectTypeEnum
	kDirectEditOperationObject    =84033792   # from enum ObjectTypeEnum
	kDirectEditOperationProxyObject=84034304   # from enum ObjectTypeEnum
	kDirectEditOperationsObject   =84034048   # from enum ObjectTypeEnum
	kDirectEditRotateOperationObject=84035584   # from enum ObjectTypeEnum
	kDirectEditRotateOperationProxyObject=84035840   # from enum ObjectTypeEnum
	kDirectEditScaleOperationObject=84049152   # from enum ObjectTypeEnum
	kDirectEditScaleOperationProxyObject=84049408   # from enum ObjectTypeEnum
	kDirectEditSizeOperationObject=84035072   # from enum ObjectTypeEnum
	kDirectEditSizeOperationProxyObject=84035328   # from enum ObjectTypeEnum
	kDirectionAndDistanceMoveDefinitionObject=84012032   # from enum ObjectTypeEnum
	kDisabledCommandListObject    =50391296   # from enum ObjectTypeEnum
	kDisplayOptionsObject         =50413312   # from enum ObjectTypeEnum
	kDisplaySettingsObject        =50435840   # from enum ObjectTypeEnum
	kDistanceAndAngleChamferDefObject=83925760   # from enum ObjectTypeEnum
	kDistanceChamferDefObject     =83925504   # from enum ObjectTypeEnum
	kDistanceExtentObject         =83917824   # from enum ObjectTypeEnum
	kDistanceFromFaceExtentObject =84072960   # from enum ObjectTypeEnum
	kDistanceHeightExtentObject   =83995648   # from enum ObjectTypeEnum
	kDockableWindowObject         =50433280   # from enum ObjectTypeEnum
	kDockableWindowsEventsObject  =50442240   # from enum ObjectTypeEnum
	kDockableWindowsObject        =50433024   # from enum ObjectTypeEnum
	kDocumentDescriptorObject     =50407936   # from enum ObjectTypeEnum
	kDocumentDescriptorsEnumeratorObject=50408192   # from enum ObjectTypeEnum
	kDocumentEventsObject         =50333440   # from enum ObjectTypeEnum
	kDocumentInterestObject       =50415616   # from enum ObjectTypeEnum
	kDocumentInterestsObject      =50415360   # from enum ObjectTypeEnum
	kDocumentObject               =50332160   # from enum ObjectTypeEnum
	kDocumentSubTypeObject        =50378496   # from enum ObjectTypeEnum
	kDocumentsEnumeratorObject    =50349824   # from enum ObjectTypeEnum
	kDocumentsObject              =50332416   # from enum ObjectTypeEnum
	kDoubleHemDefinitionObject    =151015424  # from enum ObjectTypeEnum
	kDraftAnalysesObject          =50416640   # from enum ObjectTypeEnum
	kDraftAnalysisObject          =50416896   # from enum ObjectTypeEnum
	kDraftingStandardObject       =117441792  # from enum ObjectTypeEnum
	kDragContextObject            =50440704   # from enum ObjectTypeEnum
	kDrawingBOMCellObject         =117487104  # from enum ObjectTypeEnum
	kDrawingBOMColumnObject       =117486336  # from enum ObjectTypeEnum
	kDrawingBOMColumnsObject      =117486080  # from enum ObjectTypeEnum
	kDrawingBOMObject             =117485824  # from enum ObjectTypeEnum
	kDrawingBOMRowObject          =117486848  # from enum ObjectTypeEnum
	kDrawingBOMRowsObject         =117486592  # from enum ObjectTypeEnum
	kDrawingBOMsObject            =117485568  # from enum ObjectTypeEnum
	kDrawingCurveObject           =117473792  # from enum ObjectTypeEnum
	kDrawingCurveSegmentObject    =117478144  # from enum ObjectTypeEnum
	kDrawingCurveSegmentsObject   =117477888  # from enum ObjectTypeEnum
	kDrawingCurvesEnumeratorObject=117473536  # from enum ObjectTypeEnum
	kDrawingDimensionObject       =117454848  # from enum ObjectTypeEnum
	kDrawingDimensionsObject      =117454592  # from enum ObjectTypeEnum
	kDrawingEventsObject          =117464832  # from enum ObjectTypeEnum
	kDrawingNoteObject            =117472000  # from enum ObjectTypeEnum
	kDrawingNotesObject           =117471744  # from enum ObjectTypeEnum
	kDrawingOptionsObject         =50415104   # from enum ObjectTypeEnum
	kDrawingPrintManagerObject    =50351616   # from enum ObjectTypeEnum
	kDrawingSettingsObject        =117449984  # from enum ObjectTypeEnum
	kDrawingSketchObject          =117443328  # from enum ObjectTypeEnum
	kDrawingSketchesObject        =117443584  # from enum ObjectTypeEnum
	kDrawingStandardStyleObject   =117454080  # from enum ObjectTypeEnum
	kDrawingStandardStylesEnumeratorObject=117453824  # from enum ObjectTypeEnum
	kDrawingStylesManagerObject   =117453568  # from enum ObjectTypeEnum
	kDrawingViewEventsObject      =117450496  # from enum ObjectTypeEnum
	kDrawingViewLabelObject       =117479936  # from enum ObjectTypeEnum
	kDrawingViewObject            =117441536  # from enum ObjectTypeEnum
	kDrawingViewsObject           =117442304  # from enum ObjectTypeEnum
	kDriveConstraintSettingsObject=100700160  # from enum ObjectTypeEnum
	kDriveSettingsObject          =100706816  # from enum ObjectTypeEnum
	kDynamicSimulationObject      =100700416  # from enum ObjectTypeEnum
	kDynamicSimulationsObject     =100701696  # from enum ObjectTypeEnum
	kEdgeCollectionObject         =28928      # from enum ObjectTypeEnum
	kEdgeDefinitionObject         =50429952   # from enum ObjectTypeEnum
	kEdgeDefinitionsObject        =50429696   # from enum ObjectTypeEnum
	kEdgeLoopDefinitionObject     =50428928   # from enum ObjectTypeEnum
	kEdgeLoopDefinitionsObject    =50428672   # from enum ObjectTypeEnum
	kEdgeLoopObject               =67119664   # from enum ObjectTypeEnum
	kEdgeLoopProxyObject          =67119712   # from enum ObjectTypeEnum
	kEdgeLoopsObject              =67122224   # from enum ObjectTypeEnum
	kEdgeObject                   =67120176   # from enum ObjectTypeEnum
	kEdgeProxyObject              =67120288   # from enum ObjectTypeEnum
	kEdgeUseDefinitionObject      =50429440   # from enum ObjectTypeEnum
	kEdgeUseDefinitionsObject     =50429184   # from enum ObjectTypeEnum
	kEdgeUseObject                =67119920   # from enum ObjectTypeEnum
	kEdgeUseProxyObject           =67120032   # from enum ObjectTypeEnum
	kEdgeUsesObject               =67122480   # from enum ObjectTypeEnum
	kEdgeWidthExtentObject        =83996416   # from enum ObjectTypeEnum
	kEdgesObject                  =1073963056 # from enum ObjectTypeEnum
	kEllipseRadiusDimConstraintObject=83924224   # from enum ObjectTypeEnum
	kEllipseRadiusDimConstraintProxyObject=83924336   # from enum ObjectTypeEnum
	kEmbossFeatureObject          =83953664   # from enum ObjectTypeEnum
	kEmbossFeatureProxyObject     =83957760   # from enum ObjectTypeEnum
	kEmbossFeaturesObject         =83953920   # from enum ObjectTypeEnum
	kEndOfFeaturesObject          =83969536   # from enum ObjectTypeEnum
	kEnvironmentBaseCollectionObject=50375936   # from enum ObjectTypeEnum
	kEnvironmentBaseHandlerObject =50374912   # from enum ObjectTypeEnum
	kEnvironmentBaseObject        =50376192   # from enum ObjectTypeEnum
	kEnvironmentListObject        =50390528   # from enum ObjectTypeEnum
	kEnvironmentManagerObject     =50391552   # from enum ObjectTypeEnum
	kEnvironmentObject            =50363904   # from enum ObjectTypeEnum
	kEnvironmentsObject           =50363648   # from enum ObjectTypeEnum
	kEqualConstraint3DObject      =84055808   # from enum ObjectTypeEnum
	kEqualConstraint3DProxyObject =84055920   # from enum ObjectTypeEnum
	kEqualLengthConstraintObject  =83901440   # from enum ObjectTypeEnum
	kEqualLengthConstraintProxyObject=83901552   # from enum ObjectTypeEnum
	kEqualRadiusConstraintObject  =83901696   # from enum ObjectTypeEnum
	kEqualRadiusConstraintProxyObject=83901808   # from enum ObjectTypeEnum
	kErrorManagerObject           =50420736   # from enum ObjectTypeEnum
	kExplodedViewObject           =134218752  # from enum ObjectTypeEnum
	kExplodedViewsObject          =134218496  # from enum ObjectTypeEnum
	kExpressionLimitsObject       =50422784   # from enum ObjectTypeEnum
	kExpressionListObject         =50433792   # from enum ObjectTypeEnum
	kExtendFeatureObject          =83977984   # from enum ObjectTypeEnum
	kExtendFeatureProxyObject     =83978496   # from enum ObjectTypeEnum
	kExtendFeaturesObject         =83978240   # from enum ObjectTypeEnum
	kExtrudeDefinitionObject      =84014080   # from enum ObjectTypeEnum
	kExtrudeFeatureObject         =83910656   # from enum ObjectTypeEnum
	kExtrudeFeatureProxyObject    =83958016   # from enum ObjectTypeEnum
	kExtrudeFeaturesObject        =83910912   # from enum ObjectTypeEnum
	kFaceCollectionObject         =40704      # from enum ObjectTypeEnum
	kFaceDefinitionObject         =50428416   # from enum ObjectTypeEnum
	kFaceDefinitionsObject        =50428160   # from enum ObjectTypeEnum
	kFaceDraftDefinitionObject    =84046336   # from enum ObjectTypeEnum
	kFaceDraftFeatureObject       =83911168   # from enum ObjectTypeEnum
	kFaceDraftFeatureProxyObject  =83958272   # from enum ObjectTypeEnum
	kFaceDraftFeaturesObject      =83911424   # from enum ObjectTypeEnum
	kFaceFeatureDefinitionObject  =151006720  # from enum ObjectTypeEnum
	kFaceFeatureObject            =151000832  # from enum ObjectTypeEnum
	kFaceFeatureProxyObject       =151004672  # from enum ObjectTypeEnum
	kFaceFeaturesObject           =151000576  # from enum ObjectTypeEnum
	kFaceObject                   =67119408   # from enum ObjectTypeEnum
	kFaceOffsetDefinitionObject   =84016640   # from enum ObjectTypeEnum
	kFaceOffsetFeatureObject      =83982080   # from enum ObjectTypeEnum
	kFaceOffsetFeatureProxyObject =83982336   # from enum ObjectTypeEnum
	kFaceOffsetFeaturesObject     =83982592   # from enum ObjectTypeEnum
	kFaceProxyObject              =67119520   # from enum ObjectTypeEnum
	kFaceShellDefinitionObject    =50427904   # from enum ObjectTypeEnum
	kFaceShellDefinitionsObject   =50427648   # from enum ObjectTypeEnum
	kFaceShellObject              =67119152   # from enum ObjectTypeEnum
	kFaceShellProxyObject         =67119264   # from enum ObjectTypeEnum
	kFaceShellsObject             =67121712   # from enum ObjectTypeEnum
	kFacesObject                  =67118592   # from enum ObjectTypeEnum
	kFactoryOptionsObject         =84001024   # from enum ObjectTypeEnum
	kFactoryTableDialog           =50461440   # from enum ObjectTypeEnum
	kFamilyManagerObject          =50410240   # from enum ObjectTypeEnum
	kFeatureBasedOccurrencePatternObject=100669184  # from enum ObjectTypeEnum
	kFeatureBasedOccurrencePatternProxyObject=100669312  # from enum ObjectTypeEnum
	kFeatureControlFrameObject    =117483008  # from enum ObjectTypeEnum
	kFeatureControlFrameRowObject =117483520  # from enum ObjectTypeEnum
	kFeatureControlFrameRowsObject=117483264  # from enum ObjectTypeEnum
	kFeatureControlFrameStyleObject=117481472  # from enum ObjectTypeEnum
	kFeatureControlFrameStylesEnumeratorObject=117481216  # from enum ObjectTypeEnum
	kFeatureControlFramesObject   =117482752  # from enum ObjectTypeEnum
	kFeatureDimensionObject       =83991296   # from enum ObjectTypeEnum
	kFeatureDimensionProxyObject  =83991408   # from enum ObjectTypeEnum
	kFeatureDimensionsObject      =83991040   # from enum ObjectTypeEnum
	kFeaturePatternElementObject  =83923968   # from enum ObjectTypeEnum
	kFeaturePatternElementProxyObject=83923974   # from enum ObjectTypeEnum
	kFeaturePatternElementsObject =83923712   # from enum ObjectTypeEnum
	kFeaturesObject               =100675328  # from enum ObjectTypeEnum
	kFileAccessEventsObject       =50335488   # from enum ObjectTypeEnum
	kFileAndReferencesCollectionObject=50334976   # from enum ObjectTypeEnum
	kFileDescriptorObject         =50407680   # from enum ObjectTypeEnum
	kFileDescriptorsEnumeratorObject=50407424   # from enum ObjectTypeEnum
	kFileDialogEventsObject       =50414592   # from enum ObjectTypeEnum
	kFileDialogObject             =50377728   # from enum ObjectTypeEnum
	kFileLocationsObject          =50339584   # from enum ObjectTypeEnum
	kFileManagerEventsObject      =50398208   # from enum ObjectTypeEnum
	kFileManagerObject            =50378240   # from enum ObjectTypeEnum
	kFileMetadataObject           =50418176   # from enum ObjectTypeEnum
	kFileObject                   =50407168   # from enum ObjectTypeEnum
	kFileOpenOptionsObject        =50436352   # from enum ObjectTypeEnum
	kFileOptionsObject            =50399488   # from enum ObjectTypeEnum
	kFileSaveAsObject             =50339328   # from enum ObjectTypeEnum
	kFileUIEventsObject           =50333952   # from enum ObjectTypeEnum
	kFilenameAssetValueObject     =50451968   # from enum ObjectTypeEnum
	kFilesEnumeratorObject        =50406912   # from enum ObjectTypeEnum
	kFilletConstantRadiusEdgeSetObject=83927040   # from enum ObjectTypeEnum
	kFilletConstantRadiusFaceSetObject=83978752   # from enum ObjectTypeEnum
	kFilletDefinitionObject       =83926272   # from enum ObjectTypeEnum
	kFilletFaceSetObject          =83978752   # from enum ObjectTypeEnum
	kFilletFeatureObject          =83911680   # from enum ObjectTypeEnum
	kFilletFeatureProxyObject     =83958528   # from enum ObjectTypeEnum
	kFilletFeaturesObject         =83911936   # from enum ObjectTypeEnum
	kFilletFullRoundSetObject     =83979008   # from enum ObjectTypeEnum
	kFilletIntermediateRadiusObject=83927552   # from enum ObjectTypeEnum
	kFilletRadiusEdgeSetObject    =83926784   # from enum ObjectTypeEnum
	kFilletSetbackObject          =83928320   # from enum ObjectTypeEnum
	kFilletSetbackVertexObject    =83928064   # from enum ObjectTypeEnum
	kFilletVariableRadiusEdgeSetObject=83927296   # from enum ObjectTypeEnum
	kFixedWorkAxisDefObject       =83892992   # from enum ObjectTypeEnum
	kFixedWorkPlaneDefObject      =83890432   # from enum ObjectTypeEnum
	kFixedWorkPointDefObject      =83895040   # from enum ObjectTypeEnum
	kFlangeDefinitionObject       =151011840  # from enum ObjectTypeEnum
	kFlangeFeatureObject          =151001344  # from enum ObjectTypeEnum
	kFlangeFeatureProxyObject     =151004928  # from enum ObjectTypeEnum
	kFlangeFeaturesObject         =151001088  # from enum ObjectTypeEnum
	kFlatBendResultObject         =151005952  # from enum ObjectTypeEnum
	kFlatBendResultsObject        =151005696  # from enum ObjectTypeEnum
	kFlatPatternFeaturesObject    =84000768   # from enum ObjectTypeEnum
	kFlatPatternObject            =151002624  # from enum ObjectTypeEnum
	kFlatPatternOrientationObject =151023872  # from enum ObjectTypeEnum
	kFlatPatternOrientationsObject=151023616  # from enum ObjectTypeEnum
	kFlatPatternPlateObject       =151024128  # from enum ObjectTypeEnum
	kFlatPatternPlatesObject      =151024384  # from enum ObjectTypeEnum
	kFlatPatternSettingsObject    =50456064   # from enum ObjectTypeEnum
	kFlatPunchResultObject        =151006464  # from enum ObjectTypeEnum
	kFlatPunchResultsObject       =151006208  # from enum ObjectTypeEnum
	kFloatAssetValueObject        =50450176   # from enum ObjectTypeEnum
	kFlushConstraintObject        =100666368  # from enum ObjectTypeEnum
	kFlushConstraintProxyObject   =100675840  # from enum ObjectTypeEnum
	kFlushiMateDefinitionObject   =83947264   # from enum ObjectTypeEnum
	kFlushiMateDefinitionProxyObject=83947392   # from enum ObjectTypeEnum
	kFoldDefinitionObject         =151010560  # from enum ObjectTypeEnum
	kFoldFeatureObject            =150999296  # from enum ObjectTypeEnum
	kFoldFeatureProxyObject       =151003904  # from enum ObjectTypeEnum
	kFoldFeaturesObject           =150998784  # from enum ObjectTypeEnum
	kFreeDragMoveOperationObject  =84015104   # from enum ObjectTypeEnum
	kFreeMoveDefinitionObject     =84012544   # from enum ObjectTypeEnum
	kFreeformFeatureObject        =84032256   # from enum ObjectTypeEnum
	kFreeformFeatureProxyObject   =84032768   # from enum ObjectTypeEnum
	kFreeformFeaturesObject       =84032512   # from enum ObjectTypeEnum
	kFromToExtentObject           =83919360   # from enum ObjectTypeEnum
	kFromToWidthExtentObject      =83997440   # from enum ObjectTypeEnum
	kFullSweepExtentObject        =83918336   # from enum ObjectTypeEnum
	kGeneralDimensionObject       =117456896  # from enum ObjectTypeEnum
	kGeneralDimensionsEnumeratorObject=117464576  # from enum ObjectTypeEnum
	kGeneralDimensionsObject      =117455104  # from enum ObjectTypeEnum
	kGeneralNoteObject            =117472512  # from enum ObjectTypeEnum
	kGeneralNoteSymbolDefinitionObject=84063232   # from enum ObjectTypeEnum
	kGeneralNoteSymbolDefinitionsObject=84063488   # from enum ObjectTypeEnum
	kGeneralNotesObject           =117472256  # from enum ObjectTypeEnum
	kGeneralOptionsObject         =50386688   # from enum ObjectTypeEnum
	kGeneralPreferencesObject     =50345216   # from enum ObjectTypeEnum
	kGenericObject                =2130706445 # from enum ObjectTypeEnum
	kGeometricConstraints3DObject =83941376   # from enum ObjectTypeEnum
	kGeometricConstraintsObject   =83899904   # from enum ObjectTypeEnum
	kGeometryIntentObject         =117474048  # from enum ObjectTypeEnum
	kGraphicsColorMapperObject    =84000512   # from enum ObjectTypeEnum
	kGraphicsColorSetObject       =50360832   # from enum ObjectTypeEnum
	kGraphicsCoordinateSetObject  =50360320   # from enum ObjectTypeEnum
	kGraphicsDataSetObject        =50360064   # from enum ObjectTypeEnum
	kGraphicsDataSetsCollectionObject=50359552   # from enum ObjectTypeEnum
	kGraphicsDataSetsObject       =50359808   # from enum ObjectTypeEnum
	kGraphicsImageSetObject       =50431744   # from enum ObjectTypeEnum
	kGraphicsIndexSetObject       =50361088   # from enum ObjectTypeEnum
	kGraphicsNodeObject           =50356736   # from enum ObjectTypeEnum
	kGraphicsNodeProxyObject      =50356896   # from enum ObjectTypeEnum
	kGraphicsNormalSetObject      =50360576   # from enum ObjectTypeEnum
	kGraphicsPreferencesObject    =50340096   # from enum ObjectTypeEnum
	kGraphicsPrimitiveObject      =50356992   # from enum ObjectTypeEnum
	kGraphicsTextureCoordinateSetObject=84000256   # from enum ObjectTypeEnum
	kGrillFeatureObject           =84002816   # from enum ObjectTypeEnum
	kGrillFeatureProxyObject      =84002928   # from enum ObjectTypeEnum
	kGrillFeaturesObject          =84003072   # from enum ObjectTypeEnum
	kGripSnapOptionsObject        =50430976   # from enum ObjectTypeEnum
	kGroundConstraint3DObject     =83965952   # from enum ObjectTypeEnum
	kGroundConstraint3DProxyObject=83966064   # from enum ObjectTypeEnum
	kGroundConstraintObject       =83901952   # from enum ObjectTypeEnum
	kGroundConstraintProxyObject  =83902064   # from enum ObjectTypeEnum
	kGroundPlaneSettingsObject    =50436096   # from enum ObjectTypeEnum
	kHardwareOptionsObject        =50406656   # from enum ObjectTypeEnum
	kHeadsUpDisplayOptionsObject  =50435584   # from enum ObjectTypeEnum
	kHelicalConstraint3DObject    =84009216   # from enum ObjectTypeEnum
	kHelicalConstraint3DProxyObject=84009328   # from enum ObjectTypeEnum
	kHelicalCurveConstantShapeDefinitionObject=84074496   # from enum ObjectTypeEnum
	kHelicalCurveDefinitionObject =84074240   # from enum ObjectTypeEnum
	kHelicalCurveObject           =84073984   # from enum ObjectTypeEnum
	kHelicalCurveProxyObject      =84074096   # from enum ObjectTypeEnum
	kHelicalCurveShapeDefinitionRowObject=84075264   # from enum ObjectTypeEnum
	kHelicalCurveShapeDefinitionRowsObject=84075008   # from enum ObjectTypeEnum
	kHelicalCurveVariableShapeDefinitionObject=84074752   # from enum ObjectTypeEnum
	kHelicalCurvesObject          =84075520   # from enum ObjectTypeEnum
	kHelpEventsObject             =50442496   # from enum ObjectTypeEnum
	kHelpManagerObject            =50344960   # from enum ObjectTypeEnum
	kHemDefinitionObject          =151014400  # from enum ObjectTypeEnum
	kHemFeatureObject             =150998528  # from enum ObjectTypeEnum
	kHemFeatureProxyObject        =151003648  # from enum ObjectTypeEnum
	kHemFeaturesObject            =150998272  # from enum ObjectTypeEnum
	kHighlightSetObject           =50366976   # from enum ObjectTypeEnum
	kHighlightSetsObject          =50366720   # from enum ObjectTypeEnum
	kHoleFeatureObject            =83912192   # from enum ObjectTypeEnum
	kHoleFeatureProxyObject       =83958784   # from enum ObjectTypeEnum
	kHoleFeaturesObject           =83912448   # from enum ObjectTypeEnum
	kHoleNoteObject               =117487360  # from enum ObjectTypeEnum
	kHolePlacementDefinitionObject=83966464   # from enum ObjectTypeEnum
	kHoleTableCellObject          =117471232  # from enum ObjectTypeEnum
	kHoleTableColumnObject        =117470464  # from enum ObjectTypeEnum
	kHoleTableColumnsObject       =117470208  # from enum ObjectTypeEnum
	kHoleTableObject              =117469952  # from enum ObjectTypeEnum
	kHoleTableRowObject           =117470976  # from enum ObjectTypeEnum
	kHoleTableRowsObject          =117470720  # from enum ObjectTypeEnum
	kHoleTableStyleObject         =117485312  # from enum ObjectTypeEnum
	kHoleTableStylesEnumeratorObject=117485056  # from enum ObjectTypeEnum
	kHoleTablesObject             =117469696  # from enum ObjectTypeEnum
	kHoleTagObject                =117471488  # from enum ObjectTypeEnum
	kHoleTapInfoObject            =83920384   # from enum ObjectTypeEnum
	kHoleThreadNoteObject         =117491712  # from enum ObjectTypeEnum
	kHoleThreadNotesObject        =117491456  # from enum ObjectTypeEnum
	kHorizontalAlignConstraintObject=83902464   # from enum ObjectTypeEnum
	kHorizontalAlignConstraintProxyObject=83902576   # from enum ObjectTypeEnum
	kHorizontalConstraintObject   =83902208   # from enum ObjectTypeEnum
	kHorizontalConstraintProxyObject=83902320   # from enum ObjectTypeEnum
	kImportedComponentDefinitionObject=84047104   # from enum ObjectTypeEnum
	kImportedComponentObject      =84046592   # from enum ObjectTypeEnum
	kImportedComponentsObject     =84046848   # from enum ObjectTypeEnum
	kImportedDWGComponentDefinitionObject=84038912   # from enum ObjectTypeEnum
	kImportedDWGComponentObject   =84038400   # from enum ObjectTypeEnum
	kImportedDWGComponentProxyObject=84038656   # from enum ObjectTypeEnum
	kImportedDWGLayerObject       =84057088   # from enum ObjectTypeEnum
	kImportedDWGLayersEnumeratorObject=84057344   # from enum ObjectTypeEnum
	kImportedGenericComponentDefinitionObject=84047872   # from enum ObjectTypeEnum
	kImportedGenericComponentObject=84049664   # from enum ObjectTypeEnum
	kImportedGenericComponentProxyObject=84049920   # from enum ObjectTypeEnum
	kImportedModelEntitiesObject  =84047360   # from enum ObjectTypeEnum
	kImportedModelEntityObject    =84047616   # from enum ObjectTypeEnum
	kInsertConstraintObject       =100665344  # from enum ObjectTypeEnum
	kInsertConstraintProxyObject  =100676096  # from enum ObjectTypeEnum
	kInsertiMateDefinitionObject  =83947520   # from enum ObjectTypeEnum
	kInsertiMateDefinitionProxyObject=83947648   # from enum ObjectTypeEnum
	kIntegerAssetValueObject      =50450432   # from enum ObjectTypeEnum
	kIntentConfigurationObject    =50416128   # from enum ObjectTypeEnum
	kInteractionEventsObject      =50353152   # from enum ObjectTypeEnum
	kInteractionGraphicsObject    =50387200   # from enum ObjectTypeEnum
	kInterferenceResultObject     =100668416  # from enum ObjectTypeEnum
	kInterferenceResultsObject    =100668160  # from enum ObjectTypeEnum
	kIntersectionCurveObject      =84026624   # from enum ObjectTypeEnum
	kIntersectionCurveProxyObject =84026736   # from enum ObjectTypeEnum
	kIntersectionCurvesObject     =84026368   # from enum ObjectTypeEnum
	kInventorVBAArgumentObject    =50370304   # from enum ObjectTypeEnum
	kInventorVBAArgumentsObject   =50370048   # from enum ObjectTypeEnum
	kInventorVBAComponentObject   =50369280   # from enum ObjectTypeEnum
	kInventorVBAComponentsObject  =50369024   # from enum ObjectTypeEnum
	kInventorVBAMemberObject      =50369792   # from enum ObjectTypeEnum
	kInventorVBAMembersObject     =50369536   # from enum ObjectTypeEnum
	kInventorVBAProjectObject     =50368768   # from enum ObjectTypeEnum
	kInventorVBAProjectsObject    =50368512   # from enum ObjectTypeEnum
	kJointOriginDWGObject         =100707331  # from enum ObjectTypeEnum
	kJointOriginEdgeObject        =100707329  # from enum ObjectTypeEnum
	kJointOriginFaceObject        =100707328  # from enum ObjectTypeEnum
	kJointOriginSketchObject      =100707330  # from enum ObjectTypeEnum
	kKeyboardEventsObject         =50354176   # from enum ObjectTypeEnum
	kKnitFeatureObject            =83954176   # from enum ObjectTypeEnum
	kKnitFeatureProxyObject       =83959040   # from enum ObjectTypeEnum
	kKnitFeaturesObject           =83954432   # from enum ObjectTypeEnum
	kLanguageToolsObject          =50415872   # from enum ObjectTypeEnum
	kLayerObject                  =117466112  # from enum ObjectTypeEnum
	kLayersEnumeratorObject       =117465856  # from enum ObjectTypeEnum
	kLayoutConstraintObject       =100699392  # from enum ObjectTypeEnum
	kLayoutConstraintProxyObject  =100699648  # from enum ObjectTypeEnum
	kLeaderNodeObject             =117477376  # from enum ObjectTypeEnum
	kLeaderNodesEnumeratorObject  =117477632  # from enum ObjectTypeEnum
	kLeaderNoteObject             =117473024  # from enum ObjectTypeEnum
	kLeaderNotesObject            =117472768  # from enum ObjectTypeEnum
	kLeaderObject                 =117475584  # from enum ObjectTypeEnum
	kLeaderStyleObject            =117480448  # from enum ObjectTypeEnum
	kLeaderStylesEnumeratorObject =117480192  # from enum ObjectTypeEnum
	kLegacyDistanceHeightExtentObject=83995904   # from enum ObjectTypeEnum
	kLevelOfDetailRepresentationObject=100679936  # from enum ObjectTypeEnum
	kLevelOfDetailRepresentationsObject=100679680  # from enum ObjectTypeEnum
	kLibraryFolderObject          =117499392  # from enum ObjectTypeEnum
	kLibraryFoldersObject         =117499648  # from enum ObjectTypeEnum
	kLibraryManagerObject         =50409728   # from enum ObjectTypeEnum
	kLibrarySketchedSymbolDefinitionObject=117498880  # from enum ObjectTypeEnum
	kLibrarySketchedSymbolDefinitionsObject=117499136  # from enum ObjectTypeEnum
	kLightObject                  =50402560   # from enum ObjectTypeEnum
	kLightingStyleObject          =50402048   # from enum ObjectTypeEnum
	kLightingStylesObject         =50401792   # from enum ObjectTypeEnum
	kLightsObject                 =50402304   # from enum ObjectTypeEnum
	kLineAndFaceWorkPointDefObject=83894272   # from enum ObjectTypeEnum
	kLineAndPlaneWorkAxisDefObject=83892736   # from enum ObjectTypeEnum
	kLineAndPointWorkAxisDefObject=83979264   # from enum ObjectTypeEnum
	kLineAndPointWorkPlaneDefObject=83888640   # from enum ObjectTypeEnum
	kLineAndTangentWorkPlaneDefObject=83889664   # from enum ObjectTypeEnum
	kLineGraphicsObject           =50357248   # from enum ObjectTypeEnum
	kLineLengthDimConstraint3DObject=83971840   # from enum ObjectTypeEnum
	kLineLengthDimConstraint3DProxyObject=83971952   # from enum ObjectTypeEnum
	kLinePlaneAndAngleWorkPlaneDefObject=83889152   # from enum ObjectTypeEnum
	kLineStripGraphicsObject      =50357504   # from enum ObjectTypeEnum
	kLineWorkAxisDefObject        =83891456   # from enum ObjectTypeEnum
	kLinearGeneralDimensionObject =117474560  # from enum ObjectTypeEnum
	kLinearHolePlacementDefinitionObject=83966976   # from enum ObjectTypeEnum
	kLinearModelDimensionDefinitionObject=84021504   # from enum ObjectTypeEnum
	kLinearModelDimensionObject   =84021760   # from enum ObjectTypeEnum
	kLinearModelDimensionProxyObject=84021872   # from enum ObjectTypeEnum
	kLinearModelDimensionsObject  =84020992   # from enum ObjectTypeEnum
	kLipFeatureObject             =84003328   # from enum ObjectTypeEnum
	kLipFeatureProxyObject        =84003440   # from enum ObjectTypeEnum
	kLipFeaturesObject            =84003584   # from enum ObjectTypeEnum
	kLoftFeatureObject            =83912704   # from enum ObjectTypeEnum
	kLoftFeatureProxyObject       =83959296   # from enum ObjectTypeEnum
	kLoftFeaturesObject           =83912960   # from enum ObjectTypeEnum
	kLoftRailObject               =83977472   # from enum ObjectTypeEnum
	kLoftRailsObject              =83977216   # from enum ObjectTypeEnum
	kLoftSectionDimensionObject   =83992576   # from enum ObjectTypeEnum
	kLoftSectionDimensionsObject  =83992320   # from enum ObjectTypeEnum
	kLoftedFlangeDefinitionObject =151023360  # from enum ObjectTypeEnum
	kLoftedFlangeFeatureObject    =151015680  # from enum ObjectTypeEnum
	kLoftedFlangeFeatureProxyObject=151016192  # from enum ObjectTypeEnum
	kLoftedFlangeFeaturesObject   =151015936  # from enum ObjectTypeEnum
	kLumpDefinitionObject         =50432768   # from enum ObjectTypeEnum
	kLumpDefinitionsObject        =50432512   # from enum ObjectTypeEnum
	kMachiningObject              =100698880  # from enum ObjectTypeEnum
	kMacroControlDefinitionObject =50372352   # from enum ObjectTypeEnum
	kManipulatorEventsObject      =50456832   # from enum ObjectTypeEnum
	kMapPointCurveObject          =83945984   # from enum ObjectTypeEnum
	kMapPointCurvesObject         =83946240   # from enum ObjectTypeEnum
	kMassPropertiesObject         =50366208   # from enum ObjectTypeEnum
	kMateConstraintObject         =100665856  # from enum ObjectTypeEnum
	kMateConstraintProxyObject    =100676352  # from enum ObjectTypeEnum
	kMateiMateDefinitionObject    =83947776   # from enum ObjectTypeEnum
	kMateiMateDefinitionProxyObject=83947904   # from enum ObjectTypeEnum
	kMaterialAssetObject          =50448896   # from enum ObjectTypeEnum
	kMaterialObject               =50362368   # from enum ObjectTypeEnum
	kMaterialsEnumeratorObject    =50426368   # from enum ObjectTypeEnum
	kMaterialsObject              =50362112   # from enum ObjectTypeEnum
	kMeasureEventsObject          =50416384   # from enum ObjectTypeEnum
	kMeasureToolsObject           =50413568   # from enum ObjectTypeEnum
	kMemberManagerObject          =50410496   # from enum ObjectTypeEnum
	kMeshEdgeObject               =84055296   # from enum ObjectTypeEnum
	kMeshEdgeProxyObject          =84055408   # from enum ObjectTypeEnum
	kMeshFaceObject               =84055040   # from enum ObjectTypeEnum
	kMeshFaceProxyObject          =84055152   # from enum ObjectTypeEnum
	kMeshFeatureEntitiesEnumeratorObject=84053504   # from enum ObjectTypeEnum
	kMeshFeatureEntityObject      =84053248   # from enum ObjectTypeEnum
	kMeshFeatureEntityProxyObject =84053360   # from enum ObjectTypeEnum
	kMeshFeatureObject            =84052480   # from enum ObjectTypeEnum
	kMeshFeatureProxyObject       =84052592   # from enum ObjectTypeEnum
	kMeshFeatureSetObject         =84052736   # from enum ObjectTypeEnum
	kMeshFeatureSetProxyObject    =84052848   # from enum ObjectTypeEnum
	kMeshFeatureSetsObject        =84052992   # from enum ObjectTypeEnum
	kMeshVertexObject             =84055552   # from enum ObjectTypeEnum
	kMeshVertexProxyObject        =84055664   # from enum ObjectTypeEnum
	kMessageSectionObject         =50420992   # from enum ObjectTypeEnum
	kMidPointWorkPointDefObject   =83894784   # from enum ObjectTypeEnum
	kMidSurfaceFeatureObject      =84016128   # from enum ObjectTypeEnum
	kMidSurfaceFeatureProxyObject =84015872   # from enum ObjectTypeEnum
	kMidSurfaceFeaturesObject     =84016384   # from enum ObjectTypeEnum
	kMidSurfaceThicknessObject    =84017152   # from enum ObjectTypeEnum
	kMidSurfaceThicknessesObject  =84016896   # from enum ObjectTypeEnum
	kMidpointConstraint3DObject   =84000000   # from enum ObjectTypeEnum
	kMidpointConstraint3DProxyObject=84000112   # from enum ObjectTypeEnum
	kMidpointConstraintObject     =83902720   # from enum ObjectTypeEnum
	kMidpointConstraintProxyObject=83902832   # from enum ObjectTypeEnum
	kMiniToolbarButtonObject      =50443520   # from enum ObjectTypeEnum
	kMiniToolbarCheckBoxObject    =50443776   # from enum ObjectTypeEnum
	kMiniToolbarComboBoxObject    =50444032   # from enum ObjectTypeEnum
	kMiniToolbarControlObject     =50443264   # from enum ObjectTypeEnum
	kMiniToolbarControlsObject    =50444800   # from enum ObjectTypeEnum
	kMiniToolbarDropdownObject    =50444288   # from enum ObjectTypeEnum
	kMiniToolbarListItemObject    =50445312   # from enum ObjectTypeEnum
	kMiniToolbarObject            =50441216   # from enum ObjectTypeEnum
	kMiniToolbarSliderObject      =50446848   # from enum ObjectTypeEnum
	kMiniToolbarTextBoxObject     =50461696   # from enum ObjectTypeEnum
	kMiniToolbarTextEditorObject  =50453504   # from enum ObjectTypeEnum
	kMiniToolbarValueEditorObject =50444544   # from enum ObjectTypeEnum
	kMirrorFeatureDefinitionObject=84059136   # from enum ObjectTypeEnum
	kMirrorFeatureObject          =83913216   # from enum ObjectTypeEnum
	kMirrorFeatureProxyObject     =83959552   # from enum ObjectTypeEnum
	kMirrorFeaturesObject         =83913472   # from enum ObjectTypeEnum
	kModelAnnotationObject        =84020224   # from enum ObjectTypeEnum
	kModelAnnotationTextObject    =84027136   # from enum ObjectTypeEnum
	kModelAnnotationsEnumeratorObject=84030208   # from enum ObjectTypeEnum
	kModelAnnotationsObject       =84019968   # from enum ObjectTypeEnum
	kModelCompositeAnnotationDefinitionObject=84054272   # from enum ObjectTypeEnum
	kModelCompositeAnnotationObject=84054016   # from enum ObjectTypeEnum
	kModelCompositeAnnotationProxyObject=84054128   # from enum ObjectTypeEnum
	kModelCompositeAnnotationsObject=84053760   # from enum ObjectTypeEnum
	kModelDatumIdentifierDefinitionObject=84031744   # from enum ObjectTypeEnum
	kModelDatumIdentifierObject   =84031488   # from enum ObjectTypeEnum
	kModelDatumIdentifierProxyObject=84031600   # from enum ObjectTypeEnum
	kModelDatumIdentifiersObject  =84031232   # from enum ObjectTypeEnum
	kModelDatumReferenceFrameDefinitionObject=84061696   # from enum ObjectTypeEnum
	kModelDatumReferenceFrameObject=84061952   # from enum ObjectTypeEnum
	kModelDatumReferenceFrameProxyObject=84062064   # from enum ObjectTypeEnum
	kModelDatumReferenceFramesObject=84062208   # from enum ObjectTypeEnum
	kModelDimensionDefinitionObject=84021248   # from enum ObjectTypeEnum
	kModelDimensionObject         =84020736   # from enum ObjectTypeEnum
	kModelDimensionsObject        =84020480   # from enum ObjectTypeEnum
	kModelFeatureControlFrameDefinitionObject=84030976   # from enum ObjectTypeEnum
	kModelFeatureControlFrameObject=84024064   # from enum ObjectTypeEnum
	kModelFeatureControlFrameProxyObject=84024176   # from enum ObjectTypeEnum
	kModelFeatureControlFrameRowObject=84030720   # from enum ObjectTypeEnum
	kModelFeatureControlFrameRowsObject=84030464   # from enum ObjectTypeEnum
	kModelFeatureControlFramesObject=84023808   # from enum ObjectTypeEnum
	kModelGeneralNoteDefinitionObject=84062720   # from enum ObjectTypeEnum
	kModelGeneralNoteObject       =84062464   # from enum ObjectTypeEnum
	kModelGeneralNoteProxyObject  =84062576   # from enum ObjectTypeEnum
	kModelGeneralNotesObject      =84062720   # from enum ObjectTypeEnum
	kModelHoleThreadNoteDefinitionObject=84029440   # from enum ObjectTypeEnum
	kModelHoleThreadNoteObject    =84028928   # from enum ObjectTypeEnum
	kModelHoleThreadNoteProxyObject=84029040   # from enum ObjectTypeEnum
	kModelHoleThreadNotesObject   =84029184   # from enum ObjectTypeEnum
	kModelLeaderNodeObject        =84024576   # from enum ObjectTypeEnum
	kModelLeaderNodesEnumeratorObject=84024832   # from enum ObjectTypeEnum
	kModelLeaderNoteDefinitionObject=84026880   # from enum ObjectTypeEnum
	kModelLeaderNoteObject        =84025088   # from enum ObjectTypeEnum
	kModelLeaderNoteProxyObject   =84025200   # from enum ObjectTypeEnum
	kModelLeaderNotesObject       =84025344   # from enum ObjectTypeEnum
	kModelLeaderObject            =84024320   # from enum ObjectTypeEnum
	kModelParameterObject         =50348544   # from enum ObjectTypeEnum
	kModelParametersObject        =50347264   # from enum ObjectTypeEnum
	kModelSurfaceTextureSymbolDefinitionObject=84028416   # from enum ObjectTypeEnum
	kModelSurfaceTextureSymbolObject=84028160   # from enum ObjectTypeEnum
	kModelSurfaceTextureSymbolProxyObject=84028272   # from enum ObjectTypeEnum
	kModelSurfaceTextureSymbolsObject=84028672   # from enum ObjectTypeEnum
	kModelToleranceFeatureDefinitionObject=84056064   # from enum ObjectTypeEnum
	kModelToleranceFeatureObject  =84056320   # from enum ObjectTypeEnum
	kModelToleranceFeatureProxyObject=84056432   # from enum ObjectTypeEnum
	kModelToleranceFeaturesEnumeratorObject=84056832   # from enum ObjectTypeEnum
	kModelToleranceFeaturesObject =84056576   # from enum ObjectTypeEnum
	kModelingEventsObject         =50408704   # from enum ObjectTypeEnum
	kModelingSettingsObject       =50383872   # from enum ObjectTypeEnum
	kMouseEventsObject            =50353664   # from enum ObjectTypeEnum
	kMoveAlongRayMoveOperationObject=84015360   # from enum ObjectTypeEnum
	kMoveDefinitionObject         =84014592   # from enum ObjectTypeEnum
	kMoveFaceDefinitionObject     =84011776   # from enum ObjectTypeEnum
	kMoveFaceFeatureObject        =83967744   # from enum ObjectTypeEnum
	kMoveFaceFeatureProxyObject   =83968000   # from enum ObjectTypeEnum
	kMoveFaceFeaturesObject       =83968256   # from enum ObjectTypeEnum
	kMoveFeatureObject            =84002048   # from enum ObjectTypeEnum
	kMoveFeatureProxyObject       =84002208   # from enum ObjectTypeEnum
	kMoveFeaturesObject           =84001792   # from enum ObjectTypeEnum
	kMoveOperationObject          =84014848   # from enum ObjectTypeEnum
	kNativeBrowserNodeDefinitionObject=50387456   # from enum ObjectTypeEnum
	kNonLinearEdgeWorkPointDefObject=83979776   # from enum ObjectTypeEnum
	kNonParametricBaseFeatureObject=83920896   # from enum ObjectTypeEnum
	kNonParametricBaseFeatureProxyObject=83962112   # from enum ObjectTypeEnum
	kNonParametricBaseFeaturesObject=83945728   # from enum ObjectTypeEnum
	kNormalToCurveWorkPlaneDefObject=83951616   # from enum ObjectTypeEnum
	kNormalToSurfaceWorkAxisDefObject=83968768   # from enum ObjectTypeEnum
	kNotebookOptionsObject        =50406400   # from enum ObjectTypeEnum
	kOGSRenderItemObject          =100705536  # from enum ObjectTypeEnum
	kOGSRenderItemsEnumeratorObject=100705792  # from enum ObjectTypeEnum
	kOGSSceneNodeObject           =100705024  # from enum ObjectTypeEnum
	kOGSSceneNodesEnumeratorObject=100705280  # from enum ObjectTypeEnum
	kObjectCollectionByVariantObject=2130706444 # from enum ObjectTypeEnum
	kObjectCollectionObject       =2130706443 # from enum ObjectTypeEnum
	kObjectDefaultsStyleObject    =117454336  # from enum ObjectTypeEnum
	kObjectDefaultsStylesEnumeratorObject=117464064  # from enum ObjectTypeEnum
	kObjectVisibilityObject       =50431488   # from enum ObjectTypeEnum
	kObjectsEnumeratorByVariantObject=2130706451 # from enum ObjectTypeEnum
	kObjectsEnumeratorObject      =2130706450 # from enum ObjectTypeEnum
	kOccurrencePatternElementObject=67128832   # from enum ObjectTypeEnum
	kOccurrencePatternElementProxyObject=67128992   # from enum ObjectTypeEnum
	kOccurrencePatternElementsObject=100669952  # from enum ObjectTypeEnum
	kOccurrencePatternObject      =100668928  # from enum ObjectTypeEnum
	kOccurrencePatternsObject     =100668672  # from enum ObjectTypeEnum
	kOffsetConstraintObject       =83901184   # from enum ObjectTypeEnum
	kOffsetConstraintProxyObject  =83901296   # from enum ObjectTypeEnum
	kOffsetDimConstraintObject    =83905536   # from enum ObjectTypeEnum
	kOffsetDimConstraintProxyObject=83905648   # from enum ObjectTypeEnum
	kOffsetSplineDimConstraintObject=83972608   # from enum ObjectTypeEnum
	kOffsetSplineDimConstraintProxyObject=83972720   # from enum ObjectTypeEnum
	kOffsetWidthExtentObject      =83997184   # from enum ObjectTypeEnum
	kOnFaceConstraint3DObject     =84061440   # from enum ObjectTypeEnum
	kOnFaceConstraint3DProxyObject=84061552   # from enum ObjectTypeEnum
	kOnFaceCurveObject            =84051456   # from enum ObjectTypeEnum
	kOnFaceCurveProxyObject       =84051568   # from enum ObjectTypeEnum
	kOnFaceCurvesObject           =84051200   # from enum ObjectTypeEnum
	kOrdinateDimensionObject      =117484800  # from enum ObjectTypeEnum
	kOrdinateDimensionSetObject   =117489408  # from enum ObjectTypeEnum
	kOrdinateDimensionSetsObject  =117489152  # from enum ObjectTypeEnum
	kOrdinateDimensionsEnumeratorObject=117489664  # from enum ObjectTypeEnum
	kOrdinateDimensionsObject     =117484544  # from enum ObjectTypeEnum
	kOriginIndicatorObject        =117484288  # from enum ObjectTypeEnum
	kPanelBarObject               =50372864   # from enum ObjectTypeEnum
	kParallelConstraint3DObject   =83965696   # from enum ObjectTypeEnum
	kParallelConstraint3DProxyObject=83965808   # from enum ObjectTypeEnum
	kParallelConstraintObject     =83902976   # from enum ObjectTypeEnum
	kParallelConstraintProxyObject=83903088   # from enum ObjectTypeEnum
	kParallelToXAxisConstraint3DObject=84059904   # from enum ObjectTypeEnum
	kParallelToXAxisConstraint3DProxyObject=84060016   # from enum ObjectTypeEnum
	kParallelToXYPlaneConstraint3DObject=84060672   # from enum ObjectTypeEnum
	kParallelToXYPlaneConstraint3DProxyObject=84060784   # from enum ObjectTypeEnum
	kParallelToXZPlaneConstraint3DObject=84061184   # from enum ObjectTypeEnum
	kParallelToXZPlaneConstraint3DProxyObject=84061296   # from enum ObjectTypeEnum
	kParallelToYAxisConstraint3DObject=84060160   # from enum ObjectTypeEnum
	kParallelToYAxisConstraint3DProxyObject=84060272   # from enum ObjectTypeEnum
	kParallelToYZPlaneConstraint3DObject=84060928   # from enum ObjectTypeEnum
	kParallelToYZPlaneConstraint3DProxyObject=84061040   # from enum ObjectTypeEnum
	kParallelToZAxisConstraint3DObject=84060416   # from enum ObjectTypeEnum
	kParallelToZAxisConstraint3DProxyObject=84060528   # from enum ObjectTypeEnum
	kParameterTableObject         =50349568   # from enum ObjectTypeEnum
	kParameterTablesObject        =50348288   # from enum ObjectTypeEnum
	kParametersEnumeratorObject   =50367488   # from enum ObjectTypeEnum
	kParametersObject             =50347008   # from enum ObjectTypeEnum
	kPartComponentDefinitionObject=83886592   # from enum ObjectTypeEnum
	kPartComponentDefinitionsObject=83887360   # from enum ObjectTypeEnum
	kPartEventsObject             =83895552   # from enum ObjectTypeEnum
	kPartFeatureObject            =83886848   # from enum ObjectTypeEnum
	kPartFeaturesEnumeratorObject =83917312   # from enum ObjectTypeEnum
	kPartFeaturesObject           =83887104   # from enum ObjectTypeEnum
	kPartOptionsObject            =50405632   # from enum ObjectTypeEnum
	kPartialChamferEdgeObject     =84073216   # from enum ObjectTypeEnum
	kPartialChamferEdgesObject    =84073472   # from enum ObjectTypeEnum
	kPartsListCellObject          =117445376  # from enum ObjectTypeEnum
	kPartsListColumnObject        =117444608  # from enum ObjectTypeEnum
	kPartsListColumnsObject       =117444352  # from enum ObjectTypeEnum
	kPartsListObject              =117444096  # from enum ObjectTypeEnum
	kPartsListRowObject           =117445120  # from enum ObjectTypeEnum
	kPartsListRowsObject          =117444864  # from enum ObjectTypeEnum
	kPartsListStyleObject         =117493760  # from enum ObjectTypeEnum
	kPartsListStylesEnumeratorObject=117493504  # from enum ObjectTypeEnum
	kPartsListsObject             =117443840  # from enum ObjectTypeEnum
	kPathAndGuideRailSweepDefObject=83974144   # from enum ObjectTypeEnum
	kPathAndGuideSurfaceSweepDefObject=83976704   # from enum ObjectTypeEnum
	kPathAndSectionTwistsSweepDefObject=83990272   # from enum ObjectTypeEnum
	kPathEntityObject             =83942656   # from enum ObjectTypeEnum
	kPathEntityProxyObject        =83942661   # from enum ObjectTypeEnum
	kPathObject                   =83942400   # from enum ObjectTypeEnum
	kPathProxyObject              =83942402   # from enum ObjectTypeEnum
	kPathSweepDefObject           =83973888   # from enum ObjectTypeEnum
	kPatternConstraintObject      =83905024   # from enum ObjectTypeEnum
	kPatternConstraintProxyObject =83905136   # from enum ObjectTypeEnum
	kPerpendicularConstraint3DObject=83965440   # from enum ObjectTypeEnum
	kPerpendicularConstraint3DProxyObject=83965552   # from enum ObjectTypeEnum
	kPerpendicularConstraintObject=83903232   # from enum ObjectTypeEnum
	kPerpendicularConstraintProxyObject=83903344   # from enum ObjectTypeEnum
	kPitchAndHeightCoilExtentObject=83931904   # from enum ObjectTypeEnum
	kPitchAndRevolutionCoilExtentObject=83931392   # from enum ObjectTypeEnum
	kPlanarMoveDefinitionObject   =84012288   # from enum ObjectTypeEnum
	kPlanarSketchObject           =83924736   # from enum ObjectTypeEnum
	kPlanarSketchProxyObject      =83924848   # from enum ObjectTypeEnum
	kPlanarSketchesObject         =83895296   # from enum ObjectTypeEnum
	kPlaneAndOffsetWorkPlaneDefObject=83889408   # from enum ObjectTypeEnum
	kPlaneAndPointWorkPlaneDefObject=83888896   # from enum ObjectTypeEnum
	kPlaneAndTangentWorkPlaneDefObject=83889920   # from enum ObjectTypeEnum
	kPluginLicenseManagerEventsObject=50464256   # from enum ObjectTypeEnum
	kPluginLicenseManagerObject   =50462976   # from enum ObjectTypeEnum
	kPointAndPlaneDistanceDimConstraint3DObject=83971584   # from enum ObjectTypeEnum
	kPointAndPlaneDistanceDimConstraint3DProxyObject=83971696   # from enum ObjectTypeEnum
	kPointAndPlaneWorkAxisDefObject=83892480   # from enum ObjectTypeEnum
	kPointAndTangentWorkPlaneDefObject=83968512   # from enum ObjectTypeEnum
	kPointCloudCropObject         =84038144   # from enum ObjectTypeEnum
	kPointCloudCropsObject        =84037888   # from enum ObjectTypeEnum
	kPointCloudObject             =84017408   # from enum ObjectTypeEnum
	kPointCloudPlaneObject        =84032000   # from enum ObjectTypeEnum
	kPointCloudPlaneProxyObject   =84032112   # from enum ObjectTypeEnum
	kPointCloudPointObject        =84017664   # from enum ObjectTypeEnum
	kPointCloudPointProxyObject   =84017776   # from enum ObjectTypeEnum
	kPointCloudProxyObject        =84017520   # from enum ObjectTypeEnum
	kPointCloudRegionObject       =84037120   # from enum ObjectTypeEnum
	kPointCloudRegionsObject      =84036864   # from enum ObjectTypeEnum
	kPointCloudScanObject         =84037632   # from enum ObjectTypeEnum
	kPointCloudScansObject        =84037376   # from enum ObjectTypeEnum
	kPointCloudsObject            =84036608   # from enum ObjectTypeEnum
	kPointGraphicsObject          =50358528   # from enum ObjectTypeEnum
	kPointHolePlacementDefinitionObject=83967488   # from enum ObjectTypeEnum
	kPointInferenceObject         =67129088   # from enum ObjectTypeEnum
	kPointInferenceObjectEnumerator=67129344   # from enum ObjectTypeEnum
	kPointToPointRipTypeDefObject =151023104  # from enum ObjectTypeEnum
	kPointWorkPointDefObject      =83894528   # from enum ObjectTypeEnum
	kPositionalRepresentationObject=100678912  # from enum ObjectTypeEnum
	kPositionalRepresentationsObject=100678656  # from enum ObjectTypeEnum
	kPreparationsObject           =100699136  # from enum ObjectTypeEnum
	kPresentationBodiesEnumeratorObject=134231552  # from enum ObjectTypeEnum
	kPresentationBodyObject       =134231808  # from enum ObjectTypeEnum
	kPresentationComponentObject  =134231296  # from enum ObjectTypeEnum
	kPresentationComponentsEnumeratorObject=134231040  # from enum ObjectTypeEnum
	kPresentationEdgeObject       =134232832  # from enum ObjectTypeEnum
	kPresentationEdgesEnumeratorObject=134232576  # from enum ObjectTypeEnum
	kPresentationEventsObject     =134226688  # from enum ObjectTypeEnum
	kPresentationFaceObject       =134232320  # from enum ObjectTypeEnum
	kPresentationFacesEnumeratorObject=134232064  # from enum ObjectTypeEnum
	kPresentationMeshFeatureEntitiesEnumeratorObject=134235648  # from enum ObjectTypeEnum
	kPresentationMeshFeatureEntityObject=134235904  # from enum ObjectTypeEnum
	kPresentationMeshFeatureObject=134235392  # from enum ObjectTypeEnum
	kPresentationMeshFeatureSetObject=134235136  # from enum ObjectTypeEnum
	kPresentationMeshFeatureSetsEnumeratorObject=134234880  # from enum ObjectTypeEnum
	kPresentationOptionsObject    =50434304   # from enum ObjectTypeEnum
	kPresentationSceneObject      =134230272  # from enum ObjectTypeEnum
	kPresentationScenesObject     =134230016  # from enum ObjectTypeEnum
	kPresentationSequenceObject   =134225152  # from enum ObjectTypeEnum
	kPresentationSequencesObject  =134224896  # from enum ObjectTypeEnum
	kPresentationSnapshotViewObject=134230784  # from enum ObjectTypeEnum
	kPresentationSnapshotViewsObject=134230528  # from enum ObjectTypeEnum
	kPresentationTaskObject       =134225664  # from enum ObjectTypeEnum
	kPresentationTasksObject      =134225408  # from enum ObjectTypeEnum
	kPresentationTrailObject      =134233856  # from enum ObjectTypeEnum
	kPresentationTrailSegmentsEnumeratorObject=134234112  # from enum ObjectTypeEnum
	kPresentationTrailSegmentsObject=134234368  # from enum ObjectTypeEnum
	kPresentationTrailsObject     =134233600  # from enum ObjectTypeEnum
	kPresentationTweakObject      =134226176  # from enum ObjectTypeEnum
	kPresentationTweakTrailSegmentObject=134234624  # from enum ObjectTypeEnum
	kPresentationTweaksObject     =134225920  # from enum ObjectTypeEnum
	kPresentationVertexObject     =134233344  # from enum ObjectTypeEnum
	kPresentationVerticesEnumeratorObject=134233088  # from enum ObjectTypeEnum
	kPrintManagerObject           =50351360   # from enum ObjectTypeEnum
	kProfile3DObject              =83950080   # from enum ObjectTypeEnum
	kProfile3DProxyObject         =83950192   # from enum ObjectTypeEnum
	kProfileEntity3DObject        =83950592   # from enum ObjectTypeEnum
	kProfileEntity3DProxyObject   =83950704   # from enum ObjectTypeEnum
	kProfileEntityObject          =83908608   # from enum ObjectTypeEnum
	kProfileEntityProxyObject     =83908720   # from enum ObjectTypeEnum
	kProfileObject                =83898624   # from enum ObjectTypeEnum
	kProfilePath3DObject          =83950336   # from enum ObjectTypeEnum
	kProfilePath3DProxyObject     =83950448   # from enum ObjectTypeEnum
	kProfilePathObject            =83908352   # from enum ObjectTypeEnum
	kProfilePathProxyObject       =83908464   # from enum ObjectTypeEnum
	kProfileProxyObject           =83898736   # from enum ObjectTypeEnum
	kProfiles3DObject             =83949824   # from enum ObjectTypeEnum
	kProfilesObject               =83908864   # from enum ObjectTypeEnum
	kProgressBarObject            =50419968   # from enum ObjectTypeEnum
	kProgressiveToolTipObject     =50433536   # from enum ObjectTypeEnum
	kProjectAssetLibrariesObject  =50452736   # from enum ObjectTypeEnum
	kProjectAssetLibraryObject    =50452992   # from enum ObjectTypeEnum
	kProjectOptionsButtonObject   =50445056   # from enum ObjectTypeEnum
	kProjectPathObject            =50432256   # from enum ObjectTypeEnum
	kProjectPathsObject           =50432000   # from enum ObjectTypeEnum
	kProjectedCutObject           =84005632   # from enum ObjectTypeEnum
	kProjectedCutProxyObject      =84005888   # from enum ObjectTypeEnum
	kProjectedCutsObject          =84005376   # from enum ObjectTypeEnum
	kPropertyObject               =50339072   # from enum ObjectTypeEnum
	kPropertySetObject            =50338560   # from enum ObjectTypeEnum
	kPropertySetsObject           =50338304   # from enum ObjectTypeEnum
	kPublicationBodiesEnumeratorObject=134222848  # from enum ObjectTypeEnum
	kPublicationBodyObject        =134223104  # from enum ObjectTypeEnum
	kPublicationComponentObject   =134220544  # from enum ObjectTypeEnum
	kPublicationComponentsEnumeratorObject=134220800  # from enum ObjectTypeEnum
	kPublicationComponentsObject  =134220288  # from enum ObjectTypeEnum
	kPublicationEdgeObject        =134224640  # from enum ObjectTypeEnum
	kPublicationEdgesEnumeratorObject=134224384  # from enum ObjectTypeEnum
	kPublicationEventsObject      =50462464   # from enum ObjectTypeEnum
	kPublicationFaceObject        =134223616  # from enum ObjectTypeEnum
	kPublicationFaceShellObject   =134224128  # from enum ObjectTypeEnum
	kPublicationFaceShellsEnumeratorObject=134223872  # from enum ObjectTypeEnum
	kPublicationFacesEnumeratorObject=134223360  # from enum ObjectTypeEnum
	kPublicationMarkedViewObject  =134222592  # from enum ObjectTypeEnum
	kPublicationMarkedViewsObject =134222336  # from enum ObjectTypeEnum
	kPublicationMeshEdgeObject    =134229504  # from enum ObjectTypeEnum
	kPublicationMeshFaceObject    =134229248  # from enum ObjectTypeEnum
	kPublicationObject            =134220032  # from enum ObjectTypeEnum
	kPublicationStageObject       =50461184   # from enum ObjectTypeEnum
	kPublicationTrailObject       =134228224  # from enum ObjectTypeEnum
	kPublicationTrailSegmentObject=134228992  # from enum ObjectTypeEnum
	kPublicationTrailSegmentsEnumeratorObject=134228480  # from enum ObjectTypeEnum
	kPublicationTrailSegmentsObject=134228736  # from enum ObjectTypeEnum
	kPublicationTrailsObject      =134227968  # from enum ObjectTypeEnum
	kPublicationTweakDefinitionObject=134221824  # from enum ObjectTypeEnum
	kPublicationTweakObject       =134222080  # from enum ObjectTypeEnum
	kPublicationTweakPathObject   =134227712  # from enum ObjectTypeEnum
	kPublicationTweakPathsObject  =134227456  # from enum ObjectTypeEnum
	kPublicationTweaksObject      =134221568  # from enum ObjectTypeEnum
	kPublicationVertexObject      =134227200  # from enum ObjectTypeEnum
	kPublicationVerticesEnumeratorObject=134226944  # from enum ObjectTypeEnum
	kPublicationsObject           =134219776  # from enum ObjectTypeEnum
	kPublisherServerObject        =134229760  # from enum ObjectTypeEnum
	kPunchNoteObject              =117488128  # from enum ObjectTypeEnum
	kPunchNotesObject             =117491200  # from enum ObjectTypeEnum
	kPunchToolFeatureObject       =151002368  # from enum ObjectTypeEnum
	kPunchToolFeatureProxyObject  =151005440  # from enum ObjectTypeEnum
	kPunchToolFeaturesObject      =151002112  # from enum ObjectTypeEnum
	kQueryManagerObject           =50410752   # from enum ObjectTypeEnum
	kRadialMarkingMenuObject      =50441984   # from enum ObjectTypeEnum
	kRadialMarkingMenusObject     =50446592   # from enum ObjectTypeEnum
	kRadiusDimConstraint3DObject  =84008704   # from enum ObjectTypeEnum
	kRadiusDimConstraint3DProxyObject=84008816   # from enum ObjectTypeEnum
	kRadiusDimConstraintObject    =83906816   # from enum ObjectTypeEnum
	kRadiusDimConstraintProxyObject=83906928   # from enum ObjectTypeEnum
	kRadiusGeneralDimensionObject =117475072  # from enum ObjectTypeEnum
	kRadiusModelDimensionDefinitionObject=84025856   # from enum ObjectTypeEnum
	kRadiusModelDimensionObject   =84023040   # from enum ObjectTypeEnum
	kRadiusModelDimensionProxyObject=84023152   # from enum ObjectTypeEnum
	kRadiusModelDimensionsObject  =84022272   # from enum ObjectTypeEnum
	kRectangularOccurrencePatternObject=100669440  # from enum ObjectTypeEnum
	kRectangularOccurrencePatternProxyObject=100669568  # from enum ObjectTypeEnum
	kRectangularPatternFeatureDefinitionObject=84058624   # from enum ObjectTypeEnum
	kRectangularPatternFeatureObject=83913728   # from enum ObjectTypeEnum
	kRectangularPatternFeatureProxyObject=83959808   # from enum ObjectTypeEnum
	kRectangularPatternFeaturesObject=83913984   # from enum ObjectTypeEnum
	kReferenceAssetValueObject    =50452224   # from enum ObjectTypeEnum
	kReferenceComponentObject     =83929856   # from enum ObjectTypeEnum
	kReferenceComponentsObject    =83932672   # from enum ObjectTypeEnum
	kReferenceFeatureObject       =83921152   # from enum ObjectTypeEnum
	kReferenceFeatureProxyObject  =83962368   # from enum ObjectTypeEnum
	kReferenceFeaturesEnumeratorObject=83934720   # from enum ObjectTypeEnum
	kReferenceFeaturesObject      =83923456   # from enum ObjectTypeEnum
	kReferenceKeyEventsObject     =50443008   # from enum ObjectTypeEnum
	kReferenceKeyManagerObject    =67128576   # from enum ObjectTypeEnum
	kReferenceParameterObject     =50348800   # from enum ObjectTypeEnum
	kReferenceParametersObject    =50347520   # from enum ObjectTypeEnum
	kReferencedFileDescriptorObject=50337536   # from enum ObjectTypeEnum
	kReferencedFileDescriptorsObject=50337792   # from enum ObjectTypeEnum
	kReferencedOLEFileDescriptorObject=50342400   # from enum ObjectTypeEnum
	kReferencedOLEFileDescriptorsObject=50342656   # from enum ObjectTypeEnum
	kReferencedOpaqueFileDescriptorObject=50456320   # from enum ObjectTypeEnum
	kReferencedOpaqueFileDescriptorsObject=50456576   # from enum ObjectTypeEnum
	kRefoldFeatureObject          =151017216  # from enum ObjectTypeEnum
	kRefoldFeatureProxyObject     =151017728  # from enum ObjectTypeEnum
	kRefoldFeaturesObject         =151017472  # from enum ObjectTypeEnum
	kRegionPropertiesObject       =83992064   # from enum ObjectTypeEnum
	kRenderStyleObject            =50359296   # from enum ObjectTypeEnum
	kRenderStylesObject           =50359040   # from enum ObjectTypeEnum
	kReplaceFaceFeatureObject     =83954688   # from enum ObjectTypeEnum
	kReplaceFaceFeatureProxyObject=83960576   # from enum ObjectTypeEnum
	kReplaceFaceFeaturesObject    =83954944   # from enum ObjectTypeEnum
	kRepresentationEventsObject   =50411264   # from enum ObjectTypeEnum
	kRepresentationsManagerObject =100678400  # from enum ObjectTypeEnum
	kRestFeatureObject            =84003840   # from enum ObjectTypeEnum
	kRestFeatureProxyObject       =84003952   # from enum ObjectTypeEnum
	kRestFeaturesObject           =84004096   # from enum ObjectTypeEnum
	kRevisionTableCellObject      =117469440  # from enum ObjectTypeEnum
	kRevisionTableColumnObject    =117467136  # from enum ObjectTypeEnum
	kRevisionTableColumnsObject   =117466880  # from enum ObjectTypeEnum
	kRevisionTableObject          =117466624  # from enum ObjectTypeEnum
	kRevisionTableRowObject       =117469184  # from enum ObjectTypeEnum
	kRevisionTableRowsObject      =117467392  # from enum ObjectTypeEnum
	kRevisionTableStyleObject     =117494272  # from enum ObjectTypeEnum
	kRevisionTableStylesEnumeratorObject=117494016  # from enum ObjectTypeEnum
	kRevisionTablesObject         =117466368  # from enum ObjectTypeEnum
	kRevolutionAndHeightCoilExtentObject=83931648   # from enum ObjectTypeEnum
	kRevolveFeatureObject         =83914240   # from enum ObjectTypeEnum
	kRevolveFeatureProxyObject    =83960064   # from enum ObjectTypeEnum
	kRevolveFeaturesObject        =83914496   # from enum ObjectTypeEnum
	kRevolvedFaceWorkAxisDefObject=83892224   # from enum ObjectTypeEnum
	kRibDefinitionObject          =84013312   # from enum ObjectTypeEnum
	kRibFeatureObject             =83914752   # from enum ObjectTypeEnum
	kRibFeatureProxyObject        =83960320   # from enum ObjectTypeEnum
	kRibFeaturesObject            =83915008   # from enum ObjectTypeEnum
	kRibbonObject                 =50424320   # from enum ObjectTypeEnum
	kRibbonPanelObject            =50425344   # from enum ObjectTypeEnum
	kRibbonPanelsObject           =50425088   # from enum ObjectTypeEnum
	kRibbonTabObject              =50424832   # from enum ObjectTypeEnum
	kRibbonTabsObject             =50424576   # from enum ObjectTypeEnum
	kRibbonsObject                =50424064   # from enum ObjectTypeEnum
	kRigidBodyGroupObject         =100690432  # from enum ObjectTypeEnum
	kRigidBodyGroupsObject        =100686336  # from enum ObjectTypeEnum
	kRigidBodyJointObject         =100698624  # from enum ObjectTypeEnum
	kRigidBodyJointsObject        =100694528  # from enum ObjectTypeEnum
	kRigidBodyResultsObject       =100682240  # from enum ObjectTypeEnum
	kRipDefinitionObject          =151022592  # from enum ObjectTypeEnum
	kRipFeatureObject             =151020032  # from enum ObjectTypeEnum
	kRipFeatureProxyObject        =151020288  # from enum ObjectTypeEnum
	kRipFeaturesObject            =151020544  # from enum ObjectTypeEnum
	kRolledHemDefinitionObject    =151015168  # from enum ObjectTypeEnum
	kRotateAboutLineMoveOperationObject=84015616   # from enum ObjectTypeEnum
	kRotateRotateConstraintObject =100666624  # from enum ObjectTypeEnum
	kRotateRotateConstraintProxyObject=100676608  # from enum ObjectTypeEnum
	kRotateRotateiMateDefinitionObject=83948032   # from enum ObjectTypeEnum
	kRotateRotateiMateDefinitionProxyObject=83948160   # from enum ObjectTypeEnum
	kRotateTranslateConstraintObject=100666880  # from enum ObjectTypeEnum
	kRotateTranslateConstraintProxyObject=100676864  # from enum ObjectTypeEnum
	kRotateTranslateiMateDefinitionObject=83948288   # from enum ObjectTypeEnum
	kRotateTranslateiMateDefinitionProxyObject=83948416   # from enum ObjectTypeEnum
	kRowObject                    =117462272  # from enum ObjectTypeEnum
	kRowsObject                   =117462016  # from enum ObjectTypeEnum
	kRuleFilletFeatureObject      =84004352   # from enum ObjectTypeEnum
	kRuleFilletFeatureProxyObject =84004464   # from enum ObjectTypeEnum
	kRuleFilletFeaturesObject     =84004608   # from enum ObjectTypeEnum
	kRuledSurfaceDefinitionObject =84050176   # from enum ObjectTypeEnum
	kRuledSurfaceEdgeFacePairObject=84059648   # from enum ObjectTypeEnum
	kRuledSurfaceEdgeFacePairsObject=84059392   # from enum ObjectTypeEnum
	kRuledSurfaceFeatureObject    =84050432   # from enum ObjectTypeEnum
	kRuledSurfaceFeatureProxyObject=84050944   # from enum ObjectTypeEnum
	kRuledSurfaceFeaturesObject   =84050688   # from enum ObjectTypeEnum
	kSaveOptionsObject            =50408960   # from enum ObjectTypeEnum
	kSculptFeatureObject          =83969792   # from enum ObjectTypeEnum
	kSculptFeatureProxyObject     =83970304   # from enum ObjectTypeEnum
	kSculptFeaturesObject         =83970048   # from enum ObjectTypeEnum
	kSculptSurfaceObject          =83976960   # from enum ObjectTypeEnum
	kSearchBoxEventsObject        =50462208   # from enum ObjectTypeEnum
	kSearchBoxObject              =50461952   # from enum ObjectTypeEnum
	kSectionDrawingViewObject     =117463296  # from enum ObjectTypeEnum
	kSelectEventsObject           =50353408   # from enum ObjectTypeEnum
	kSelectSetObject              =50366464   # from enum ObjectTypeEnum
	kSelectionPreferencesObject   =50454016   # from enum ObjectTypeEnum
	kShadedDisplayOptionsObject   =50413056   # from enum ObjectTypeEnum
	kSheetFormatObject            =117482496  # from enum ObjectTypeEnum
	kSheetFormatsObject           =117482240  # from enum ObjectTypeEnum
	kSheetMetalComponentDefinitionObject=150995200  # from enum ObjectTypeEnum
	kSheetMetalFeaturesObject     =150995456  # from enum ObjectTypeEnum
	kSheetMetalStyleObject        =150995968  # from enum ObjectTypeEnum
	kSheetMetalStylesObject       =150995712  # from enum ObjectTypeEnum
	kSheetObject                  =117441280  # from enum ObjectTypeEnum
	kSheetSettingsObject          =50408448   # from enum ObjectTypeEnum
	kSheetsObject                 =117442560  # from enum ObjectTypeEnum
	kShellDefinitionObject        =83963136   # from enum ObjectTypeEnum
	kShellFeatureObject           =83915264   # from enum ObjectTypeEnum
	kShellFeatureProxyObject      =83960832   # from enum ObjectTypeEnum
	kShellFeaturesObject          =83915520   # from enum ObjectTypeEnum
	kShellThicknessFaceSetObject  =83963392   # from enum ObjectTypeEnum
	kShrinkwrapComponentObject    =84072192   # from enum ObjectTypeEnum
	kShrinkwrapComponentProxyObject=84072194   # from enum ObjectTypeEnum
	kShrinkwrapComponentsObject   =84072448   # from enum ObjectTypeEnum
	kShrinkwrapDefinitionObject   =84072704   # from enum ObjectTypeEnum
	kSilhouetteCurveObject        =84012800   # from enum ObjectTypeEnum
	kSilhouetteCurveProxyObject   =84012929   # from enum ObjectTypeEnum
	kSilhouetteCurvesObject       =84013056   # from enum ObjectTypeEnum
	kSimulationComponentObject    =100700416  # from enum ObjectTypeEnum
	kSimulationManagerObject      =100701440  # from enum ObjectTypeEnum
	kSingleHemDefinitionObject    =151014656  # from enum ObjectTypeEnum
	kSinglePointRipTypeDefObject  =151022848  # from enum ObjectTypeEnum
	kSketch3DObject               =83936256   # from enum ObjectTypeEnum
	kSketch3DOptionsObject        =50405888   # from enum ObjectTypeEnum
	kSketch3DProxyObject          =83936368   # from enum ObjectTypeEnum
	kSketch3DSettingsObject       =50383616   # from enum ObjectTypeEnum
	kSketchArc3DObject            =83938304   # from enum ObjectTypeEnum
	kSketchArc3DProxyObject       =83938416   # from enum ObjectTypeEnum
	kSketchArcObject              =83898880   # from enum ObjectTypeEnum
	kSketchArcProxyObject         =83898992   # from enum ObjectTypeEnum
	kSketchArcs3DObject           =83938560   # from enum ObjectTypeEnum
	kSketchArcsObject             =83897344   # from enum ObjectTypeEnum
	kSketchBlockDefinitionObject  =84006400   # from enum ObjectTypeEnum
	kSketchBlockDefinitionProxyObject=84006512   # from enum ObjectTypeEnum
	kSketchBlockDefinitionsEnumeratorObject=84007424   # from enum ObjectTypeEnum
	kSketchBlockDefinitionsObject =84006144   # from enum ObjectTypeEnum
	kSketchBlockObject            =84006912   # from enum ObjectTypeEnum
	kSketchBlockProxyObject       =84007024   # from enum ObjectTypeEnum
	kSketchBlocksEnumeratorObject =84007168   # from enum ObjectTypeEnum
	kSketchBlocksObject           =84006656   # from enum ObjectTypeEnum
	kSketchCircle3DObject         =83939840   # from enum ObjectTypeEnum
	kSketchCircle3DProxyObject    =83939952   # from enum ObjectTypeEnum
	kSketchCircleObject           =83899648   # from enum ObjectTypeEnum
	kSketchCircleProxyObject      =83899760   # from enum ObjectTypeEnum
	kSketchCircles3DObject        =83940864   # from enum ObjectTypeEnum
	kSketchCirclesObject          =83898368   # from enum ObjectTypeEnum
	kSketchConstraintSettingsObject=50453760   # from enum ObjectTypeEnum
	kSketchConstraints3dEnumeratorObject=83941120   # from enum ObjectTypeEnum
	kSketchConstraintsEnumeratorObject=83897088   # from enum ObjectTypeEnum
	kSketchControlPointSpline3DObject=84018432   # from enum ObjectTypeEnum
	kSketchControlPointSpline3DProxyObject=84018544   # from enum ObjectTypeEnum
	kSketchControlPointSplineObject=84017920   # from enum ObjectTypeEnum
	kSketchControlPointSplineProxyObject=84018032   # from enum ObjectTypeEnum
	kSketchControlPointSplines3DObject=84018688   # from enum ObjectTypeEnum
	kSketchControlPointSplinesObject=84018176   # from enum ObjectTypeEnum
	kSketchDrivenPatternDefinitionObject=84058368   # from enum ObjectTypeEnum
	kSketchDrivenPatternFeatureObject=84051712   # from enum ObjectTypeEnum
	kSketchDrivenPatternFeatureProxyObject=84052224   # from enum ObjectTypeEnum
	kSketchDrivenPatternFeaturesObject=84051968   # from enum ObjectTypeEnum
	kSketchEllipse3DObject        =83939328   # from enum ObjectTypeEnum
	kSketchEllipse3DProxyObject   =83939440   # from enum ObjectTypeEnum
	kSketchEllipseObject          =83899392   # from enum ObjectTypeEnum
	kSketchEllipseProxyObject     =83899504   # from enum ObjectTypeEnum
	kSketchEllipses3DObject       =83940352   # from enum ObjectTypeEnum
	kSketchEllipsesObject         =83898112   # from enum ObjectTypeEnum
	kSketchEllipticalArc3DObject  =83939584   # from enum ObjectTypeEnum
	kSketchEllipticalArc3DProxyObject=83939696   # from enum ObjectTypeEnum
	kSketchEllipticalArcObject    =83904768   # from enum ObjectTypeEnum
	kSketchEllipticalArcProxyObject=83904880   # from enum ObjectTypeEnum
	kSketchEllipticalArcs3DObject =83940608   # from enum ObjectTypeEnum
	kSketchEllipticalArcsObject   =83904512   # from enum ObjectTypeEnum
	kSketchEntities3DEnumeratorObject=83937024   # from enum ObjectTypeEnum
	kSketchEntitiesEnumeratorObject=83908096   # from enum ObjectTypeEnum
	kSketchEquationCurve3DObject  =84019456   # from enum ObjectTypeEnum
	kSketchEquationCurve3DProxyObject=84019568   # from enum ObjectTypeEnum
	kSketchEquationCurveObject    =84018944   # from enum ObjectTypeEnum
	kSketchEquationCurveProxyObject=84019056   # from enum ObjectTypeEnum
	kSketchEquationCurves3DObject =84019712   # from enum ObjectTypeEnum
	kSketchEquationCurvesObject   =84019200   # from enum ObjectTypeEnum
	kSketchEventsObject           =50411008   # from enum ObjectTypeEnum
	kSketchFillRegion             =83969280   # from enum ObjectTypeEnum
	kSketchFillRegions            =83969024   # from enum ObjectTypeEnum
	kSketchFixedSpline3DObject    =83964416   # from enum ObjectTypeEnum
	kSketchFixedSpline3DProxyObject=83964528   # from enum ObjectTypeEnum
	kSketchFixedSplineObject      =83963904   # from enum ObjectTypeEnum
	kSketchFixedSplineProxyObject =83964016   # from enum ObjectTypeEnum
	kSketchFixedSplines3DObject   =83964160   # from enum ObjectTypeEnum
	kSketchFixedSplinesObject     =83963648   # from enum ObjectTypeEnum
	kSketchHolePlacementDefinitionObject=83966720   # from enum ObjectTypeEnum
	kSketchImageObject            =83972352   # from enum ObjectTypeEnum
	kSketchImageProxyObject       =83972368   # from enum ObjectTypeEnum
	kSketchImagesObject           =83972096   # from enum ObjectTypeEnum
	kSketchLine3DObject           =83937280   # from enum ObjectTypeEnum
	kSketchLine3DProxyObject      =83937392   # from enum ObjectTypeEnum
	kSketchLineObject             =83896064   # from enum ObjectTypeEnum
	kSketchLineProxyObject        =83896176   # from enum ObjectTypeEnum
	kSketchLines3DObject          =83937536   # from enum ObjectTypeEnum
	kSketchLinesObject            =83896320   # from enum ObjectTypeEnum
	kSketchOffsetSplineObject     =83962624   # from enum ObjectTypeEnum
	kSketchOffsetSplineProxyObject=83962736   # from enum ObjectTypeEnum
	kSketchOffsetSplinesObject    =83962880   # from enum ObjectTypeEnum
	kSketchOptionsObject          =50400000   # from enum ObjectTypeEnum
	kSketchPoint3DObject          =83937792   # from enum ObjectTypeEnum
	kSketchPoint3DProxyObject     =83937904   # from enum ObjectTypeEnum
	kSketchPointObject            =83896576   # from enum ObjectTypeEnum
	kSketchPointProxyObject       =83896688   # from enum ObjectTypeEnum
	kSketchPoints3DObject         =83938048   # from enum ObjectTypeEnum
	kSketchPointsObject           =83896832   # from enum ObjectTypeEnum
	kSketchSettingsObject         =50383360   # from enum ObjectTypeEnum
	kSketchSpline3DObject         =83939072   # from enum ObjectTypeEnum
	kSketchSpline3DProxyObject    =83939184   # from enum ObjectTypeEnum
	kSketchSplineHandle3DObject   =83980032   # from enum ObjectTypeEnum
	kSketchSplineHandle3DProxyObject=83980144   # from enum ObjectTypeEnum
	kSketchSplineHandleObject     =83984128   # from enum ObjectTypeEnum
	kSketchSplineHandleProxyObject=83984240   # from enum ObjectTypeEnum
	kSketchSplineObject           =83899136   # from enum ObjectTypeEnum
	kSketchSplineProxyObject      =83899248   # from enum ObjectTypeEnum
	kSketchSplines3DObject        =83940096   # from enum ObjectTypeEnum
	kSketchSplinesObject          =83897856   # from enum ObjectTypeEnum
	kSketchedSymbolDefinitionLibrariesObject=117496320  # from enum ObjectTypeEnum
	kSketchedSymbolDefinitionLibraryObject=117496576  # from enum ObjectTypeEnum
	kSketchedSymbolDefinitionObject=117448448  # from enum ObjectTypeEnum
	kSketchedSymbolDefinitionsObject=117448192  # from enum ObjectTypeEnum
	kSketchedSymbolObject         =117448704  # from enum ObjectTypeEnum
	kSketchedSymbolsObject        =117449472  # from enum ObjectTypeEnum
	kSketches3DEnumeratorObject   =83997696   # from enum ObjectTypeEnum
	kSketches3DObject             =83936512   # from enum ObjectTypeEnum
	kSketchesEnumeratorObject     =83932416   # from enum ObjectTypeEnum
	kSmoothConstraint3DObject     =83977728   # from enum ObjectTypeEnum
	kSmoothConstraint3DProxyObject=83977840   # from enum ObjectTypeEnum
	kSmoothConstraintObject       =83973376   # from enum ObjectTypeEnum
	kSmoothConstraintProxyObject  =83973488   # from enum ObjectTypeEnum
	kSnapFitFeatureObject         =84004864   # from enum ObjectTypeEnum
	kSnapFitFeatureProxyObject    =84004976   # from enum ObjectTypeEnum
	kSnapFitFeaturesObject        =84005120   # from enum ObjectTypeEnum
	kSoftwareVersionObject        =50345728   # from enum ObjectTypeEnum
	kSolidSweepDefinitionObject   =84075776   # from enum ObjectTypeEnum
	kSpellCheckOptionsObject      =50464000   # from enum ObjectTypeEnum
	kSphereCenterPointWorkPointDefObject=84027392   # from enum ObjectTypeEnum
	kSpiralCoilExtentObject       =83932160   # from enum ObjectTypeEnum
	kSplineFitPointConstraintObject=83900928   # from enum ObjectTypeEnum
	kSplineFitPointConstraintProxyObject=83901040   # from enum ObjectTypeEnum
	kSplineFitPointsConstraint3DObject=83955712   # from enum ObjectTypeEnum
	kSplineFitPointsConstraint3DProxyObject=83955824   # from enum ObjectTypeEnum
	kSplineLengthDimConstraint3DObject=84073728   # from enum ObjectTypeEnum
	kSplineLengthDimConstraint3DProxyObject=84073840   # from enum ObjectTypeEnum
	kSplitFeatureObject           =83915776   # from enum ObjectTypeEnum
	kSplitFeatureProxyObject      =83961088   # from enum ObjectTypeEnum
	kSplitFeaturesObject          =83916032   # from enum ObjectTypeEnum
	kStandardThreadInfoObject     =83920128   # from enum ObjectTypeEnum
	kStoryboardObject             =134221312  # from enum ObjectTypeEnum
	kStoryboardsObject            =134221056  # from enum ObjectTypeEnum
	kStringAssetValueObject       =50451712   # from enum ObjectTypeEnum
	kStyleEventsObject            =50414336   # from enum ObjectTypeEnum
	kStyleObject                  =117478400  # from enum ObjectTypeEnum
	kStylesManagerObject          =50426112   # from enum ObjectTypeEnum
	kStylesObject                 =117478656  # from enum ObjectTypeEnum
	kSurfaceBodiesObject          =67121456   # from enum ObjectTypeEnum
	kSurfaceBodyDefinitionObject  =50435072   # from enum ObjectTypeEnum
	kSurfaceBodyObject            =67118896   # from enum ObjectTypeEnum
	kSurfaceBodyProxyObject       =67119008   # from enum ObjectTypeEnum
	kSurfaceGraphicsEdgeListObject=50418944   # from enum ObjectTypeEnum
	kSurfaceGraphicsEdgeObject    =50419200   # from enum ObjectTypeEnum
	kSurfaceGraphicsFaceListObject=50418432   # from enum ObjectTypeEnum
	kSurfaceGraphicsFaceObject    =50418688   # from enum ObjectTypeEnum
	kSurfaceGraphicsObject        =50417920   # from enum ObjectTypeEnum
	kSurfaceGraphicsVertexListObject=50447104   # from enum ObjectTypeEnum
	kSurfaceGraphicsVertexObject  =50447360   # from enum ObjectTypeEnum
	kSurfaceTextureANSIDefinitionObject=117497088  # from enum ObjectTypeEnum
	kSurfaceTextureBSIDefinitionObject=117497344  # from enum ObjectTypeEnum
	kSurfaceTextureDINDefinitionObject=117497600  # from enum ObjectTypeEnum
	kSurfaceTextureGBDefinitionObject=117497856  # from enum ObjectTypeEnum
	kSurfaceTextureGOSTDefinitionObject=117498112  # from enum ObjectTypeEnum
	kSurfaceTextureISODefinitionObject=117498368  # from enum ObjectTypeEnum
	kSurfaceTextureJISDefinitionObject=117498624  # from enum ObjectTypeEnum
	kSurfaceTextureStyleObject    =117481984  # from enum ObjectTypeEnum
	kSurfaceTextureStylesEnumeratorObject=117481728  # from enum ObjectTypeEnum
	kSurfaceTextureSymbolDefinitionObject=117496832  # from enum ObjectTypeEnum
	kSurfaceTextureSymbolObject   =117484032  # from enum ObjectTypeEnum
	kSurfaceTextureSymbolsObject  =117483776  # from enum ObjectTypeEnum
	kSweepDefinitionObject        =83973632   # from enum ObjectTypeEnum
	kSweepFeatureObject           =83916288   # from enum ObjectTypeEnum
	kSweepFeatureProxyObject      =83961344   # from enum ObjectTypeEnum
	kSweepFeaturesObject          =83916544   # from enum ObjectTypeEnum
	kSweepGraphicsObject          =50414080   # from enum ObjectTypeEnum
	kSymmetryConstraintObject     =83903488   # from enum ObjectTypeEnum
	kSymmetryConstraintProxyObject=83903600   # from enum ObjectTypeEnum
	kTableFormatObject            =117465088  # from enum ObjectTypeEnum
	kTableParameterObject         =50349312   # from enum ObjectTypeEnum
	kTableParametersObject        =50348032   # from enum ObjectTypeEnum
	kTableStyleObject             =117494784  # from enum ObjectTypeEnum
	kTableStylesEnumeratorObject  =117494528  # from enum ObjectTypeEnum
	kTangentConstraint3DObject    =83955968   # from enum ObjectTypeEnum
	kTangentConstraint3DProxyObject=83956080   # from enum ObjectTypeEnum
	kTangentConstraintObject      =100665600  # from enum ObjectTypeEnum
	kTangentConstraintProxyObject =100677120  # from enum ObjectTypeEnum
	kTangentDistanceDimConstraintObject=83907072   # from enum ObjectTypeEnum
	kTangentDistanceDimConstraintProxyObject=83907184   # from enum ObjectTypeEnum
	kTangentSketchConstraintObject=83903744   # from enum ObjectTypeEnum
	kTangentSketchConstraintProxyObject=83903856   # from enum ObjectTypeEnum
	kTangentiMateDefinitionObject =83948544   # from enum ObjectTypeEnum
	kTangentiMateDefinitionProxyObject=83948672   # from enum ObjectTypeEnum
	kTaperedThreadInfoObject      =83920640   # from enum ObjectTypeEnum
	kTeardropHemDefinitionObject  =151014912  # from enum ObjectTypeEnum
	kTextBoxConstraintObject      =83972864   # from enum ObjectTypeEnum
	kTextBoxConstraintProxyObject =83972976   # from enum ObjectTypeEnum
	kTextBoxObject                =117445888  # from enum ObjectTypeEnum
	kTextBoxesObject              =117445632  # from enum ObjectTypeEnum
	kTextGraphicsObject           =50358784   # from enum ObjectTypeEnum
	kTextStyleObject              =117447936  # from enum ObjectTypeEnum
	kTextStylesEnumeratorObject   =117465600  # from enum ObjectTypeEnum
	kTextStylesObject             =117447680  # from enum ObjectTypeEnum
	kTextureAssetValueObject      =50451456   # from enum ObjectTypeEnum
	kTextureCoordinateSetObject   =50405376   # from enum ObjectTypeEnum
	kTextureMapObject             =50404864   # from enum ObjectTypeEnum
	kTextureMapsObject            =50404608   # from enum ObjectTypeEnum
	kThemeManagerObject           =50463232   # from enum ObjectTypeEnum
	kThickenFeatureObject         =83955200   # from enum ObjectTypeEnum
	kThickenFeatureProxyObject    =83961600   # from enum ObjectTypeEnum
	kThickenFeaturesObject        =83955456   # from enum ObjectTypeEnum
	kThreadFeatureObject          =83916800   # from enum ObjectTypeEnum
	kThreadFeatureProxyObject     =83961856   # from enum ObjectTypeEnum
	kThreadFeaturesObject         =83917056   # from enum ObjectTypeEnum
	kThreadInfoObject             =83919872   # from enum ObjectTypeEnum
	kThreadNoteObject             =117487872  # from enum ObjectTypeEnum
	kThreadTableQueryObject       =50411520   # from enum ObjectTypeEnum
	kThreePlanesWorkPointDefObject=83893760   # from enum ObjectTypeEnum
	kThreePointAngleDimConstraintObject=83906304   # from enum ObjectTypeEnum
	kThreePointAngleDimConstraintProxyObject=83906416   # from enum ObjectTypeEnum
	kThreePointsWorkPlaneDefObject=83888128   # from enum ObjectTypeEnum
	kThroughAllExtentObject       =83919616   # from enum ObjectTypeEnum
	kTitleBlockDefinitionObject   =117447168  # from enum ObjectTypeEnum
	kTitleBlockDefinitionsObject  =117446912  # from enum ObjectTypeEnum
	kTitleBlockObject             =117447424  # from enum ObjectTypeEnum
	kToExtentObject               =83918848   # from enum ObjectTypeEnum
	kToHeightExtentObject         =83996160   # from enum ObjectTypeEnum
	kToNextExtentObject           =83919104   # from enum ObjectTypeEnum
	kToleranceObject              =50377984   # from enum ObjectTypeEnum
	kTorusCenterPointWorkPointDefObject=83990784   # from enum ObjectTypeEnum
	kTorusMidPlaneWorkPlaneDefObject=83990528   # from enum ObjectTypeEnum
	kTrailObject                  =134219264  # from enum ObjectTypeEnum
	kTrailSegmentObject           =134219520  # from enum ObjectTypeEnum
	kTrailSegmentsEnumeratorObject=134226432  # from enum ObjectTypeEnum
	kTrailsEnumeratorObject       =134219008  # from enum ObjectTypeEnum
	kTransactionEventsObject      =50342144   # from enum ObjectTypeEnum
	kTransactionManagerObject     =50341376   # from enum ObjectTypeEnum
	kTransactionObject            =50341632   # from enum ObjectTypeEnum
	kTransactionsEnumeratorObject =50341888   # from enum ObjectTypeEnum
	kTransientGeometryObject      =67126912   # from enum ObjectTypeEnum
	kTransitionalConstraintObject =100666112  # from enum ObjectTypeEnum
	kTransitionalConstraintProxyObject=100677376  # from enum ObjectTypeEnum
	kTranslateTranslateConstraintObject=100667136  # from enum ObjectTypeEnum
	kTranslateTranslateConstraintProxyObject=100677888  # from enum ObjectTypeEnum
	kTranslatorAddInObject        =50343936   # from enum ObjectTypeEnum
	kTriadEventsObject            =50392064   # from enum ObjectTypeEnum
	kTriangleFanGraphicsObject    =50358272   # from enum ObjectTypeEnum
	kTriangleGraphicsObject       =50357760   # from enum ObjectTypeEnum
	kTriangleStripGraphicsObject  =50358016   # from enum ObjectTypeEnum
	kTrimFeatureObject            =83974400   # from enum ObjectTypeEnum
	kTrimFeatureProxyObject       =83976448   # from enum ObjectTypeEnum
	kTrimFeaturesObject           =83976192   # from enum ObjectTypeEnum
	kTutorialsManagerObject       =50454528   # from enum ObjectTypeEnum
	kTwoDistancesChamferDefObject =83926016   # from enum ObjectTypeEnum
	kTwoLineAngleDimConstraint3DObject=83971072   # from enum ObjectTypeEnum
	kTwoLineAngleDimConstraint3DProxyObject=83971184   # from enum ObjectTypeEnum
	kTwoLineAngleDimConstraintObject=83906048   # from enum ObjectTypeEnum
	kTwoLineAngleDimConstraintProxyObject=83906160   # from enum ObjectTypeEnum
	kTwoLinesWorkPlaneDefObject   =83888384   # from enum ObjectTypeEnum
	kTwoLinesWorkPointDefObject   =83894016   # from enum ObjectTypeEnum
	kTwoPlanesWorkAxisDefObject   =83891712   # from enum ObjectTypeEnum
	kTwoPlanesWorkPlaneDefObject  =83951872   # from enum ObjectTypeEnum
	kTwoPointDistanceDimConstraint3DObject=83971328   # from enum ObjectTypeEnum
	kTwoPointDistanceDimConstraint3DProxyObject=83971440   # from enum ObjectTypeEnum
	kTwoPointDistanceDimConstraintObject=83905792   # from enum ObjectTypeEnum
	kTwoPointDistanceDimConstraintProxyObject=83905904   # from enum ObjectTypeEnum
	kTwoPointsWorkAxisDefObject   =83891968   # from enum ObjectTypeEnum
	kUnfoldFeatureObject          =151016448  # from enum ObjectTypeEnum
	kUnfoldFeatureProxyObject     =151016960  # from enum ObjectTypeEnum
	kUnfoldFeaturesObject         =151016704  # from enum ObjectTypeEnum
	kUnfoldMethodObject           =150996480  # from enum ObjectTypeEnum
	kUnfoldMethodsObject          =150996224  # from enum ObjectTypeEnum
	kUnitAttributesObject         =117499904  # from enum ObjectTypeEnum
	kUnitsOfMeasureObject         =50346240   # from enum ObjectTypeEnum
	kUnknownObject                =2130706483 # from enum ObjectTypeEnum
	kUnwrapDefinitionObject       =84076800   # from enum ObjectTypeEnum
	kUnwrapFeatureObject          =84076288   # from enum ObjectTypeEnum
	kUnwrapFeatureProxyObject     =84076544   # from enum ObjectTypeEnum
	kUnwrapFeaturesObject         =84076032   # from enum ObjectTypeEnum
	kUserCoordinateSystemDefinitionObject=84010752   # from enum ObjectTypeEnum
	kUserCoordinateSystemObject   =84008192   # from enum ObjectTypeEnum
	kUserCoordinateSystemProxyObject=84008352   # from enum ObjectTypeEnum
	kUserCoordinateSystemSettingsObject=50431232   # from enum ObjectTypeEnum
	kUserCoordinateSystemsObject  =84008448   # from enum ObjectTypeEnum
	kUserInputEventsObject        =50340352   # from enum ObjectTypeEnum
	kUserInterfaceEventsObject    =50402816   # from enum ObjectTypeEnum
	kUserInterfaceManagerObject   =50388224   # from enum ObjectTypeEnum
	kUserParameterObject          =50349056   # from enum ObjectTypeEnum
	kUserParametersObject         =50347776   # from enum ObjectTypeEnum
	kVertexDefinitionObject       =50430464   # from enum ObjectTypeEnum
	kVertexDefinitionsObject      =50430208   # from enum ObjectTypeEnum
	kVertexObject                 =67120432   # from enum ObjectTypeEnum
	kVertexProxyObject            =67120544   # from enum ObjectTypeEnum
	kVerticalAlignConstraintObject=83904256   # from enum ObjectTypeEnum
	kVerticalAlignConstraintProxyObject=83904368   # from enum ObjectTypeEnum
	kVerticalConstraintObject     =83904000   # from enum ObjectTypeEnum
	kVerticalConstraintProxyObject=83904112   # from enum ObjectTypeEnum
	kVerticesObject               =67122992   # from enum ObjectTypeEnum
	kViewListObject               =50389760   # from enum ObjectTypeEnum
	kViewObject                   =50332672   # from enum ObjectTypeEnum
	kViewsEnumeratorObject        =50350080   # from enum ObjectTypeEnum
	kViewsObject                  =50332928   # from enum ObjectTypeEnum
	kVirtualComponentDefinitionObject=100675072  # from enum ObjectTypeEnum
	kVisibleOccurrenceFinderObject=100704768  # from enum ObjectTypeEnum
	kWebBrowserDialogEventsObject =50455808   # from enum ObjectTypeEnum
	kWebBrowserDialogObject       =50455296   # from enum ObjectTypeEnum
	kWebBrowserDialogsObject      =50455552   # from enum ObjectTypeEnum
	kWebBrowserDockableWindowObject=50454272   # from enum ObjectTypeEnum
	kWebViewObject                =50455040   # from enum ObjectTypeEnum
	kWebViewsObject               =50454784   # from enum ObjectTypeEnum
	kWeldBeadObject               =100672768  # from enum ObjectTypeEnum
	kWeldBeadsObject              =100672000  # from enum ObjectTypeEnum
	kWeldObject                   =100672512  # from enum ObjectTypeEnum
	kWeldmentComponentDefinitionObject=100673280  # from enum ObjectTypeEnum
	kWeldsComponentDefinitionObject=100670208  # from enum ObjectTypeEnum
	kWeldsObject                  =100671744  # from enum ObjectTypeEnum
	kWidthOffsetWidthExtentObject =83996928   # from enum ObjectTypeEnum
	kWireDefinitionObject         =50445824   # from enum ObjectTypeEnum
	kWireDefinitionsObject        =50445568   # from enum ObjectTypeEnum
	kWireEdgeDefinitionObject     =50446336   # from enum ObjectTypeEnum
	kWireEdgeDefinitionsObject    =50446080   # from enum ObjectTypeEnum
	kWireObject                   =67131392   # from enum ObjectTypeEnum
	kWireframeDisplayOptionsObject=50412800   # from enum ObjectTypeEnum
	kWiresObject                  =67132160   # from enum ObjectTypeEnum
	kWorkAxesObject               =83890944   # from enum ObjectTypeEnum
	kWorkAxisObject               =83891200   # from enum ObjectTypeEnum
	kWorkAxisProxyObject          =83891360   # from enum ObjectTypeEnum
	kWorkPlaneObject              =83887616   # from enum ObjectTypeEnum
	kWorkPlaneProxyObject         =83887776   # from enum ObjectTypeEnum
	kWorkPlanesObject             =83887872   # from enum ObjectTypeEnum
	kWorkPointObject              =83893504   # from enum ObjectTypeEnum
	kWorkPointProxyObject         =83893664   # from enum ObjectTypeEnum
	kWorkPointsObject             =83893248   # from enum ObjectTypeEnum
	kWorkSurfaceObject            =83945216   # from enum ObjectTypeEnum
	kWorkSurfaceProxyObject       =83945328   # from enum ObjectTypeEnum
	kWorkSurfacesObject           =83945472   # from enum ObjectTypeEnum
	kiAssemblyFactoryObject       =100680960  # from enum ObjectTypeEnum
	kiAssemblyMemberObject        =100680192  # from enum ObjectTypeEnum
	kiAssemblyTableCellObject     =100681216  # from enum ObjectTypeEnum
	kiAssemblyTableColumnObject   =100681728  # from enum ObjectTypeEnum
	kiAssemblyTableColumnsObject  =100681472  # from enum ObjectTypeEnum
	kiAssemblyTableRowObject      =100680704  # from enum ObjectTypeEnum
	kiAssemblyTableRowsObject     =100680448  # from enum ObjectTypeEnum
	kiFeatureComponentObject      =83932928   # from enum ObjectTypeEnum
	kiFeatureComponentsObject     =83933184   # from enum ObjectTypeEnum
	kiFeatureDefinitionObject     =83942912   # from enum ObjectTypeEnum
	kiFeatureEntityInputObject    =83944192   # from enum ObjectTypeEnum
	kiFeatureInputObject          =83943680   # from enum ObjectTypeEnum
	kiFeatureInputsObject         =83943424   # from enum ObjectTypeEnum
	kiFeatureObject               =83998208   # from enum ObjectTypeEnum
	kiFeatureOptionsObject        =50406144   # from enum ObjectTypeEnum
	kiFeatureParameterInputObject =83943936   # from enum ObjectTypeEnum
	kiFeatureProxyObject          =83998320   # from enum ObjectTypeEnum
	kiFeatureSketchPlaneInputObject=83944704   # from enum ObjectTypeEnum
	kiFeatureTableCellObject      =83998464   # from enum ObjectTypeEnum
	kiFeatureTableColumnObject    =83998720   # from enum ObjectTypeEnum
	kiFeatureTableColumnsObject   =83998976   # from enum ObjectTypeEnum
	kiFeatureTableObject          =83999744   # from enum ObjectTypeEnum
	kiFeatureTableRowObject       =83999232   # from enum ObjectTypeEnum
	kiFeatureTableRowsObject      =83999488   # from enum ObjectTypeEnum
	kiFeatureTemplateDescriptorObject=83933952   # from enum ObjectTypeEnum
	kiFeatureTemplateDescriptorsObject=83934208   # from enum ObjectTypeEnum
	kiFeatureVectorInputObject    =83944960   # from enum ObjectTypeEnum
	kiFeatureWorkPlaneInputObject =83944448   # from enum ObjectTypeEnum
	kiFeaturesObject              =83997952   # from enum ObjectTypeEnum
	kiMateDefinitionObject        =83946752   # from enum ObjectTypeEnum
	kiMateDefinitionsEnumeratorObject=83952384   # from enum ObjectTypeEnum
	kiMateDefinitionsObject       =83946496   # from enum ObjectTypeEnum
	kiMateResultObject            =83949312   # from enum ObjectTypeEnum
	kiMateResultProxyObject       =83949321   # from enum ObjectTypeEnum
	kiMateResultsEnumeratorObject =83949568   # from enum ObjectTypeEnum
	kiMateResultsObject           =83949056   # from enum ObjectTypeEnum
	kiPartFactoryObject           =83933440   # from enum ObjectTypeEnum
	kiPartMemberObject            =83933696   # from enum ObjectTypeEnum
	kiPartTableCellObject         =83936000   # from enum ObjectTypeEnum
	kiPartTableColumnObject       =83935232   # from enum ObjectTypeEnum
	kiPartTableColumnsObject      =83934976   # from enum ObjectTypeEnum
	kiPartTableRowObject          =83935744   # from enum ObjectTypeEnum
	kiPartTableRowsObject         =83935488   # from enum ObjectTypeEnum
	kCanIgnoreDegreeOfFreedom     =78082      # from enum OccurrenceDOFStateEnum
	kCanRetainDegreeOfFreedom     =78081      # from enum OccurrenceDOFStateEnum
	kNoDegreeOfFreedomState       =78083      # from enum OccurrenceDOFStateEnum
	kBestImageFidelity            =37380      # from enum OfflineImageFidelityEnum
	kBetterImageFidelity          =37379      # from enum OfflineImageFidelityEnum
	kLowerImageFidelity           =37377      # from enum OfflineImageFidelityEnum
	kStandardImageFidelity        =37378      # from enum OfflineImageFidelityEnum
	kCircularCornerClosure        =96257      # from enum OffsetCornerClosureTypeEnum
	kExtendCornerClosure          =96259      # from enum OffsetCornerClosureTypeEnum
	kLinearCornerClosure          =96258      # from enum OffsetCornerClosureTypeEnum
	kConstrainedOrbit             =86018      # from enum OrbitTypeEnum
	kFreeOrbit                    =86017      # from enum OrbitTypeEnum
	kOrdinateContinuousAlignment  =102145     # from enum OrdinateDimensionAlignmentEnum
	kOrdinateLeaderAligned        =102146     # from enum OrdinateDimensionAlignmentEnum
	kOridateNoAlignment           =102147     # from enum OrdinateDimensionAlignmentEnum
	kApplyDrivenDimension         =50689      # from enum OverConstrainedDimensionBehaviorEnum
	kWarnOfOverConstrainedCondition=50690      # from enum OverConstrainedDimensionBehaviorEnum
	kFullOverflowMenu             =97793      # from enum OverflowMenuBehaviorEnum
	kRadialOnlyOverflowMenu       =97794      # from enum OverflowMenuBehaviorEnum
	kShortOverflowMenu            =97795      # from enum OverflowMenuBehaviorEnum
	kDefaultPageOrientation       =10241      # from enum PageOrientationTypeEnum
	kLandscapePageOrientation     =10242      # from enum PageOrientationTypeEnum
	kPortraitPageOrientation      =10243      # from enum PageOrientationTypeEnum
	kPaperSize10x14               =14337      # from enum PaperSizeEnum
	kPaperSize11x17               =14338      # from enum PaperSizeEnum
	kPaperSizeA0                  =14357      # from enum PaperSizeEnum
	kPaperSizeA0Oversize          =14358      # from enum PaperSizeEnum
	kPaperSizeA1                  =14359      # from enum PaperSizeEnum
	kPaperSizeA1Oversize          =14360      # from enum PaperSizeEnum
	kPaperSizeA2                  =14339      # from enum PaperSizeEnum
	kPaperSizeA2Oversize          =14361      # from enum PaperSizeEnum
	kPaperSizeA3                  =14340      # from enum PaperSizeEnum
	kPaperSizeA4                  =14341      # from enum PaperSizeEnum
	kPaperSizeA4Small             =14342      # from enum PaperSizeEnum
	kPaperSizeA5                  =14343      # from enum PaperSizeEnum
	kPaperSizeA6                  =14365      # from enum PaperSizeEnum
	kPaperSizeB0                  =14366      # from enum PaperSizeEnum
	kPaperSizeB1                  =14362      # from enum PaperSizeEnum
	kPaperSizeB2                  =14363      # from enum PaperSizeEnum
	kPaperSizeB3                  =14364      # from enum PaperSizeEnum
	kPaperSizeB4                  =14344      # from enum PaperSizeEnum
	kPaperSizeB5                  =14345      # from enum PaperSizeEnum
	kPaperSizeB6                  =14367      # from enum PaperSizeEnum
	kPaperSizeCSheet              =14346      # from enum PaperSizeEnum
	kPaperSizeCustom              =14355      # from enum PaperSizeEnum
	kPaperSizeDSheet              =14347      # from enum PaperSizeEnum
	kPaperSizeDefault             =14356      # from enum PaperSizeEnum
	kPaperSizeESheet              =14348      # from enum PaperSizeEnum
	kPaperSizeExecutive           =14349      # from enum PaperSizeEnum
	kPaperSizeFolio               =14350      # from enum PaperSizeEnum
	kPaperSizeLedger              =14351      # from enum PaperSizeEnum
	kPaperSizeLegal               =14352      # from enum PaperSizeEnum
	kPaperSizeLetter              =14353      # from enum PaperSizeEnum
	kPaperSizeQuarto              =14354      # from enum PaperSizeEnum
	kArchitecturalDisplayFormat   =92419      # from enum ParameterDisplayFormatEnum
	kDecimalDisplayFormat         =92417      # from enum ParameterDisplayFormatEnum
	kFractionalDisplayFormat      =92418      # from enum ParameterDisplayFormatEnum
	kDerivedParameter             =11525      # from enum ParameterTypeEnum
	kModelParameter               =11521      # from enum ParameterTypeEnum
	kReferenceParameter           =11522      # from enum ParameterTypeEnum
	kTableParameter               =11523      # from enum ParameterTypeEnum
	kUserParameter                =11524      # from enum ParameterTypeEnum
	kNegativeExtentDirection      =20994      # from enum PartFeatureExtentDirectionEnum
	kPositiveExtentDirection      =20993      # from enum PartFeatureExtentDirectionEnum
	kSymmetricExtentDirection     =20995      # from enum PartFeatureExtentDirectionEnum
	kAngleExtent                  =20738      # from enum PartFeatureExtentEnum
	kCenteredWidthExtent          =20755      # from enum PartFeatureExtentEnum
	kCutAcrossBendsExtent         =20756      # from enum PartFeatureExtentEnum
	kDistanceExtent               =20737      # from enum PartFeatureExtentEnum
	kDistanceFromFaceExtent       =20757      # from enum PartFeatureExtentEnum
	kEdgeWidthExtent              =20751      # from enum PartFeatureExtentEnum
	kFlangeDistanceExtent         =20748      # from enum PartFeatureExtentEnum
	kFlangeLegacyDistanceExtent   =20750      # from enum PartFeatureExtentEnum
	kFlangeToExtent               =20749      # from enum PartFeatureExtentEnum
	kFromToExtent                 =20742      # from enum PartFeatureExtentEnum
	kFromToWidthExtent            =20754      # from enum PartFeatureExtentEnum
	kFullSweepExtent              =20739      # from enum PartFeatureExtentEnum
	kOffsetWidthExtent            =20753      # from enum PartFeatureExtentEnum
	kPitchAndHeightCoilExtent     =20746      # from enum PartFeatureExtentEnum
	kPitchAndRevolutionCoilExtent =20744      # from enum PartFeatureExtentEnum
	kRevolutionAndHeightCoilExtent=20745      # from enum PartFeatureExtentEnum
	kSpiralCoilExtent             =20747      # from enum PartFeatureExtentEnum
	kThroughAllExtent             =20743      # from enum PartFeatureExtentEnum
	kToExtent                     =20741      # from enum PartFeatureExtentEnum
	kToNextExtent                 =20740      # from enum PartFeatureExtentEnum
	kWidthOffsetWidthExtent       =20752      # from enum PartFeatureExtentEnum
	kCutOperation                 =20482      # from enum PartFeatureOperationEnum
	kIntersectOperation           =20483      # from enum PartFeatureOperationEnum
	kJoinOperation                =20481      # from enum PartFeatureOperationEnum
	kNewBodyOperation             =20485      # from enum PartFeatureOperationEnum
	kSurfaceOperation             =20484      # from enum PartFeatureOperationEnum
	kChamferDistanceDirvenDimensionType=115201     # from enum PartialChamferDrivenDimensionTypeEnum
	kEndDistanceDirvenDimensionType=115203     # from enum PartialChamferDrivenDimensionTypeEnum
	kStartDistanceDirvenDimensionType=115202     # from enum PartialChamferDrivenDimensionTypeEnum
	kMicrosoftAccess              =48641      # from enum PartsListFileFormatEnum
	kMicrosoftExcel               =48642      # from enum PartsListFileFormatEnum
	kTextFileCommaDelimited       =48647      # from enum PartsListFileFormatEnum
	kTextFileTabDelimited         =48646      # from enum PartsListFileFormatEnum
	kUnicodeTextFileCommaDelimited=48649      # from enum PartsListFileFormatEnum
	kUnicodeTextFileTabDelimited  =48648      # from enum PartsListFileFormatEnum
	kdBASEIII                     =48643      # from enum PartsListFileFormatEnum
	kdBASEIV                      =48644      # from enum PartsListFileFormatEnum
	kFirstLevelComponents         =46593      # from enum PartsListLevelEnum
	kPartsOnly                    =46594      # from enum PartsListLevelEnum
	kStructured                   =46593      # from enum PartsListLevelEnum
	kStructuredAllLevels          =46595      # from enum PartsListLevelEnum
	kAdjustToModelCompute         =47362      # from enum PatternComputeTypeEnum
	kIdenticalCompute             =47361      # from enum PatternComputeTypeEnum
	kOptimizedCompute             =47363      # from enum PatternComputeTypeEnum
	kAdjustToDirection1           =33794      # from enum PatternOrientationEnum
	kAdjustToDirection2           =33795      # from enum PatternOrientationEnum
	kIdentical                    =33793      # from enum PatternOrientationEnum
	kFittedPositioningMethod      =113409     # from enum PatternPositioningMethodEnum
	kIncrementalPositioningMethod =113410     # from enum PatternPositioningMethodEnum
	kDefault                      =33537      # from enum PatternSpacingTypeEnum
	kFitToPathLength              =33539      # from enum PatternSpacingTypeEnum
	kFitted                       =33538      # from enum PatternSpacingTypeEnum
	kPhysicalModelArea            =72450      # from enum PhysicalPropertyEnum
	kPhysicalModelDensity         =72452      # from enum PhysicalPropertyEnum
	kPhysicalModelMass            =72449      # from enum PhysicalPropertyEnum
	kPhysicalModelVolume          =72451      # from enum PhysicalPropertyEnum
	kPtAtIntersection             =22273      # from enum PointInferenceEnum
	kPtAtMidPoint                 =22276      # from enum PointInferenceEnum
	kPtOnCurve                    =22274      # from enum PointInferenceEnum
	kPtOnPt                       =22275      # from enum PointInferenceEnum
	kAxisEndPointIntent           =57867      # from enum PointIntentEnum
	kAxisMidPointIntent           =57866      # from enum PointIntentEnum
	kAxisStartPointIntent         =57865      # from enum PointIntentEnum
	kBottomLeftPointIntent        =57872      # from enum PointIntentEnum
	kBottomMiddlePointIntent      =57873      # from enum PointIntentEnum
	kBottomRightPointIntent       =57874      # from enum PointIntentEnum
	kCenterPointIntent            =57860      # from enum PointIntentEnum
	kCircularBottomPointIntent    =57864      # from enum PointIntentEnum
	kCircularLeftPointIntent      =57861      # from enum PointIntentEnum
	kCircularRightPointIntent     =57862      # from enum PointIntentEnum
	kCircularTopPointIntent       =57863      # from enum PointIntentEnum
	kEndPointIntent               =57858      # from enum PointIntentEnum
	kLeftMiddlePointIntent        =57875      # from enum PointIntentEnum
	kMidPointIntent               =57859      # from enum PointIntentEnum
	kPlanarFaceCenterPointIntent  =57868      # from enum PointIntentEnum
	kRightMiddlePointIntent       =57876      # from enum PointIntentEnum
	kStartPointIntent             =57857      # from enum PointIntentEnum
	kTopLeftPointIntent           =57869      # from enum PointIntentEnum
	kTopMiddlePointIntent         =57870      # from enum PointIntentEnum
	kTopRightPointIntent          =57871      # from enum PointIntentEnum
	kCirclePointStyle             =20226      # from enum PointRenderStyleEnum
	kCrossPointStyle              =20230      # from enum PointRenderStyleEnum
	kCustomImagePointStyle        =20235      # from enum PointRenderStyleEnum
	kDimCircularPointStyle        =20227      # from enum PointRenderStyleEnum
	kEndPointStyle                =20234      # from enum PointRenderStyleEnum
	kFilledCirclePointStyle       =20228      # from enum PointRenderStyleEnum
	kFilledCircleSelectPointStyle =20229      # from enum PointRenderStyleEnum
	kFilledCrossPointStyle        =20231      # from enum PointRenderStyleEnum
	kNoSnapPointStyle             =20233      # from enum PointRenderStyleEnum
	kOnCurvePointStyle            =20232      # from enum PointRenderStyleEnum
	kXPointStyle                  =20225      # from enum PointRenderStyleEnum
	kAboveAndBelow                =42498      # from enum PrefixAndSuffixOrderEnum
	kBeforeAndAfter               =42497      # from enum PrefixAndSuffixOrderEnum
	kPrintColorPalette            =13313      # from enum PrintColorModeEnum
	kPrintDefaultColorMode        =13315      # from enum PrintColorModeEnum
	kPrintGrayScale               =13314      # from enum PrintColorModeEnum
	kDefaultOrientation           =13571      # from enum PrintOrientationEnum
	kLandscapeOrientation         =13570      # from enum PrintOrientationEnum
	kPortraitOrientation          =13569      # from enum PrintOrientationEnum
	kPrintAllSheets               =14082      # from enum PrintRangeEnum
	kPrintCurrentSheet            =14081      # from enum PrintRangeEnum
	kPrintSheetRange              =14083      # from enum PrintRangeEnum
	kPrintBestFitScale            =13826      # from enum PrintScaleModeEnum
	kPrintCurrentWindow           =13828      # from enum PrintScaleModeEnum
	kPrintCustomScale             =13827      # from enum PrintScaleModeEnum
	kPrintFullScale               =13825      # from enum PrintScaleModeEnum
	kCommandNameEvent             =6661       # from enum PrivateEventTypeEnum
	kDimensionEvent               =6659       # from enum PrivateEventTypeEnum
	kFileNameEvent                =6657       # from enum PrivateEventTypeEnum
	kNameEvent                    =6658       # from enum PrivateEventTypeEnum
	kStringEvent                  =6660       # from enum PrivateEventTypeEnum
	kProductEditionInventor       =76551      # from enum ProductEditionEnum
	kProductEditionInventorFactoryAdvanced=76553      # from enum ProductEditionEnum
	kProductEditionInventorFactoryPremium=76552      # from enum ProductEditionEnum
	kProductEditionInventorFactoryUltimate=76553      # from enum ProductEditionEnum
	kProductEditionInventorLT     =76545      # from enum ProductEditionEnum
	kProductEditionInventorOEM    =76554      # from enum ProductEditionEnum
	kProductEditionInventorProfessional=76547      # from enum ProductEditionEnum
	kProductEditionInventorRO     =76555      # from enum ProductEditionEnum
	kProductEditionInventorRoutedSystems=76548      # from enum ProductEditionEnum
	kProductEditionInventorSimulation=76549      # from enum ProductEditionEnum
	kProductEditionInventorSuite  =76546      # from enum ProductEditionEnum
	kProductEditionInventorTooling=76550      # from enum ProductEditionEnum
	kOrthographicProjection       =86273      # from enum ProjectionTypeEnum
	kPerspectiveProjection        =86274      # from enum ProjectionTypeEnum
	kDontAllowButton1NeverAgain   =8          # from enum PromptMessageRestrictionsEnum
	kDontAllowButton1NoMoreThisSession=16         # from enum PromptMessageRestrictionsEnum
	kDontAllowButton2NeverAgain   =64         # from enum PromptMessageRestrictionsEnum
	kDontAllowButton2NoMoreThisSession=128        # from enum PromptMessageRestrictionsEnum
	kDontAllowButton3NeverAgain   =512        # from enum PromptMessageRestrictionsEnum
	kDontAllowButton3NoMoreThisSession=1024       # from enum PromptMessageRestrictionsEnum
	kDontAllowNeverAgain          =1          # from enum PromptMessageRestrictionsEnum
	kDontAllowNoMoreThisSession   =2          # from enum PromptMessageRestrictionsEnum
	kNoRestrictions               =0          # from enum PromptMessageRestrictionsEnum
	kAuthoringToolContentLibrary  =11         # from enum PropertiesForContentLibraryEnum
	kComponentTypeContentLibrary  =3          # from enum PropertiesForContentLibraryEnum
	kDomainCategoriesContentLibrary=13         # from enum PropertiesForContentLibraryEnum
	kFamilyContentLibrary         =6          # from enum PropertiesForContentLibraryEnum
	kFamilyIdContentLibrary       =17         # from enum PropertiesForContentLibraryEnum
	kFamilyReviesionTimeContentLibrary=18         # from enum PropertiesForContentLibraryEnum
	kFamilyRevisionContentLibrary =9          # from enum PropertiesForContentLibraryEnum
	kFamilyfolderContentLibrary   =19         # from enum PropertiesForContentLibraryEnum
	kLibraryContentLibrary        =4          # from enum PropertiesForContentLibraryEnum
	kLibraryIdContentLibrary      =10         # from enum PropertiesForContentLibraryEnum
	kLibraryLocationContentLibrary=2          # from enum PropertiesForContentLibraryEnum
	kMemberContentLibrary         =7          # from enum PropertiesForContentLibraryEnum
	kMemberFileNameContentLibrary =21         # from enum PropertiesForContentLibraryEnum
	kMemberIdContentLibrary       =20         # from enum PropertiesForContentLibraryEnum
	kMemberRevisionContentLibrary =8          # from enum PropertiesForContentLibraryEnum
	kSizeDesignationContentLibrary=12         # from enum PropertiesForContentLibraryEnum
	kUserCategoriesContentLibrary =15         # from enum PropertiesForContentLibraryEnum
	k_MonikerContentLibrary       =16         # from enum PropertiesForContentLibraryEnum
	k_PropertySetSchemaRevisionContentLibrary=14         # from enum PropertiesForContentLibraryEnum
	k_SubLibraryContentLibrary    =5          # from enum PropertiesForContentLibraryEnum
	kCheckInByDesignTrackingControl=7          # from enum PropertiesForDesignTrackingControlEnum
	kCheckInDateDesignTrackingControl=8          # from enum PropertiesForDesignTrackingControlEnum
	kCheckOutVersionDesignTrackingControls=12         # from enum PropertiesForDesignTrackingControlEnum
	kCheckOutWorkGroupDesignTrackingControl=9          # from enum PropertiesForDesignTrackingControlEnum
	kCheckOutWorkSpaceDesignTrackingControl=11         # from enum PropertiesForDesignTrackingControlEnum
	kCheckedOutByDesignTrackingControl=5          # from enum PropertiesForDesignTrackingControlEnum
	kCheckedOutDateDesignTrackingControl=6          # from enum PropertiesForDesignTrackingControlEnum
	kCurrentVersionDesignTrackingControl=14         # from enum PropertiesForDesignTrackingControlEnum
	kDrawingDeferUpdateDesignTrackingControl=19         # from enum PropertiesForDesignTrackingControlEnum
	kLastSavedByDesignTrackingControl=16         # from enum PropertiesForDesignTrackingControlEnum
	kLastSavedDateDesignTrackingControl=17         # from enum PropertiesForDesignTrackingControlEnum
	kNextVersionDesignTrackingControl=13         # from enum PropertiesForDesignTrackingControlEnum
	kPreviousVersionDesignTrackingControl=15         # from enum PropertiesForDesignTrackingControlEnum
	kAppearanceDesignTrackingProperties=72         # from enum PropertiesForDesignTrackingPropertiesEnum
	kAuthorityDesignTrackingProperties=43         # from enum PropertiesForDesignTrackingPropertiesEnum
	kCatalogWebLinkDesignTrackingProperties=23         # from enum PropertiesForDesignTrackingPropertiesEnum
	kCategoriesDesignTrackingProperties=56         # from enum PropertiesForDesignTrackingPropertiesEnum
	kCheckedByDesignTrackingProperties=10         # from enum PropertiesForDesignTrackingPropertiesEnum
	kCostCenterDesignTrackingProperties=9          # from enum PropertiesForDesignTrackingPropertiesEnum
	kCostDesignTrackingProperties =36         # from enum PropertiesForDesignTrackingPropertiesEnum
	kCreationDateDesignTrackingProperties=4          # from enum PropertiesForDesignTrackingPropertiesEnum
	kDateCheckedDesignTrackingProperties=11         # from enum PropertiesForDesignTrackingPropertiesEnum
	kDateEngrApprovedDesignTrackingProperties=13         # from enum PropertiesForDesignTrackingPropertiesEnum
	kDateMfgApprovedDesignTrackingProperties=35         # from enum PropertiesForDesignTrackingPropertiesEnum
	kDensityDesignTrackingProperties=61         # from enum PropertiesForDesignTrackingPropertiesEnum
	kDescriptionDesignTrackingProperties=29         # from enum PropertiesForDesignTrackingPropertiesEnum
	kDesignStatusDesignTrackingProperties=40         # from enum PropertiesForDesignTrackingPropertiesEnum
	kDesignerDesignTrackingProperties=41         # from enum PropertiesForDesignTrackingPropertiesEnum
	kDocSubTypeDesignTrackingProperties=31         # from enum PropertiesForDesignTrackingPropertiesEnum
	kDocSubTypeNameDesignTrackingProperties=32         # from enum PropertiesForDesignTrackingPropertiesEnum
	kDrawingDeferUpdateDesignTrackingProperties=51         # from enum PropertiesForDesignTrackingPropertiesEnum
	kEngineerDesignTrackingProperties=42         # from enum PropertiesForDesignTrackingPropertiesEnum
	kEngrApprovedByDesignTrackingProperties=12         # from enum PropertiesForDesignTrackingPropertiesEnum
	kExternalPropRevIdDesignTrackingProperties=46         # from enum PropertiesForDesignTrackingPropertiesEnum
	kFlatPatternDeferUpdateDesignTrackingProperties=73         # from enum PropertiesForDesignTrackingPropertiesEnum
	kFlatPatternExtentsAreaDesignTrackingProperties=65         # from enum PropertiesForDesignTrackingPropertiesEnum
	kFlatPatternExtentsLengthDesignTrackingProperties=64         # from enum PropertiesForDesignTrackingPropertiesEnum
	kFlatPatternExtentsWidthDesignTrackingProperties=63         # from enum PropertiesForDesignTrackingPropertiesEnum
	kLanguageDesignTrackingProperties=50         # from enum PropertiesForDesignTrackingPropertiesEnum
	kLastUpdatedWithDesignTrackingProperties=67         # from enum PropertiesForDesignTrackingPropertiesEnum
	kManufacturerDesignTrackingProperties=48         # from enum PropertiesForDesignTrackingPropertiesEnum
	kMassDesignTrackingProperties =58         # from enum PropertiesForDesignTrackingPropertiesEnum
	kMaterialDesignTrackingProperties=20         # from enum PropertiesForDesignTrackingPropertiesEnum
	kMaterialIdentifierDesignTrackingProperties=71         # from enum PropertiesForDesignTrackingPropertiesEnum
	kMfgApprovedByDesignTrackingProperties=34         # from enum PropertiesForDesignTrackingPropertiesEnum
	kParameterizedTemplateDesignTrackingProperties=44         # from enum PropertiesForDesignTrackingPropertiesEnum
	kPartIconDesignTrackingProperties=28         # from enum PropertiesForDesignTrackingPropertiesEnum
	kPartNumberDesignTrackingProperties=5          # from enum PropertiesForDesignTrackingPropertiesEnum
	kPartPropRevIdDesignTrackingProperties=21         # from enum PropertiesForDesignTrackingPropertiesEnum
	kProjectDesignTrackingProperties=7          # from enum PropertiesForDesignTrackingPropertiesEnum
	kProxyRefreshDateDesignTrackingProperties=33         # from enum PropertiesForDesignTrackingPropertiesEnum
	kSheetMetalRuleDesignTrackingProperties=66         # from enum PropertiesForDesignTrackingPropertiesEnum
	kStandardDesignTrackingProperties=37         # from enum PropertiesForDesignTrackingPropertiesEnum
	kStandardRevisionDesignTrackingProperties=47         # from enum PropertiesForDesignTrackingPropertiesEnum
	kStandardsOrganizationDesignTrackingProperties=49         # from enum PropertiesForDesignTrackingPropertiesEnum
	kStockNumberDesignTrackingProperties=55         # from enum PropertiesForDesignTrackingPropertiesEnum
	kSurfaceAreaDesignTrackingProperties=59         # from enum PropertiesForDesignTrackingPropertiesEnum
	kTemplateRowDesignTrackingProperties=45         # from enum PropertiesForDesignTrackingPropertiesEnum
	kUserStatusDesignTrackingProperties=17         # from enum PropertiesForDesignTrackingPropertiesEnum
	kValidMassPropsDesignTrackingProperties=62         # from enum PropertiesForDesignTrackingPropertiesEnum
	kVendorDesignTrackingProperties=30         # from enum PropertiesForDesignTrackingPropertiesEnum
	kVolumeDesignTrackingProperties=60         # from enum PropertiesForDesignTrackingPropertiesEnum
	kWeldMaterialDesignTrackingProperties=57         # from enum PropertiesForDesignTrackingPropertiesEnum
	kCategoryDocSummaryInformation=2          # from enum PropertiesForDocSummaryInformationEnum
	kCompanyDocSummaryInformation =15         # from enum PropertiesForDocSummaryInformationEnum
	kManagerDocSummaryInformation =14         # from enum PropertiesForDocSummaryInformationEnum
	kAuthorSummaryInformation     =4          # from enum PropertiesForSummaryInformationEnum
	kCommentsSummaryInformation   =6          # from enum PropertiesForSummaryInformationEnum
	kCreationTimeSummaryInformation=12         # from enum PropertiesForSummaryInformationEnum
	kKeywordsSummaryInformation   =5          # from enum PropertiesForSummaryInformationEnum
	kLastSavedBySummaryInformation=8          # from enum PropertiesForSummaryInformationEnum
	kRevisionSummaryInformation   =9          # from enum PropertiesForSummaryInformationEnum
	kSubjectSummaryInformation    =3          # from enum PropertiesForSummaryInformationEnum
	kThumbnailSummaryInformation  =17         # from enum PropertiesForSummaryInformationEnum
	kTitleSummaryInformation      =2          # from enum PropertiesForSummaryInformationEnum
	kDummyUserDefinedProperties   =0          # from enum PropertiesForUserDefinedPropertiesEnum
	kAngleDisplayPrecision_PrivateModelInformation=13         # from enum PropertiesFor_PrivateModelInformationEnum
	kAngleUnits_PrivateModelInformation=9          # from enum PropertiesFor_PrivateModelInformationEnum
	kAssemblyAvailablePvs_PrivateModelInformation=15         # from enum PropertiesFor_PrivateModelInformationEnum
	kCompacted_PrivateModelInformation=14         # from enum PropertiesFor_PrivateModelInformationEnum
	kLengthDisplayPrecision_PrivateModelInformation=12         # from enum PropertiesFor_PrivateModelInformationEnum
	kLengthUnits_PrivateModelInformation=8          # from enum PropertiesFor_PrivateModelInformationEnum
	kMassUnits_PrivateModelInformation=11         # from enum PropertiesFor_PrivateModelInformationEnum
	kPartActiveColorStyle_PrivateModelInformation=16         # from enum PropertiesFor_PrivateModelInformationEnum
	kTimeUnits_PrivateModelInformation=10         # from enum PropertiesFor_PrivateModelInformationEnum
	kBaseQuantityPartsListProperty=45576      # from enum PropertyTypeEnum
	kBaseUnitPartsListProperty    =45577      # from enum PropertyTypeEnum
	kCustomProperty               =45570      # from enum PropertyTypeEnum
	kFileProperty                 =45569      # from enum PropertyTypeEnum
	kFilenamePartsListProperty    =45571      # from enum PropertyTypeEnum
	kItemPartsListProperty        =45572      # from enum PropertyTypeEnum
	kItemQuantityPartsListProperty=45578      # from enum PropertyTypeEnum
	kMassPartsListProperty        =45573      # from enum PropertyTypeEnum
	kMaterialPartsListProperty    =45574      # from enum PropertyTypeEnum
	kQuantityPartsListProperty    =45575      # from enum PropertyTypeEnum
	kUnitQuantityPartsListProperty=45579      # from enum PropertyTypeEnum
	kVolumePartsListProperty      =45580      # from enum PropertyTypeEnum
	kAllComponentsTrailsDisplay   =111364     # from enum PublicationTweakTrailsDisplayEnum
	kAllPartsTrailsDisplay        =111363     # from enum PublicationTweakTrailsDisplayEnum
	kNoneTrailsDisplay            =111361     # from enum PublicationTweakTrailsDisplayEnum
	kSingleTrailDisplay           =111362     # from enum PublicationTweakTrailsDisplayEnum
	kNumberOfLikePunchesInFeature =83713      # from enum PunchNoteQuantityEnum
	kNumberOfLikePunchesInModel   =83714      # from enum PunchNoteQuantityEnum
	k2DSketchAndCenterMarkPunchRepresentation=64517      # from enum PunchRepresentationTypeEnum
	k2DSketchPunchRepresentation  =64515      # from enum PunchRepresentationTypeEnum
	kCentermarkPunchRepresentation=64516      # from enum PunchRepresentationTypeEnum
	kDefaultPunchRepresentation   =64513      # from enum PunchRepresentationTypeEnum
	kFormedFeaturePunchRepresentation=64514      # from enum PunchRepresentationTypeEnum
	kBestRayTracingQuality        =95747      # from enum RayTracingQualityEnum
	kDraftRayTracingQuality       =95749      # from enum RayTracingQualityEnum
	kGoodRayTracingQuality        =95746      # from enum RayTracingQualityEnum
	kHighRayTracingQuality        =95750      # from enum RayTracingQualityEnum
	kInteractiveRayTracingQuality =95745      # from enum RayTracingQualityEnum
	kLowRayTracingQuality         =95748      # from enum RayTracingQualityEnum
	kMonitorAndEnableUpdate       =90626      # from enum ReferenceMonitoringEnum
	kNoMonitor                    =90625      # from enum ReferenceMonitoringEnum
	kMissingReference             =49668      # from enum ReferenceStatusEnum
	kOutOfDateReference           =49667      # from enum ReferenceStatusEnum
	kReplacedReference            =49669      # from enum ReferenceStatusEnum
	kUnknownReference             =49665      # from enum ReferenceStatusEnum
	kUpToDateReference            =49666      # from enum ReferenceStatusEnum
	kRelationshipAngleValue       =103169     # from enum RelationshipValueTypeEnum
	kRelationshipAngularPositionValue=103173     # from enum RelationshipValueTypeEnum
	kRelationshipGapValue         =103170     # from enum RelationshipValueTypeEnum
	kRelationshipLinearPositionValue=103171     # from enum RelationshipValueTypeEnum
	kRelationshipOffsetValue      =103172     # from enum RelationshipValueTypeEnum
	kEmbeddedReport               =107778     # from enum ReportLocationEnum
	kExternalReport               =107779     # from enum ReportLocationEnum
	kNoReport                     =107777     # from enum ReportLocationEnum
	kRevisionTableCustomProperty  =89346      # from enum RevisionTablePropertyEnum
	kRevisionTableDateProperty    =89347      # from enum RevisionTablePropertyEnum
	kRevisionTableFileProperty    =89345      # from enum RevisionTablePropertyEnum
	kRevisionTableLtrProperty     =89351      # from enum RevisionTablePropertyEnum
	kRevisionTableSheetProperty   =89348      # from enum RevisionTablePropertyEnum
	kRevisionTableZoneProperty    =89349      # from enum RevisionTablePropertyEnum
	kRevisionTableZoneSheetProperty=89350      # from enum RevisionTablePropertyEnum
	kCircularRevisionTag          =89089      # from enum RevisionTagShapeEnum
	kHexagonRevisionTag           =89090      # from enum RevisionTagShapeEnum
	kSquareRevisionTag            =89091      # from enum RevisionTagShapeEnum
	kTriangularRevisionTag        =89092      # from enum RevisionTagShapeEnum
	kFiniteRibExtent              =93697      # from enum RibFeatureExtentEnum
	kToNextRibExtent              =93698      # from enum RibFeatureExtentEnum
	kRibThicknessAtRoot           =93954      # from enum RibThicknessPlaneEnum
	kRibThicknessAtSketchPlane    =93953      # from enum RibThicknessPlaneEnum
	kAllTextOff                   =82946      # from enum RibbonAppearanceEnum
	kCompact                      =82948      # from enum RibbonAppearanceEnum
	kLarge                        =82949      # from enum RibbonAppearanceEnum
	kNormal                       =82945      # from enum RibbonAppearanceEnum
	kSmall                        =82947      # from enum RibbonAppearanceEnum
	kDockToLeft                   =85763      # from enum RibbonDockingStateEnum
	kDockToRight                  =85764      # from enum RibbonDockingStateEnum
	kDockToTop                    =85762      # from enum RibbonDockingStateEnum
	kFloating                     =85761      # from enum RibbonDockingStateEnum
	kFullRibbon                   =83201      # from enum RibbonStateEnum
	kMinimizeToPanelButtons       =83204      # from enum RibbonStateEnum
	kMinimizeToPanelTitles        =83203      # from enum RibbonStateEnum
	kMinimizeToTabs               =83202      # from enum RibbonStateEnum
	kAngleVectorVectorJoint       =68097      # from enum RigidBodyJointTypeEnum
	kConCentricCircleCircleJoint  =68109      # from enum RigidBodyJointTypeEnum
	kDistanceLineLineJoint        =68113      # from enum RigidBodyJointTypeEnum
	kDistanceLinePlaneJoint       =68114      # from enum RigidBodyJointTypeEnum
	kDistancePlanePlaneJoint      =68115      # from enum RigidBodyJointTypeEnum
	kDistancePointLineJoint       =68111      # from enum RigidBodyJointTypeEnum
	kDistancePointPlaneJoint      =68112      # from enum RigidBodyJointTypeEnum
	kDistancePointPointJoint      =68110      # from enum RigidBodyJointTypeEnum
	kEqualDistancePlanePlaneJoint =68117      # from enum RigidBodyJointTypeEnum
	kEqualDistancePointPlaneJoint =68116      # from enum RigidBodyJointTypeEnum
	kGearJoint                    =68138      # from enum RigidBodyJointTypeEnum
	kMateConeConeJoint            =68104      # from enum RigidBodyJointTypeEnum
	kMateCurveCurveJoint          =68108      # from enum RigidBodyJointTypeEnum
	kMateCylinderCylinderJoint    =68101      # from enum RigidBodyJointTypeEnum
	kMateLineLineJoint            =68100      # from enum RigidBodyJointTypeEnum
	kMatePointCircleJoint         =68106      # from enum RigidBodyJointTypeEnum
	kMatePointCurveJoint          =68105      # from enum RigidBodyJointTypeEnum
	kMatePointLineJoint           =68099      # from enum RigidBodyJointTypeEnum
	kMatePointPointJoint          =68098      # from enum RigidBodyJointTypeEnum
	kMatePointSurfaceJoint        =68107      # from enum RigidBodyJointTypeEnum
	kMateSphereConeJoint          =68103      # from enum RigidBodyJointTypeEnum
	kMateSphereSphereJoint        =68102      # from enum RigidBodyJointTypeEnum
	kPerpendicularCurveSurfaceJoint=68134      # from enum RigidBodyJointTypeEnum
	kRevoluteJoint                =68136      # from enum RigidBodyJointTypeEnum
	kSymmetricCircleCircleLineJoint=68148      # from enum RigidBodyJointTypeEnum
	kSymmetricEllipseEllipseLineJoint=68149      # from enum RigidBodyJointTypeEnum
	kSymmetricLineLineLineJoint   =68147      # from enum RigidBodyJointTypeEnum
	kSymmetricLineLinePlaneJoint  =68145      # from enum RigidBodyJointTypeEnum
	kSymmetricPlanePlanePlaneJoint=68144      # from enum RigidBodyJointTypeEnum
	kSymmetricPointPointLineJoint =68146      # from enum RigidBodyJointTypeEnum
	kSymmetricPointPointPlaneJoint=68142      # from enum RigidBodyJointTypeEnum
	kSymmetricVectorVectorPlaneJoint=68143      # from enum RigidBodyJointTypeEnum
	kTangentCircleCircleJoint     =68129      # from enum RigidBodyJointTypeEnum
	kTangentCircleCylinderJoint   =68127      # from enum RigidBodyJointTypeEnum
	kTangentConeConeJoint         =68125      # from enum RigidBodyJointTypeEnum
	kTangentCurveSurfaceJoint     =68132      # from enum RigidBodyJointTypeEnum
	kTangentCylinderConeJoint     =68123      # from enum RigidBodyJointTypeEnum
	kTangentCylinderCylinderJoint =68119      # from enum RigidBodyJointTypeEnum
	kTangentCylinderSphereJoint   =68120      # from enum RigidBodyJointTypeEnum
	kTangentLineCircleJoint       =68131      # from enum RigidBodyJointTypeEnum
	kTangentLineCylinderJoint     =68128      # from enum RigidBodyJointTypeEnum
	kTangentLineSphereJoint       =68130      # from enum RigidBodyJointTypeEnum
	kTangentPlaneCircleJoint      =68126      # from enum RigidBodyJointTypeEnum
	kTangentPlaneConeJoint        =68122      # from enum RigidBodyJointTypeEnum
	kTangentPlaneCylinderJoint    =68118      # from enum RigidBodyJointTypeEnum
	kTangentSphereConeJoint       =68124      # from enum RigidBodyJointTypeEnum
	kTangentSphereSphereJoint     =68121      # from enum RigidBodyJointTypeEnum
	kTangentSurfaceSurfaceJoint   =68133      # from enum RigidBodyJointTypeEnum
	kTransitionalJoint            =68137      # from enum RigidBodyJointTypeEnum
	kTranslationalJoint           =68135      # from enum RigidBodyJointTypeEnum
	kUniversalJoint               =68141      # from enum RigidBodyJointTypeEnum
	kUnknownJoint                 =68150      # from enum RigidBodyJointTypeEnum
	kWeldJoint                    =68140      # from enum RigidBodyJointTypeEnum
	kWireframeWireframeJoint      =68139      # from enum RigidBodyJointTypeEnum
	kFaceExtentsRipType           =90883      # from enum RipTypeEnum
	kPointToPointRipType          =90882      # from enum RipTypeEnum
	kSinglePointRipType           =90881      # from enum RipTypeEnum
	kCombineNotesRowMerge         =77315      # from enum RowMergeTypeEnum
	kNoRowMerge                   =77313      # from enum RowMergeTypeEnum
	kRollupRowMerge               =77314      # from enum RowMergeTypeEnum
	kNormalRuledSurfaceType       =110337     # from enum RuledSurfaceTypeEnum
	kSweepRuledSurfaceType        =110339     # from enum RuledSurfaceTypeEnum
	kTangentRuledSurfaceType      =110338     # from enum RuledSurfaceTypeEnum
	kLowerLeftQuadrant            =96001      # from enum ScreenQuadrantEnum
	kLowerRightQuadrant           =96002      # from enum ScreenQuadrantEnum
	kUpperLeftQuadrant            =96003      # from enum ScreenQuadrantEnum
	kUpperRightQuadrant           =96004      # from enum ScreenQuadrantEnum
	kOutOfDateFiles               =2          # from enum SearchBoxFilterEnum
	kUnresolvedFiles              =1          # from enum SearchBoxFilterEnum
	kHalfSectionViewType          =110850     # from enum SectionViewTypeEnum
	kNoSectionViewType            =110852     # from enum SectionViewTypeEnum
	kQuarterSectionViewType       =110849     # from enum SectionViewTypeEnum
	kThreeQuarterSectionViewType  =110851     # from enum SectionViewTypeEnum
	SELECTTYPE_INSIDE             =1          # from enum SelectType
	SELECTTYPE_OVERLAP            =2          # from enum SelectType
	kBrowserSelection             =15362      # from enum SelectionDeviceEnum
	kGraphicsWindowSelection      =15361      # from enum SelectionDeviceEnum
	kNameSelection                =15363      # from enum SelectionDeviceEnum
	kUnknownSelection             =15364      # from enum SelectionDeviceEnum
	kAllCircularEntities          =18435      # from enum SelectionFilterEnum
	kAllCustomGraphicsFilter      =18436      # from enum SelectionFilterEnum
	kAllEntitiesFilter            =18439      # from enum SelectionFilterEnum
	kAllLinearEntities            =18433      # from enum SelectionFilterEnum
	kAllPlanarEntities            =18432      # from enum SelectionFilterEnum
	kAllPointEntities             =18434      # from enum SelectionFilterEnum
	kAssemblyFeatureFilter        =16646      # from enum SelectionFilterEnum
	kAssemblyLeafOccurrenceFilter =16643      # from enum SelectionFilterEnum
	kAssemblyOccurrenceFilter     =16640      # from enum SelectionFilterEnum
	kAssemblyOccurrencePatternElementFilter=16645      # from enum SelectionFilterEnum
	kAssemblyOccurrencePatternFilter=16644      # from enum SelectionFilterEnum
	kCustomBrowserNodeFilter      =18437      # from enum SelectionFilterEnum
	kDWGEntityBlockFilter         =15911      # from enum SelectionFilterEnum
	kDWGEntityCircularFilter      =15907      # from enum SelectionFilterEnum
	kDWGEntityEllipticalFilter    =15908      # from enum SelectionFilterEnum
	kDWGEntityFilter              =15905      # from enum SelectionFilterEnum
	kDWGEntityLinearFilter        =15906      # from enum SelectionFilterEnum
	kDWGEntityPolylineFilter      =15909      # from enum SelectionFilterEnum
	kDWGEntitySegmentFilter       =15912      # from enum SelectionFilterEnum
	kDWGEntitySplineFilter        =15910      # from enum SelectionFilterEnum
	kDrawingAutoCADBlockDefinitionFilter=16923      # from enum SelectionFilterEnum
	kDrawingAutoCADBlockFilter    =16922      # from enum SelectionFilterEnum
	kDrawingBalloonFilter         =16906      # from enum SelectionFilterEnum
	kDrawingBorderDefinitionFilter=16909      # from enum SelectionFilterEnum
	kDrawingBorderFilter          =16913      # from enum SelectionFilterEnum
	kDrawingCenterlineFilter      =16915      # from enum SelectionFilterEnum
	kDrawingCentermarkFilter      =16916      # from enum SelectionFilterEnum
	kDrawingCurveSegmentFilter    =16914      # from enum SelectionFilterEnum
	kDrawingCustomTableFilter     =16905      # from enum SelectionFilterEnum
	kDrawingDefaultFilter         =16896      # from enum SelectionFilterEnum
	kDrawingDimensionFilter       =16900      # from enum SelectionFilterEnum
	kDrawingFeatureControlFrameFilter=16918      # from enum SelectionFilterEnum
	kDrawingHoleTableFilter       =16902      # from enum SelectionFilterEnum
	kDrawingHoleTagFilter         =16903      # from enum SelectionFilterEnum
	kDrawingNoteFilter            =16899      # from enum SelectionFilterEnum
	kDrawingOriginIndicatorFilter =16920      # from enum SelectionFilterEnum
	kDrawingPartsListFilter       =16901      # from enum SelectionFilterEnum
	kDrawingRevisionTableFilter   =16904      # from enum SelectionFilterEnum
	kDrawingSheetFilter           =16897      # from enum SelectionFilterEnum
	kDrawingSheetFormatFilter     =16917      # from enum SelectionFilterEnum
	kDrawingSketchedSymbolDefinitionFilter=16908      # from enum SelectionFilterEnum
	kDrawingSketchedSymbolFilter  =16907      # from enum SelectionFilterEnum
	kDrawingSurfaceTextureSymbolFilter=16919      # from enum SelectionFilterEnum
	kDrawingTitleBlockDefinitionFilter=16910      # from enum SelectionFilterEnum
	kDrawingTitleBlockFilter      =16912      # from enum SelectionFilterEnum
	kDrawingViewFilter            =16898      # from enum SelectionFilterEnum
	kDrawingViewLabelFilter       =16921      # from enum SelectionFilterEnum
	kFeatureDimensionFilter       =18438      # from enum SelectionFilterEnum
	kModelAnnotationFilter        =16388      # from enum SelectionFilterEnum
	kPartBodyFilter               =15890      # from enum SelectionFilterEnum
	kPartDefaultFilter            =15886      # from enum SelectionFilterEnum
	kPartEdgeCircularFilter       =15874      # from enum SelectionFilterEnum
	kPartEdgeFilter               =15873      # from enum SelectionFilterEnum
	kPartEdgeLinearFilter         =15875      # from enum SelectionFilterEnum
	kPartEdgeMidpointFilter       =15876      # from enum SelectionFilterEnum
	kPartFaceConicalFilter        =15880      # from enum SelectionFilterEnum
	kPartFaceCylindricalFilter    =15879      # from enum SelectionFilterEnum
	kPartFaceFilter               =15877      # from enum SelectionFilterEnum
	kPartFacePlanarFilter         =15878      # from enum SelectionFilterEnum
	kPartFaceSphericalFilter      =15882      # from enum SelectionFilterEnum
	kPartFaceToroidalFilter       =15881      # from enum SelectionFilterEnum
	kPartFeatureFilter            =15884      # from enum SelectionFilterEnum
	kPartMeshEdgeCircularFilter   =15903      # from enum SelectionFilterEnum
	kPartMeshEdgeFilter           =15897      # from enum SelectionFilterEnum
	kPartMeshEdgeLinearFilter     =15904      # from enum SelectionFilterEnum
	kPartMeshFaceConicalFilter    =15900      # from enum SelectionFilterEnum
	kPartMeshFaceCylindricalFilter=15899      # from enum SelectionFilterEnum
	kPartMeshFaceFilter           =15896      # from enum SelectionFilterEnum
	kPartMeshFacePlanarFilter     =15901      # from enum SelectionFilterEnum
	kPartMeshFaceSphericalFilter  =15902      # from enum SelectionFilterEnum
	kPartMeshFeatureFilter        =15894      # from enum SelectionFilterEnum
	kPartMeshFeatureSetFilter     =15895      # from enum SelectionFilterEnum
	kPartMeshVertexFilter         =15898      # from enum SelectionFilterEnum
	kPartSurfaceFeatureFilter     =15885      # from enum SelectionFilterEnum
	kPartVertexFilter             =15883      # from enum SelectionFilterEnum
	kPointCloudFilter             =15891      # from enum SelectionFilterEnum
	kPointCloudPlaneFilter        =15893      # from enum SelectionFilterEnum
	kPointCloudPointFilter        =15892      # from enum SelectionFilterEnum
	kPublicationComponentFilter   =17153      # from enum SelectionFilterEnum
	kPublicationEdgeFilter        =17156      # from enum SelectionFilterEnum
	kPublicationFaceFilter        =17155      # from enum SelectionFilterEnum
	kPublicationLeafComponentFilter=17154      # from enum SelectionFilterEnum
	kPublicationTrailNodeFilter   =17159      # from enum SelectionFilterEnum
	kPublicationTrailSegmentFilter=17160      # from enum SelectionFilterEnum
	kPublicationTweakPathFilter   =17158      # from enum SelectionFilterEnum
	kPublicationVertexFilter      =17157      # from enum SelectionFilterEnum
	kSketch3DCurveCircularFilter  =17666      # from enum SelectionFilterEnum
	kSketch3DCurveEllipseFilter   =17667      # from enum SelectionFilterEnum
	kSketch3DCurveFilter          =17664      # from enum SelectionFilterEnum
	kSketch3DCurveLinearFilter    =17665      # from enum SelectionFilterEnum
	kSketch3DCurveSplineFilter    =17668      # from enum SelectionFilterEnum
	kSketch3DDefaultFilter        =17670      # from enum SelectionFilterEnum
	kSketch3DDimConstraintFilter  =17672      # from enum SelectionFilterEnum
	kSketch3DObjectFilter         =17671      # from enum SelectionFilterEnum
	kSketch3DPointFilter          =17669      # from enum SelectionFilterEnum
	kSketch3DProfileFilter        =17673      # from enum SelectionFilterEnum
	kSketchBlockDefinitionFilter  =16141      # from enum SelectionFilterEnum
	kSketchBlockFilter            =16142      # from enum SelectionFilterEnum
	kSketchCurveCircularFilter    =16131      # from enum SelectionFilterEnum
	kSketchCurveEllipseFilter     =16132      # from enum SelectionFilterEnum
	kSketchCurveFilter            =16129      # from enum SelectionFilterEnum
	kSketchCurveLinearFilter      =16130      # from enum SelectionFilterEnum
	kSketchCurveSplineFilter      =16133      # from enum SelectionFilterEnum
	kSketchDefaultFilter          =16135      # from enum SelectionFilterEnum
	kSketchDimConstraintFilter    =16128      # from enum SelectionFilterEnum
	kSketchImageFilter            =16137      # from enum SelectionFilterEnum
	kSketchObjectFilter           =16136      # from enum SelectionFilterEnum
	kSketchPointFilter            =16134      # from enum SelectionFilterEnum
	kSketchProfileFilter          =16139      # from enum SelectionFilterEnum
	kSketchProjectedCutFilter     =16140      # from enum SelectionFilterEnum
	kSketchTextBoxFilter          =16138      # from enum SelectionFilterEnum
	kUserCoordinateSystemFilter   =16387      # from enum SelectionFilterEnum
	kWorkAxisFilter               =16384      # from enum SelectionFilterEnum
	kWorkPlaneFilter              =16385      # from enum SelectionFilterEnum
	kWorkPointFilter              =16386      # from enum SelectionFilterEnum
	kAnnotationSelectionPriority  =67594      # from enum SelectionPriorityEnum
	kBodySelectionPriority        =67593      # from enum SelectionPriorityEnum
	kComponentSelectionPriority   =67590      # from enum SelectionPriorityEnum
	kEdgeAndFaceSelectionPriority =67587      # from enum SelectionPriorityEnum
	kEdgeSelectionPriority        =67592      # from enum SelectionPriorityEnum
	kFeatureSelectionPriority     =67585      # from enum SelectionPriorityEnum
	kGroupSelectionPriority       =67588      # from enum SelectionPriorityEnum
	kPartSelectionPriority        =67591      # from enum SelectionPriorityEnum
	kSketchSelectionPriority      =67586      # from enum SelectionPriorityEnum
	kWireSelectionPriority        =67589      # from enum SelectionPriorityEnum
	k45DegreesLeftShadowDirection =92161      # from enum ShadowDirectionEnum
	k45DegreesRightShadowDirection=92162      # from enum ShadowDirectionEnum
	kAboveShadowDirection         =92163      # from enum ShadowDirectionEnum
	kEnvironmentShadowDirection   =92168      # from enum ShadowDirectionEnum
	kLightFourShadowDirection     =92167      # from enum ShadowDirectionEnum
	kLightOneShadowDirection      =92164      # from enum ShadowDirectionEnum
	kLightThreeShadowDirection    =92166      # from enum ShadowDirectionEnum
	kLightTwoShadowDirection      =92165      # from enum ShadowDirectionEnum
	kUnknownShapeTutorialIndicator=50454593   # from enum ShapeStyleEnum
	kSheetMetalFlatPatternArea    =78851      # from enum SheetMetalPropertyEnum
	kSheetMetalFlatPatternLength  =78849      # from enum SheetMetalPropertyEnum
	kSheetMetalFlatPatternWidth   =78850      # from enum SheetMetalPropertyEnum
	kBothSidesShellDirection      =41219      # from enum ShellDirectionEnum
	kInsideShellDirection         =41217      # from enum ShellDirectionEnum
	kOutsideShellDirection        =41218      # from enum ShellDirectionEnum
	kShiftStateAlt                =4          # from enum ShiftStateEnum
	kShiftStateCtrl               =2          # from enum ShiftStateEnum
	kShiftStateCtrlAlt            =6          # from enum ShiftStateEnum
	kShiftStateNone               =0          # from enum ShiftStateEnum
	kShiftStateShift              =1          # from enum ShiftStateEnum
	kShiftStateShiftAlt           =5          # from enum ShiftStateEnum
	kShiftStateShiftCtrl          =3          # from enum ShiftStateEnum
	kShiftStateShiftCtrlAlt       =7          # from enum ShiftStateEnum
	kAcceleratorShortcut          =68355      # from enum ShortcutTypeEnum
	kAliasShortcut                =68354      # from enum ShortcutTypeEnum
	kNoShortcut                   =68353      # from enum ShortcutTypeEnum
	kShrinkwrapRemoveAll          =114690     # from enum ShrinkwrapRemoveStyleEnum
	kShrinkwrapRemoveByRange      =114691     # from enum ShrinkwrapRemoveStyleEnum
	kShrinkwrapRemoveNone         =114689     # from enum ShrinkwrapRemoveStyleEnum
	kCoincidentInference          =1          # from enum SketchConstraintInferenceTypeEnum
	kHorizontalInference          =2          # from enum SketchConstraintInferenceTypeEnum
	kIntersectionInference        =4          # from enum SketchConstraintInferenceTypeEnum
	kMidPointInference            =8          # from enum SketchConstraintInferenceTypeEnum
	kOnCurveInference             =16         # from enum SketchConstraintInferenceTypeEnum
	kParallelInference            =32         # from enum SketchConstraintInferenceTypeEnum
	kPerpendicularInference       =64         # from enum SketchConstraintInferenceTypeEnum
	kTangentInference             =128        # from enum SketchConstraintInferenceTypeEnum
	kVerticalInference            =256        # from enum SketchConstraintInferenceTypeEnum
	kNoNewSketchCreation          =55041      # from enum SketchCreationOnNewPartEnum
	kXYPlaneSketchCreation        =55042      # from enum SketchCreationOnNewPartEnum
	kXZPlaneSketchCreation        =55044      # from enum SketchCreationOnNewPartEnum
	kYZPlaneSketchCreation        =55043      # from enum SketchCreationOnNewPartEnum
	kCoincident                   =1          # from enum SketchGeometricConstraintTypeEnum
	kColinear                     =4          # from enum SketchGeometricConstraintTypeEnum
	kConcentric                   =2          # from enum SketchGeometricConstraintTypeEnum
	kEqual                        =8          # from enum SketchGeometricConstraintTypeEnum
	kFix                          =16         # from enum SketchGeometricConstraintTypeEnum
	kHorizontal                   =32         # from enum SketchGeometricConstraintTypeEnum
	kParallel                     =64         # from enum SketchGeometricConstraintTypeEnum
	kPerpendicular                =128        # from enum SketchGeometricConstraintTypeEnum
	kSmooth                       =256        # from enum SketchGeometricConstraintTypeEnum
	kSymmetric                    =512        # from enum SketchGeometricConstraintTypeEnum
	kTangent                      =1024       # from enum SketchGeometricConstraintTypeEnum
	kVertical                     =2048       # from enum SketchGeometricConstraintTypeEnum
	kDistinctlyManySolutions      =2          # from enum SolutionNatureEnum
	kInfinitelyManySolutions      =3          # from enum SolutionNatureEnum
	kNoSolution                   =4          # from enum SolutionNatureEnum
	kUniqueSolution               =1          # from enum SolutionNatureEnum
	kUnknownSolutionNature        =0          # from enum SolutionNatureEnum
	kACADSplineFit                =26371      # from enum SplineFitMethodEnum
	kSmoothSplineFit              =26369      # from enum SplineFitMethodEnum
	kSweetSplineFit               =26370      # from enum SplineFitMethodEnum
	kPath                         =33025      # from enum SplitToolTypeEnum
	kSurfaceBody                  =33028      # from enum SplitToolTypeEnum
	kWorkPlane                    =33026      # from enum SplitToolTypeEnum
	kWorkSurface                  =33027      # from enum SplitToolTypeEnum
	kSplitBody                    =32771      # from enum SplitTypeEnum
	kSplitFaces                   =32770      # from enum SplitTypeEnum
	kSplitPart                    =32769      # from enum SplitTypeEnum
	kTrimSolid                    =32769      # from enum SplitTypeEnum
	kAlwaysSectionStandardParts   =66561      # from enum StandardPartsSectionBehaviorEnum
	kNeverSectionStandardParts    =66562      # from enum StandardPartsSectionBehaviorEnum
	kObeyBrowserSettingsSectionStandardParts=66563      # from enum StandardPartsSectionBehaviorEnum
	kFileNewDialogStartupAction   =70913      # from enum StartupActionTypeEnum
	kFileOpenDialogStartupAction  =70914      # from enum StartupActionTypeEnum
	kNewFileFromTemplateStartupAction=70915      # from enum StartupActionTypeEnum
	kNoStartupAction              =70916      # from enum StartupActionTypeEnum
	kInventorClassicStartupHelpTopic=71169      # from enum StartupHelpFocusTopicEnum
	kInventorForAutocadStartupHelpTopic=71170      # from enum StartupHelpFocusTopicEnum
	kStatusError                  =96004      # from enum StatusEnum
	kStatusNo                     =96002      # from enum StatusEnum
	kStatusUnknown                =96003      # from enum StatusEnum
	kStatusYes                    =96001      # from enum StatusEnum
	kFileOrStreamStorage          =6148       # from enum StorageTypeEnum
	kFileStorage                  =6146       # from enum StorageTypeEnum
	kStorageStorage               =6149       # from enum StorageTypeEnum
	kStreamStorage                =6147       # from enum StorageTypeEnum
	kUnknownStorage               =6145       # from enum StorageTypeEnum
	kPublicationTrailType         =2          # from enum StoryboardObjectTypeEnum
	kPublicationTweakPathType     =1          # from enum StoryboardObjectTypeEnum
	kBothStyleLocation            =51201      # from enum StyleLocationEnum
	kLibraryStyleLocation         =51203      # from enum StyleLocationEnum
	kLocalStyleLocation           =51202      # from enum StyleLocationEnum
	kBodyRenderStyle              =37125      # from enum StyleSourceTypeEnum
	kFeatureRenderStyle           =37122      # from enum StyleSourceTypeEnum
	kOverrideRenderStyle          =37123      # from enum StyleSourceTypeEnum
	kPartRenderStyle              =37121      # from enum StyleSourceTypeEnum
	kWeldBeadRenderStyle          =37124      # from enum StyleSourceTypeEnum
	kBalloonStyleType             =71426      # from enum StyleTypeEnum
	kCentermarkStyleType          =71427      # from enum StyleTypeEnum
	kDatumTargetStyleType         =71428      # from enum StyleTypeEnum
	kDimensionStyleType           =71429      # from enum StyleTypeEnum
	kFeatureControlFrameStyleType =71430      # from enum StyleTypeEnum
	kHatchStyleType               =71431      # from enum StyleTypeEnum
	kHoleTableStyleType           =71432      # from enum StyleTypeEnum
	kIDStyleType                  =71433      # from enum StyleTypeEnum
	kLayerStyleType               =71434      # from enum StyleTypeEnum
	kLeaderStyleType              =71435      # from enum StyleTypeEnum
	kObjectDefaultsStyleType      =71436      # from enum StyleTypeEnum
	kPartsListStyleType           =71437      # from enum StyleTypeEnum
	kRevisionTableStyleType       =71438      # from enum StyleTypeEnum
	kSheetMetalStyleType          =71445      # from enum StyleTypeEnum
	kStandardStyleType            =71425      # from enum StyleTypeEnum
	kSurfaceTextureStyleType      =71439      # from enum StyleTypeEnum
	kTableStyleType               =71440      # from enum StyleTypeEnum
	kTextStyleType                =71441      # from enum StyleTypeEnum
	kUnfoldMethodType             =71446      # from enum StyleTypeEnum
	kViewAnnotationStyleType      =71444      # from enum StyleTypeEnum
	kWeldBeadStyleType            =71443      # from enum StyleTypeEnum
	kWeldSymbolStyleType          =71442      # from enum StyleTypeEnum
	kNoStylesLibraryAccess        =54019      # from enum StylesLibraryAccessEnum
	kReadOnlyStylesLibraryAccess  =54017      # from enum StylesLibraryAccessEnum
	kReadWriteStylesLibraryAccess =54018      # from enum StylesLibraryAccessEnum
	SurfaceGeometryForm_ClosedUVLoops=1          # from enum SurfaceGeometryFormEnum
	SurfaceGeometryForm_NURBS     =4          # from enum SurfaceGeometryFormEnum
	SurfaceGeometryForm_Not_ClosedUVLoops=2          # from enum SurfaceGeometryFormEnum
	SurfaceGeometryForm_Not_NURBS =8          # from enum SurfaceGeometryFormEnum
	SurfaceGeometryForm_ProceduralToNURBS=16         # from enum SurfaceGeometryFormEnum
	kBasicSurfaceType             =76801      # from enum SurfaceTextureTypeEnum
	kMaterialRemovalProhibitedSurfaceType=76803      # from enum SurfaceTextureTypeEnum
	kMaterialRemovalRequiredSurfaceType=76802      # from enum SurfaceTextureTypeEnum
	kBSplineSurface               =5897       # from enum SurfaceTypeEnum
	kConeSurface                  =5893       # from enum SurfaceTypeEnum
	kCylinderSurface              =5891       # from enum SurfaceTypeEnum
	kEllipticalConeSurface        =5894       # from enum SurfaceTypeEnum
	kEllipticalCylinderSurface    =5892       # from enum SurfaceTypeEnum
	kPlaneSurface                 =5890       # from enum SurfaceTypeEnum
	kSphereSurface                =5896       # from enum SurfaceTypeEnum
	kTorusSurface                 =5895       # from enum SurfaceTypeEnum
	kUnknownSurface               =5889       # from enum SurfaceTypeEnum
	kPathAndGuideRailSweepDef     =59138      # from enum SweepDefinitionTypeEnum
	kPathAndGuideSurfaceSweepDef  =59139      # from enum SweepDefinitionTypeEnum
	kPathAndSectionTwistsSweepDef =59140      # from enum SweepDefinitionTypeEnum
	kPathSweepDef                 =59137      # from enum SweepDefinitionTypeEnum
	kAlignToVector                =59651      # from enum SweepProfileOrientationEnum
	kNormalToPath                 =59649      # from enum SweepProfileOrientationEnum
	kParallelToOriginalProfile    =59650      # from enum SweepProfileOrientationEnum
	kNoProfileScaling             =59395      # from enum SweepProfileScalingEnum
	kXProfileScaling              =59394      # from enum SweepProfileScalingEnum
	kXYProfileScaling             =59393      # from enum SweepProfileScalingEnum
	kPathAndGuidRailSweepType     =104450     # from enum SweepTypeEnum
	kPathAndGuidSurfaceSweepType  =104451     # from enum SweepTypeEnum
	kPathAndSectionTwistSweepType =104452     # from enum SweepTypeEnum
	kPathSweepType                =104449     # from enum SweepTypeEnum
	kDefaultSystemOfMeasure       =8961       # from enum SystemOfMeasureEnum
	kEnglishSystemOfMeasure       =8963       # from enum SystemOfMeasureEnum
	kMetricSystemOfMeasure        =8962       # from enum SystemOfMeasureEnum
	kBottomUpDirection            =46082      # from enum TableDirectionEnum
	kTopDownDirection             =46081      # from enum TableDirectionEnum
	kBendTableSource              =77058      # from enum TableSourceTypeEnum
	kCSVTableSource               =77061      # from enum TableSourceTypeEnum
	kConfigurationTableSource     =77059      # from enum TableSourceTypeEnum
	kExcelTableSource             =77060      # from enum TableSourceTypeEnum
	kNoTableSource                =77057      # from enum TableSourceTypeEnum
	kExactLineSpacing             =29185      # from enum TextLineSpacingTypeEnum
	kMultipleLineSpacing          =29186      # from enum TextLineSpacingTypeEnum
	k1DTexture                    =95489      # from enum TextureDimensionEnum
	k2DTexture                    =95490      # from enum TextureDimensionEnum
	kAutomaticMappingType         =100866     # from enum TextureMappingTypeEnum
	kBoxMappingType               =100867     # from enum TextureMappingTypeEnum
	kCylindricalMappingType       =100868     # from enum TextureMappingTypeEnum
	kNoMappingType                =100865     # from enum TextureMappingTypeEnum
	kPlanarMappingType            =100869     # from enum TextureMappingTypeEnum
	kSphericalMappingType         =100870     # from enum TextureMappingTypeEnum
	kStandardThread               =22017      # from enum ThreadTypeEnum
	kTaperedThread                =22018      # from enum ThreadTypeEnum
	kActiveComponentIsoViewOnSave =79874      # from enum ThumbnailSaveOptionEnum
	kActiveWindow                 =79876      # from enum ThumbnailSaveOptionEnum
	kActiveWindowOnSave           =79875      # from enum ThumbnailSaveOptionEnum
	kImportFromFile               =79877      # from enum ThumbnailSaveOptionEnum
	kNoThumbnail                  =79873      # from enum ThumbnailSaveOptionEnum
	kLowerLeftTitleBlockAlignment =66818      # from enum TitleBlockAlignmentEnum
	kLowerRightTitleBlockAlignment=66820      # from enum TitleBlockAlignmentEnum
	kUpperLeftTitleBlockAlignment =66817      # from enum TitleBlockAlignmentEnum
	kUpperRightTitleBlockAlignment=66819      # from enum TitleBlockAlignmentEnum
	kBottomLeftPosition           =29443      # from enum TitleBlockLocationEnum
	kBottomRightPosition          =29444      # from enum TitleBlockLocationEnum
	kTopLeftPosition              =29441      # from enum TitleBlockLocationEnum
	kTopRightPosition             =29442      # from enum TitleBlockLocationEnum
	kBasicTolerance               =31245      # from enum ToleranceTypeEnum
	kDefaultTolerance             =31233      # from enum ToleranceTypeEnum
	kDeviationTolerance           =31236      # from enum ToleranceTypeEnum
	kLimitLinearTolerance         =31238      # from enum ToleranceTypeEnum
	kLimitsFitsLinearTolerance    =31242      # from enum ToleranceTypeEnum
	kLimitsFitsShowSizeTolerance  =31243      # from enum ToleranceTypeEnum
	kLimitsFitsShowTolerance      =31244      # from enum ToleranceTypeEnum
	kLimitsFitsStackedTolerance   =31241      # from enum ToleranceTypeEnum
	kLimitsStackedTolerance       =31237      # from enum ToleranceTypeEnum
	kMaxTolerance                 =31239      # from enum ToleranceTypeEnum
	kMinTolerance                 =31240      # from enum ToleranceTypeEnum
	kOverrideTolerance            =31234      # from enum ToleranceTypeEnum
	kReferenceTolerance           =31246      # from enum ToleranceTypeEnum
	kSymmetricTolerance           =31235      # from enum ToleranceTypeEnum
	kCurrentTransaction           =3588       # from enum TransactionPointEnum
	kNextTransaction              =3586       # from enum TransactionPointEnum
	kPreviousTransaction          =3587       # from enum TransactionPointEnum
	kUnknownTransaction           =3585       # from enum TransactionPointEnum
	kUptoSpecifiedTransaction     =3589       # from enum TransactionPointEnum
	kDoneState                    =36866      # from enum TransactionStateEnum
	kUncommittedState             =36865      # from enum TransactionStateEnum
	kUndoneState                  =36867      # from enum TransactionStateEnum
	kBlendingTransparency         =58625      # from enum TransparencyTypeEnum
	kScreenDoorTransparency       =58626      # from enum TransparencyTypeEnum
	kRepositionMoveType           =49409      # from enum TriadMoveTypeEnum
	kAllSegments                  =0          # from enum TriadSegmentEnum
	kOriginSegment                =1          # from enum TriadSegmentEnum
	kXAxisRotationSegment         =16         # from enum TriadSegmentEnum
	kXAxisTranslationSegment      =2          # from enum TriadSegmentEnum
	kXYPlaneTranslationSegment    =128        # from enum TriadSegmentEnum
	kXZPlaneTranslationSegment    =256        # from enum TriadSegmentEnum
	kYAxisRotationSegment         =32         # from enum TriadSegmentEnum
	kYAxisTranslationSegment      =4          # from enum TriadSegmentEnum
	kYZPlaneTranslationSegment    =512        # from enum TriadSegmentEnum
	kZAxisRotationSegment         =64         # from enum TriadSegmentEnum
	kZAxisTranslationSegment      =8          # from enum TriadSegmentEnum
	kRotationTweakType            =111106     # from enum TweakTypeEnum
	kTransformTweakType           =111107     # from enum TweakTypeEnum
	kTranslationTweakType         =111105     # from enum TweakTypeEnum
	kThreePointsDefinitionType    =90370      # from enum UCSDefinitionTypeEnum
	kTransformationDefinitionType =90369      # from enum UCSDefinitionTypeEnum
	kBendAllowanceEquationType    =81409      # from enum UnfoldMethodEquationTypeEnum
	kBendCompensationEquationType =81410      # from enum UnfoldMethodEquationTypeEnum
	kBendDeductionEquationType    =81411      # from enum UnfoldMethodEquationTypeEnum
	kBendkFactorEquationType      =81412      # from enum UnfoldMethodEquationTypeEnum
	kBendTableUnfoldMethod        =28674      # from enum UnfoldMethodTypeEnum
	kCustomEquationUnfoldMethod   =28675      # from enum UnfoldMethodTypeEnum
	kLinearUnfoldMethod           =28673      # from enum UnfoldMethodTypeEnum
	kLockDOF                      =4          # from enum UniqueOccurrencesBehaviorEnum
	kRetainDOF                    =2          # from enum UniqueOccurrencesBehaviorEnum
	kSinglePartRigidBody          =1          # from enum UniqueOccurrencesBehaviorEnum
	kAcreAreaUnits                =11301      # from enum UnitsTypeEnum
	kAmpElectricalCurrentUnits    =11327      # from enum UnitsTypeEnum
	kBTUWorkUnits                 =11320      # from enum UnitsTypeEnum
	kBooleanUnits                 =11347      # from enum UnitsTypeEnum
	kCalorieWorkUnits             =11319      # from enum UnitsTypeEnum
	kCandelaLuminousIntensityUnits=11342      # from enum UnitsTypeEnum
	kCelsiusTemperatureUnits      =11296      # from enum UnitsTypeEnum
	kCentimeterLengthUnits        =11268      # from enum UnitsTypeEnum
	kCircularMilAreaUnits         =11326      # from enum UnitsTypeEnum
	kCompositeUnits               =11322      # from enum UnitsTypeEnum
	kCoulombElectricalChargeUnits =11330      # from enum UnitsTypeEnum
	kCupVolumeUnits               =11306      # from enum UnitsTypeEnum
	kDatabaseAngleUnits           =11277      # from enum UnitsTypeEnum
	kDatabaseLengthUnits          =11267      # from enum UnitsTypeEnum
	kDatabaseMassUnits            =11282      # from enum UnitsTypeEnum
	kDatabaseTemperatureUnits     =11294      # from enum UnitsTypeEnum
	kDatabaseTimeUnits            =11289      # from enum UnitsTypeEnum
	kDefaultDisplayAngleUnits     =11276      # from enum UnitsTypeEnum
	kDefaultDisplayLengthUnits    =11266      # from enum UnitsTypeEnum
	kDefaultDisplayMassUnits      =11281      # from enum UnitsTypeEnum
	kDefaultDisplayTemperatureUnits=11293      # from enum UnitsTypeEnum
	kDefaultDisplayTimeUnits      =11288      # from enum UnitsTypeEnum
	kDegreeAngleUnits             =11279      # from enum UnitsTypeEnum
	kDyneForceUnits               =11312      # from enum UnitsTypeEnum
	kErgWorkUnits                 =11318      # from enum UnitsTypeEnum
	kFahrenheitTemperatureUnits   =11297      # from enum UnitsTypeEnum
	kFaradElectricalCapacitanceUnits=11331      # from enum UnitsTypeEnum
	kFeetPerSecondSpeedUnits      =11299      # from enum UnitsTypeEnum
	kFootLengthUnits              =11273      # from enum UnitsTypeEnum
	kGallonVolumeUnits            =11303      # from enum UnitsTypeEnum
	kGammaMagneticInductionUnits  =11337      # from enum UnitsTypeEnum
	kGaussMagneticInductionUnits  =11338      # from enum UnitsTypeEnum
	kGradAngleUnits               =11280      # from enum UnitsTypeEnum
	kGramMassUnits                =11284      # from enum UnitsTypeEnum
	kHenryElectricalInductanceUnits=11339      # from enum UnitsTypeEnum
	kHertzFrequencyUnits          =11341      # from enum UnitsTypeEnum
	kHorsePowerPowerUnits         =11316      # from enum UnitsTypeEnum
	kHourTimeUnits                =11292      # from enum UnitsTypeEnum
	kInchLengthUnits              =11272      # from enum UnitsTypeEnum
	kJouleWorkUnits               =11317      # from enum UnitsTypeEnum
	kKSIPressureUnits             =11310      # from enum UnitsTypeEnum
	kKelvinTemperatureUnits       =11295      # from enum UnitsTypeEnum
	kKilogramMassUnits            =11283      # from enum UnitsTypeEnum
	kLbForceUnits                 =11313      # from enum UnitsTypeEnum
	kLbMassMassUnits              =11286      # from enum UnitsTypeEnum
	kLiterVolumeUnits             =11302      # from enum UnitsTypeEnum
	kLumenLuminousFluxUnits       =11343      # from enum UnitsTypeEnum
	kLuxIlluminationUnits         =11344      # from enum UnitsTypeEnum
	kMaxwellMagneticFluxUnits     =11335      # from enum UnitsTypeEnum
	kMeterLengthUnits             =11270      # from enum UnitsTypeEnum
	kMetersPerSecondSpeedUnits    =11298      # from enum UnitsTypeEnum
	kMicronLengthUnits            =11271      # from enum UnitsTypeEnum
	kMilLengthUnits               =11324      # from enum UnitsTypeEnum
	kMileLengthUnits              =11275      # from enum UnitsTypeEnum
	kMilesPerHourSpeedUnits       =11300      # from enum UnitsTypeEnum
	kMillimeterLengthUnits        =11269      # from enum UnitsTypeEnum
	kMinuteTimeUnits              =11291      # from enum UnitsTypeEnum
	kMoleSubstanceUnits           =11345      # from enum UnitsTypeEnum
	kNauticalMileLengthUnits      =11323      # from enum UnitsTypeEnum
	kNewtonForceUnits             =11311      # from enum UnitsTypeEnum
	kOerstedMagneticInductionUnits=11340      # from enum UnitsTypeEnum
	kOhmElectricalResistanceUnits =11329      # from enum UnitsTypeEnum
	kOunceForceUnits              =11314      # from enum UnitsTypeEnum
	kOunceMassUnits               =11287      # from enum UnitsTypeEnum
	kOunceVolumeUnits             =11307      # from enum UnitsTypeEnum
	kPSIPressureUnits             =11309      # from enum UnitsTypeEnum
	kPascalPressureUnits          =11308      # from enum UnitsTypeEnum
	kPintVolumeUnits              =11305      # from enum UnitsTypeEnum
	kQuartVolumeUnits             =11304      # from enum UnitsTypeEnum
	kRPMAngularVelocityUnits      =11321      # from enum UnitsTypeEnum
	kRadianAngleUnits             =11278      # from enum UnitsTypeEnum
	kSecondTimeUnits              =11290      # from enum UnitsTypeEnum
	kSiemensElectricalConductanceUnits=11332      # from enum UnitsTypeEnum
	kSlugMassUnits                =11285      # from enum UnitsTypeEnum
	kSteradianAngleUnits          =11325      # from enum UnitsTypeEnum
	kTeslaMagneticInductionUnits  =11336      # from enum UnitsTypeEnum
	kTextUnits                    =11346      # from enum UnitsTypeEnum
	kUnitlessUnits                =11265      # from enum UnitsTypeEnum
	kVoltElectricalVoltageUnits   =11328      # from enum UnitsTypeEnum
	kWattPowerUnits               =11315      # from enum UnitsTypeEnum
	kWeberMagneticFluxUnits       =11334      # from enum UnitsTypeEnum
	kYardLengthUnits              =11274      # from enum UnitsTypeEnum
	kmhoElectricalConductanceUnits=11333      # from enum UnitsTypeEnum
	kOriginAlignment              =116993     # from enum UnwrapResultAlignmentEnum
	kXYPlaneAlignment             =116994     # from enum UnwrapResultAlignmentEnum
	kDontUpdateProperties         =71681      # from enum UpdatePropertiesOnSaveForFileTypeEnum
	kUpdatePropertiesForPartsAndAssemblies=71683      # from enum UpdatePropertiesOnSaveForFileTypeEnum
	kUpdatePropertiesForPartsOnly =71682      # from enum UpdatePropertiesOnSaveForFileTypeEnum
	kApplicationVBAProject        =30465      # from enum VBAProjectTypeEnum
	kDocumentVBAProject           =30466      # from enum VBAProjectTypeEnum
	kUserVBAProject               =30467      # from enum VBAProjectTypeEnum
	kBooleanType                  =14597      # from enum ValueTypeEnum
	kByteArrayType                =14596      # from enum ValueTypeEnum
	kDoubleType                   =14594      # from enum ValueTypeEnum
	kIntegerType                  =14593      # from enum ValueTypeEnum
	kStringType                   =14595      # from enum ValueTypeEnum
	kAngleUnits                   =94977      # from enum ValueUnitsTypeEnum
	kAngularVelocityUnits         =94978      # from enum ValueUnitsTypeEnum
	kAreaUnits                    =94979      # from enum ValueUnitsTypeEnum
	kCurrentUnits                 =94980      # from enum ValueUnitsTypeEnum
	kForceUnits                   =94981      # from enum ValueUnitsTypeEnum
	kLengthUnits                  =94982      # from enum ValueUnitsTypeEnum
	kMassUnits                    =94983      # from enum ValueUnitsTypeEnum
	kPowerUnits                   =94984      # from enum ValueUnitsTypeEnum
	kPressureUnits                =94985      # from enum ValueUnitsTypeEnum
	kSpeedUnits                   =94986      # from enum ValueUnitsTypeEnum
	kTemperatureUnits             =94987      # from enum ValueUnitsTypeEnum
	kTimeUnits                    =94988      # from enum ValueUnitsTypeEnum
	kUnitless                     =94989      # from enum ValueUnitsTypeEnum
	kVoltageUnits                 =94990      # from enum ValueUnitsTypeEnum
	kVolumeUnits                  =94991      # from enum ValueUnitsTypeEnum
	kWorkUnits                    =94992      # from enum ValueUnitsTypeEnum
	kAlignTextBaseline            =25604      # from enum VerticalTextAlignmentEnum
	kAlignTextLower               =25603      # from enum VerticalTextAlignmentEnum
	kAlignTextMiddle              =25601      # from enum VerticalTextAlignmentEnum
	kAlignTextUpper               =25602      # from enum VerticalTextAlignmentEnum
	kModelOriginInsertion         =86786      # from enum ViewBlockInsertionPointEnum
	kViewCenterInsertion          =86785      # from enum ViewBlockInsertionPointEnum
	kCenteredViewJustification    =67073      # from enum ViewJustificationEnum
	kFixedViewJustification       =67074      # from enum ViewJustificationEnum
	kBottomLeftViewCorner         =41475      # from enum ViewLayoutEnum
	kBottomRightViewCorner        =41476      # from enum ViewLayoutEnum
	kTopLeftViewCorner            =41473      # from enum ViewLayoutEnum
	kTopRightViewCorner           =41474      # from enum ViewLayoutEnum
	kPanViewOperation             =30210      # from enum ViewOperationTypeEnum
	kRotateViewOperation          =30209      # from enum ViewOperationTypeEnum
	kZoomViewOperation            =30211      # from enum ViewOperationTypeEnum
	kArbitraryViewOrientation     =10763      # from enum ViewOrientationTypeEnum
	kBackViewOrientation          =10756      # from enum ViewOrientationTypeEnum
	kBottomViewOrientation        =10757      # from enum ViewOrientationTypeEnum
	kCurrentViewOrientation       =10765      # from enum ViewOrientationTypeEnum
	kDefaultViewOrientation       =10753      # from enum ViewOrientationTypeEnum
	kFlatBacksidePivot180ViewOrientation=10773      # from enum ViewOrientationTypeEnum
	kFlatBacksidePivotLeftViewOrientation=10772      # from enum ViewOrientationTypeEnum
	kFlatBacksidePivotRightViewOrientation=10771      # from enum ViewOrientationTypeEnum
	kFlatBacksideViewOrientation  =10770      # from enum ViewOrientationTypeEnum
	kFlatPivot180ViewOrientation  =10769      # from enum ViewOrientationTypeEnum
	kFlatPivotLeftViewOrientation =10768      # from enum ViewOrientationTypeEnum
	kFlatPivotRightViewOrientation=10767      # from enum ViewOrientationTypeEnum
	kFrontViewOrientation         =10764      # from enum ViewOrientationTypeEnum
	kIsoBottomLeftViewOrientation =10762      # from enum ViewOrientationTypeEnum
	kIsoBottomRightViewOrientation=10761      # from enum ViewOrientationTypeEnum
	kIsoTopLeftViewOrientation    =10760      # from enum ViewOrientationTypeEnum
	kIsoTopRightViewOrientation   =10759      # from enum ViewOrientationTypeEnum
	kLeftViewOrientation          =10758      # from enum ViewOrientationTypeEnum
	kRightViewOrientation         =10755      # from enum ViewOrientationTypeEnum
	kSavedCameraViewOrientation   =10766      # from enum ViewOrientationTypeEnum
	kTopViewOrientation           =10754      # from enum ViewOrientationTypeEnum
	kAllComponentsViewPreview     =70657      # from enum ViewPreviewTypeEnum
	kBoundingBoxViewPreview       =70659      # from enum ViewPreviewTypeEnum
	kPartialViewPreview           =70658      # from enum ViewPreviewTypeEnum
	kBrowserViewType              =9219       # from enum ViewTypeEnum
	kGraphicsViewType             =9218       # from enum ViewTypeEnum
	kNoteBookViewType             =9220       # from enum ViewTypeEnum
	kUnknownViewType              =9217       # from enum ViewTypeEnum
	kAssemblyFeatureGroup         =35073      # from enum WeldmentFeatureGroupEnum
	kMachiningFeatureGroup        =35076      # from enum WeldmentFeatureGroupEnum
	kPreperationsFeatureGroup     =35074      # from enum WeldmentFeatureGroupEnum
	kWeldsFeatureGroup            =35075      # from enum WeldmentFeatureGroupEnum
	kAssemblyWeldmentState        =80897      # from enum WeldmentStateEnum
	kMachiningWeldmentState       =80898      # from enum WeldmentStateEnum
	kPreparationsWeldmentState    =80900      # from enum WeldmentStateEnum
	kWeldsWeldmentState           =80899      # from enum WeldmentStateEnum
	kMaximize                     =32514      # from enum WindowsSizeEnum
	kMinimize                     =32515      # from enum WindowsSizeEnum
	kNormalWindow                 =32513      # from enum WindowsSizeEnum
	kAnalyticEdgeWorkAxis         =12555      # from enum WorkAxisDefinitionEnum
	kAssemblyWorkAxis             =12552      # from enum WorkAxisDefinitionEnum
	kFixedWorkAxis                =12551      # from enum WorkAxisDefinitionEnum
	kLineAndPlaneWorkAxis         =12550      # from enum WorkAxisDefinitionEnum
	kLineAndPointWorkAxis         =12554      # from enum WorkAxisDefinitionEnum
	kLineWorkAxis                 =12545      # from enum WorkAxisDefinitionEnum
	kNormalToSurfaceWorkAxis      =12553      # from enum WorkAxisDefinitionEnum
	kPointAndPlaneWorkAxis        =12549      # from enum WorkAxisDefinitionEnum
	kRevolvedFaceWorkAxis         =12548      # from enum WorkAxisDefinitionEnum
	kTwoPlanesWorkAxis            =12546      # from enum WorkAxisDefinitionEnum
	kTwoPointsWorkAxis            =12547      # from enum WorkAxisDefinitionEnum
	kAssemblyWorkPlane            =12044      # from enum WorkPlaneDefinitionEnum
	kFixedWorkPlane               =12041      # from enum WorkPlaneDefinitionEnum
	kLineAndPointWorkPlane        =12035      # from enum WorkPlaneDefinitionEnum
	kLineAndTangentWorkPlane      =12039      # from enum WorkPlaneDefinitionEnum
	kLinePlaneAndAngleWorkPlane   =12037      # from enum WorkPlaneDefinitionEnum
	kNormalToCurveWorkPlane       =12042      # from enum WorkPlaneDefinitionEnum
	kPlaneAndOffsetWorkPlane      =12038      # from enum WorkPlaneDefinitionEnum
	kPlaneAndPointWorkPlane       =12036      # from enum WorkPlaneDefinitionEnum
	kPlaneAndTangentWorkPlane     =12040      # from enum WorkPlaneDefinitionEnum
	kPointAndTangentWorkPlane     =12045      # from enum WorkPlaneDefinitionEnum
	kThreePointsWorkPlane         =12033      # from enum WorkPlaneDefinitionEnum
	kTorusMidPlaneWorkPlane       =12046      # from enum WorkPlaneDefinitionEnum
	kTwoLinesWorkPlane            =12034      # from enum WorkPlaneDefinitionEnum
	kTwoPlanesWorkPlane           =12043      # from enum WorkPlaneDefinitionEnum
	kAssemblyWorkPoint            =12808      # from enum WorkPointDefinitionEnum
	kCentroidWorkPoint            =12811      # from enum WorkPointDefinitionEnum
	kCurveAndEntityWorkPoint      =12807      # from enum WorkPointDefinitionEnum
	kFixedWorkPoint               =12806      # from enum WorkPointDefinitionEnum
	kLineAndFaceWorkPoint         =12803      # from enum WorkPointDefinitionEnum
	kMidPointWorkPoint            =12805      # from enum WorkPointDefinitionEnum
	kNonLinearEdgeWorkPoint       =12809      # from enum WorkPointDefinitionEnum
	kPointWorkPoint               =12804      # from enum WorkPointDefinitionEnum
	kSphereCenterPointWorkPoint   =12812      # from enum WorkPointDefinitionEnum
	kThreePlanesWorkPoint         =12801      # from enum WorkPointDefinitionEnum
	kTorusCenterPointWorkPoint    =12810      # from enum WorkPointDefinitionEnum
	kTwoLinesWorkPoint            =12802      # from enum WorkPointDefinitionEnum
	kZoomTargetAll                =55811      # from enum ZoomTargetComponentWithiMateEnum
	kZoomTargetNone               =55809      # from enum ZoomTargetComponentWithiMateEnum
	kZoomTargetPlacedComponent    =55810      # from enum ZoomTargetComponentWithiMateEnum
	kCurrentInventorVersionHiveCU =2565       # from enum _RegistryHiveTypeEnum
	kHKEY_CLASSES_ROOT            =2562       # from enum _RegistryHiveTypeEnum
	kHKEY_CURRENT_USER            =2564       # from enum _RegistryHiveTypeEnum
	kHKEY_LOCAL_MACHINE           =2563       # from enum _RegistryHiveTypeEnum
	kInventorHiveCU               =2561       # from enum _RegistryHiveTypeEnum
	kInventorHiveLM               =2560       # from enum _RegistryHiveTypeEnum
	kHalfOpenedSegState           =2          # from enum _SegmentLoadState
	kLoadedSegState               =8          # from enum _SegmentLoadState
	kNotOpenSegState              =0          # from enum _SegmentLoadState
	kOpenedSegState               =4          # from enum _SegmentLoadState
	kPreOpenedSegState            =1          # from enum _SegmentLoadState
	kAdaptiveColumn               =88074      # from enum iComponentColumnTypeEnum
	kBOMQuantityColumn            =88067      # from enum iComponentColumnTypeEnum
	kBOMStructureColumn           =88066      # from enum iComponentColumnTypeEnum
	kExclusionColumn              =88070      # from enum iComponentColumnTypeEnum
	kFilePropertyColumn           =88068      # from enum iComponentColumnTypeEnum
	kFlatPatternBendOrderColumn   =88079      # from enum iComponentColumnTypeEnum
	kFlatPatternOrientationColumn =88078      # from enum iComponentColumnTypeEnum
	kGroundedColumn               =88073      # from enum iComponentColumnTypeEnum
	kMemberNameColumn             =88065      # from enum iComponentColumnTypeEnum
	kParameterValueColumn         =88069      # from enum iComponentColumnTypeEnum
	kSheetMetalRuleColumn         =88080      # from enum iComponentColumnTypeEnum
	kSheetMetalUnfoldColumn       =88081      # from enum iComponentColumnTypeEnum
	kThreadClassColumn            =88084      # from enum iComponentColumnTypeEnum
	kThreadDesignationColumn      =88083      # from enum iComponentColumnTypeEnum
	kThreadDirectionColumn        =88085      # from enum iComponentColumnTypeEnum
	kThreadPipeDiameterColumn     =88086      # from enum iComponentColumnTypeEnum
	kThreadTypeColumn             =88082      # from enum iComponentColumnTypeEnum
	kUnknownColumn                =88087      # from enum iComponentColumnTypeEnum
	kiComponentTableReplaceColumn =88071      # from enum iComponentColumnTypeEnum
	kiFeatureTableReplaceColumn   =88072      # from enum iComponentColumnTypeEnum
	kiMateMatchingListColumn      =88076      # from enum iComponentColumnTypeEnum
	kiMateMatchingNameColumn      =88075      # from enum iComponentColumnTypeEnum
	kiMateSequenceNumberColumn    =88077      # from enum iComponentColumnTypeEnum
	kiFeatureEntityInputTypeCircularEdge=32         # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeCircularSketchCurve=512        # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeConicalSurface=65536      # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeCylindricalSurface=32768      # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeEllipticalSketchCurve=1024       # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeGenericEdge=8          # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeGenericSketchCurve=128        # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeGenericSurface=16384      # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeLinearEdge=16         # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeLinearSketchCurve=256        # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypePlanarFace=4096       # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeSketchPoint=2          # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeSphericalSurface=131072     # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeSplineSketchCurve=2048       # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeToroidalSurface=262144     # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeUnknown=0          # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeVertex=1          # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeWorkAxis=64         # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeWorkPlane=8192       # from enum iFeatureEntityInputTypeEnum
	kiFeatureEntityInputTypeWorkPoint=4          # from enum iFeatureEntityInputTypeEnum
	kParamLimitList               =33283      # from enum iFeatureParamLimitTypeEnum
	kParamLimitNone               =33281      # from enum iFeatureParamLimitTypeEnum
	kParamLimitRange              =33282      # from enum iFeatureParamLimitTypeEnum

RecordMap = {
	###'tagSTATSTG': '{00000000-0000-0000-0000-000000000000}', # Record disabled because it doesn't have a non-null GUID
}

CLSIDToClassMap = {}
CLSIDToPackageMap = {
	'{425458DA-4495-11D3-B791-0060B0F159EF}' : 'AddInAutomation',
	'{5DF8601E-6B16-11D3-B794-0060B0F159EF}' : 'ComponentDefinition',
	'{5DF860AE-6B16-11D3-B794-0060B0F159EF}' : 'SurfaceBodies',
	'{5DF86089-6B16-11D3-B794-0060B0F159EF}' : 'SurfaceBody',
	'{5DF86091-6B16-11D3-B794-0060B0F159EF}' : 'FaceShells',
	'{5DF8608A-6B16-11D3-B794-0060B0F159EF}' : 'FaceShell',
	'{5DF86092-6B16-11D3-B794-0060B0F159EF}' : 'Faces',
	'{5DF8608B-6B16-11D3-B794-0060B0F159EF}' : 'Face',
	'{DA33F1A4-7C3F-11D3-B794-0060B0F159EF}' : 'PartFeature',
	'{790B4EB3-7947-4D08-9510-372E93A24CF1}' : 'AttributeSets',
	'{EFA08B24-F116-4751-90FA-46ADE09BF0B3}' : 'AttributeSet',
	'{BC3487BB-F349-4A6C-9F72-D8C62CBADE6B}' : 'Attribute',
	'{FBCADB33-9CBE-11D3-B799-0060B0F159EF}' : 'DataIO',
	'{1734EB04-2921-11D5-A4C1-00C04F6B9531}' : 'AttributesEnumerator',
	'{5DF86062-6B16-11D3-B794-0060B0F159EF}' : 'Box',
	'{CB69F172-558E-11D3-B793-0060B0F159EF}' : 'Point',
	'{CB69F171-558E-11D3-B793-0060B0F159EF}' : 'Matrix',
	'{CB69F174-558E-11D3-B793-0060B0F159EF}' : 'Vector',
	'{CB69F176-558E-11D3-B793-0060B0F159EF}' : 'UnitVector',
	'{D480B516-E785-4CEE-B43C-FD4E3B6055F4}' : 'RenderStyle',
	'{EF562DD1-92FA-11D4-8DE0-0010B541CAA8}' : 'ComponentOccurrencesEnumerator',
	'{5DF86020-6B16-11D3-B794-0060B0F159EF}' : 'ComponentOccurrence',
	'{AA044AA1-D685-11D3-B7A0-0060B0F159EF}' : 'AssemblyComponentDefinition',
	'{5DF86024-6B16-11D3-B794-0060B0F159EF}' : 'ComponentOccurrences',
	'{6BA435DD-BBD6-11D4-8DE6-0010B541CAA8}' : 'NameValueMap',
	'{66829BB6-656B-431C-BF5C-0BF53DBA225D}' : 'ClientGraphicsCollection',
	'{2B0F6166-711D-47E0-B9B1-54ED9E3F160B}' : 'ClientGraphics',
	'{58614F83-BD65-4B95-9C8B-92280B06D2F1}' : 'GraphicsNode',
	'{EBDAEE90-2DE0-42E5-8AA0-823A643DB4B3}' : 'GraphicsPrimitive',
	'{CB69F173-558E-11D3-B793-0060B0F159EF}' : 'Point2d',
	'{DA33F19F-7C3F-11D3-B794-0060B0F159EF}' : 'Matrix2d',
	'{CB69F175-558E-11D3-B793-0060B0F159EF}' : 'Vector2d',
	'{CB69F177-558E-11D3-B793-0060B0F159EF}' : 'UnitVector2d',
	'{6C312B38-95D8-47B3-A6A8-78942F77A1C7}' : 'LineGraphics',
	'{956DA506-F82D-4924-A000-C1A66CDB3B49}' : 'GraphicsCoordinateSet',
	'{9D2A8D7D-D599-4D54-BDE0-586E5E18880D}' : 'GraphicsIndexSet',
	'{E54B3528-EB27-4A1A-8403-48A9846C93BB}' : 'GraphicsColorSet',
	'{0D084DAB-C766-4595-A449-7625772E88D2}' : 'Color',
	'{D2666468-C11D-42F3-AB1E-6E590C5AA182}' : 'LineStripGraphics',
	'{114E3531-FE3B-4042-A454-372A6B98F26F}' : 'PointGraphics',
	'{FC23373B-FA59-43C7-BD1B-2618DFA1C8C0}' : 'GraphicsImageSet',
	'{F3D4C961-7227-4E32-90A3-C60A9EEFA90D}' : 'TextGraphics',
	'{99CBF031-2FFA-440F-B947-8470CD64E79C}' : 'TriangleFanGraphics',
	'{D8297E9E-DD8B-4C8D-9271-186CAE8E00C1}' : 'GraphicsNormalSet',
	'{AFA9F4D2-A1D8-42C3-8BFA-994FFAB1BEA4}' : 'GraphicsColorMapper',
	'{FFA15510-CD22-4C40-8DEE-4F846C3D5470}' : 'GraphicsTextureCoordinateSet',
	'{B5E1C129-EE0E-4C45-9AC3-FE79794F1EB0}' : 'TriangleGraphics',
	'{907F6639-A091-4B19-B1B4-E677D960934C}' : 'TriangleStripGraphics',
	'{6757C085-699B-474B-9566-61221A64A09F}' : 'FeatureGraphics',
	'{9AB0A7C1-DDEE-400D-B526-287FB2EB6DDD}' : 'CurveGraphics',
	'{807562AB-40E2-47D3-9FDC-E74E2D1E5724}' : 'ViewList',
	'{70109AA3-63C1-11D2-B78B-0060B0EC020B}' : 'View',
	'{70109AA1-63C1-11D2-B78B-0060B0EC020B}' : 'Document',
	'{6E5CDAB2-6BA5-4EAD-B357-78646BE0A813}' : 'File',
	'{C64DD969-DCB0-4FA9-AD0A-E09744466D61}' : 'FileDescriptorsEnumerator',
	'{67CF708B-CA38-419D-8016-19CEAA5FBB7D}' : 'FileDescriptor',
	'{4771DB69-A789-4BA4-A35C-56BFCC6AECFA}' : 'FilesEnumerator',
	'{DBD3CBEE-DBBC-4A71-B122-33A8D1786D20}' : 'DocumentDescriptorsEnumerator',
	'{D755CFCA-9E02-4A08-AFE8-7178E818C763}' : 'DocumentDescriptor',
	'{ACE59077-7778-11D4-8DD8-0010B541CAA8}' : 'DocumentsEnumerator',
	'{70109AA4-63C1-11D2-B78B-0060B0EC020B}' : 'Views',
	'{3D218008-FA54-48CB-89BC-8EFBF3D0B6CC}' : 'ClientViews',
	'{BCD3EFAF-0FEF-4AC1-8303-2A4BF18E96FC}' : 'ClientView',
	'{9C88D3AD-C3EB-11D3-B79E-0060B0F159EF}' : 'Camera',
	'{1F6B29F0-6C04-4D11-8ACE-9D41C2904FCD}' : 'DocumentEventsObject',
	'{851B66FA-B31A-453D-8628-2DE2A5768C59}' : 'DocumentEventsSink',
	'{70109AAC-63C1-11D2-B78B-0060B0EC020B}' : 'DocumentEvents',
	'{9CAF98A0-33EA-11D3-B78F-0060B0F159EF}' : 'ReferencedOLEFileDescriptors',
	'{9CAF989F-33EA-11D3-B78F-0060B0F159EF}' : 'ReferencedOLEFileDescriptor',
	'{A94DCF5E-90E9-4F60-BB55-F65B4618ECD5}' : 'ObjectsEnumerator',
	'{5076EA3C-FC27-499D-BEC8-B57BD219F0A7}' : 'ReferencedOpaqueFileDescriptors',
	'{5076EA3B-FC27-499D-BEC8-B57BD219F0A7}' : 'ReferencedOpaqueFileDescriptor',
	'{076C16D1-4994-11D4-9E0F-0010A4C72F07}' : 'SoftwareVersion',
	'{73F35CC8-ED6E-11D2-B785-0060B0F159EF}' : 'PropertySets',
	'{73F35CC7-ED6E-11D2-B785-0060B0F159EF}' : 'PropertySet',
	'{73F35CC9-ED6E-11D2-B785-0060B0F159EF}' : 'Property',
	'{46D51BD4-B58D-4C94-BA7A-124B184AC687}' : 'AttributeManager',
	'{1734EB03-2921-11D5-A4C1-00C04F6B9531}' : 'AttributeSetsEnumerator',
	'{6939FFDD-BA10-11D2-B779-0060B0F159EF}' : 'ObjectCollection',
	'{D007B6F9-71BB-48FF-B14C-EE5D633CB0C3}' : 'UnitsOfMeasure',
	'{C52EE54D-B18E-4CB3-AEE3-7D0375F92948}' : 'ParametersEnumerator',
	'{44E517BC-D882-4AFE-A300-B3DAC6B8DB58}' : 'Parameter',
	'{C13EA1C0-2DD0-4B64-9938-0E4804316912}' : 'ExpressionList',
	'{77B88412-A66B-43BE-BEE2-06CFE38B0C70}' : 'Tolerance',
	'{B2EC7987-2BDE-47F6-8EE7-534C7B854B2B}' : 'CustomPropertyFormat',
	'{69190E26-316F-47BD-AE75-8B64641C18C8}' : 'PrintManager',
	'{8C2CC3CF-A455-40D6-8505-56A702F6FB77}' : 'GraphicsDataSetsCollection',
	'{400A64D5-7150-42F6-943E-F190518265CA}' : 'GraphicsDataSets',
	'{D4BF045D-8DFB-44B5-9FFC-FE6ACADF2B23}' : 'GraphicsDataSet',
	'{1F76C4FA-DB71-4D87-8390-1529297ED5A9}' : 'RenderStyles',
	'{1EBEC999-3A4D-4A4C-A35A-3F2E773DD56D}' : 'BrowserPanes',
	'{21F02BD0-F849-49E1-A1EC-A04A8F49AE05}' : 'BrowserPaneObject',
	'{619680F8-EB9A-4F13-8D23-721FE776C955}' : 'BrowserPaneSink',
	'{D99ADCF5-8187-4381-979E-499E017C7C0C}' : 'BrowserPane',
	'{5D21C290-CB28-4861-9367-C3F1B9F0BCCB}' : 'BrowserNode',
	'{E9E1E669-7C31-486B-A5A6-FD0825ABCB28}' : 'BrowserNodeDefinition',
	'{76B0EC66-F962-4D22-9E96-3D02F49AD363}' : 'BrowserNodesEnumerator',
	'{70109AA0-63C1-11D2-B78B-0060B0EC020B}' : 'Application',
	'{70109AA2-63C1-11D2-B78B-0060B0EC020B}' : 'Documents',
	'{6ED45F3A-BAF4-41FE-8907-970BB3CA48DF}' : 'ApplicationEventsObject',
	'{CD4C47ED-C403-4F42-B3BF-0A90F3E89D81}' : 'ApplicationEventsSink',
	'{70109AAD-63C1-11D2-B78B-0060B0EC020B}' : 'ApplicationEvents',
	'{CCEBC8A5-7171-47B6-B9DC-067DAC0C79E7}' : 'WebView',
	'{9A14B139-7101-40B1-BD92-B3F9870DC7F0}' : 'DesignProject',
	'{0B13DE4E-2371-408F-AF1A-F884A9061ED9}' : 'ContentCenterConfiguration',
	'{CF66D521-D40D-477C-A686-D2D5A614D323}' : 'IntentConfiguration',
	'{7B4F757F-55D3-4078-9AED-61AD15AC9AD5}' : 'ProjectPaths',
	'{F8D97A2E-CC4D-49EF-8FFF-F16F2FB13929}' : 'ProjectPath',
	'{4A60CB5E-1EE8-4180-A801-194704F3021E}' : 'DesignProjectManager',
	'{131DB1C8-39A0-41F6-B881-9B49050D08DC}' : 'DesignProjects',
	'{4F599909-D43A-4090-BC23-3616A075A02D}' : 'ProjectOptionsButtonObject',
	'{0C946530-B275-481A-9573-6CA7D4F93611}' : 'ProjectOptionsButtonSink',
	'{A4791D9E-EEA1-4524-8543-174DA9CC42B3}' : 'ProjectOptionsButton',
	'{C6EEC114-BE48-4323-B58C-9DF90ED92996}' : 'ProjectAssetLibrary',
	'{EC5AD11E-A3AB-4C86-85BD-61DEBF623987}' : 'ProjectAssetLibraries',
	'{A50B89A5-B9C9-449C-AD62-813F12D80A5D}' : 'ModelingEventsObject',
	'{124B76C3-CB79-4414-9CB9-DDA2F8C5C90A}' : 'ModelingEventsSink',
	'{B0128AFD-14AE-4FD6-AED0-314D1F79F3EB}' : 'ModelingEvents',
	'{BB91C845-BD7E-4470-948F-C5A069B21BBC}' : 'ClientFeature',
	'{44A143D3-13C8-4B0A-AE53-CCC6169C44DB}' : 'FeatureDimensions',
	'{6C0C1E47-E731-4ECF-8EDD-EF8CE58E395E}' : 'FeatureDimension',
	'{766A9447-A604-43C8-9393-2D2709837D1E}' : 'Asset',
	'{C6E1E6AB-897D-4CDD-A486-4ABAA04FC9B9}' : 'AssetValue',
	'{25E59F53-ADFB-4B1B-8CF4-C8EAE80CA85F}' : 'AssetCategory',
	'{BE5F1900-C9E6-49B4-BA3A-1BC7FF49DCD0}' : 'AssetLibrary',
	'{047360BD-1872-4C10-8538-01518FD7F750}' : 'AssetCategories',
	'{505BB0CA-670E-4D54-AB26-F66A64DBB72C}' : 'AssetsEnumerator',
	'{0A1F6F03-BA19-49CD-8376-93A85FB08A2A}' : 'ClientFeatureDefinition',
	'{112F95FB-41E9-466C-9ACC-1074F5512831}' : 'ClientFeatureElements',
	'{BA8A81FD-71F7-4BE4-A009-1CC6731723FD}' : 'ClientFeatureElement',
	'{9789E1AC-1767-4225-96DD-FD06F614AD59}' : 'ModelAnnotations',
	'{089C1D07-A3A6-4649-B1C4-CE9DAB1D8BBE}' : 'ModelAnnotation',
	'{6E94434B-5CEC-4CC5-AB2E-B37904E7264E}' : 'ModelCompositeAnnotation',
	'{CEBC9A45-2058-4537-9D52-5E11419267DE}' : 'ModelToleranceFeature',
	'{A342F0A8-2B29-44B8-BB55-C6A89EC0A977}' : 'ModelToleranceFeatureDefinition',
	'{8F656C43-9BFD-4BAE-AF23-A21067DDED8E}' : 'ModelAnnotationsEnumerator',
	'{24B7B991-46D9-45F8-82CD-05212ECFC6DD}' : 'FaceCollection',
	'{E0AE1A27-0BDD-442C-8A74-92F5E6F1E839}' : 'ModelToleranceFeaturesEnumerator',
	'{F874F2B3-E7C0-434A-BC00-DE5E1B687452}' : 'ModelCompositeAnnotationDefinition',
	'{01711A84-0018-4452-A736-D9292E754D38}' : 'ModelFeatureControlFrames',
	'{F2948971-943D-4CBB-88B0-20E0B48B8573}' : 'ModelFeatureControlFrame',
	'{CD675FA9-2F1B-4574-B287-C0C601CCC1B1}' : 'ModelFeatureControlFrameDefinition',
	'{FAF83927-A3E9-4ABC-BBCF-AA1D983010F8}' : 'AnnotationPlane',
	'{740E1B50-7EC5-4C4E-B94B-CCEB4FB5C489}' : 'AnnotationPlaneDefinition',
	'{CB69F178-558E-11D3-B793-0060B0F159EF}' : 'Line',
	'{5DF860B0-6B16-11D3-B794-0060B0F159EF}' : 'CurveEvaluator',
	'{CB69F17A-558E-11D3-B793-0060B0F159EF}' : 'Plane',
	'{5DF860B2-6B16-11D3-B794-0060B0F159EF}' : 'SurfaceEvaluator',
	'{5DF86063-6B16-11D3-B794-0060B0F159EF}' : 'Box2d',
	'{181A614B-8F7D-4E15-BCF9-08ECC5F225E2}' : 'ModelFeatureControlFrameRows',
	'{D0F606AE-494C-4810-8280-071F5A56824F}' : 'ModelFeatureControlFrameRow',
	'{EB143431-FB4F-4B4B-BDDA-C21026571456}' : 'ModelDatumIdentifier',
	'{0B87CDBE-3271-46A7-9C95-259667C9FFCF}' : 'ModelDatumIdentifierDefinition',
	'{56B990B9-D25A-436F-A652-1D21EC739C57}' : 'GeometryIntent',
	'{F2E7C272-A777-41B1-B217-C31B8CFAEF77}' : 'ModelLeader',
	'{7430CE13-37A3-4A67-A645-2AAD0BB71038}' : 'ModelLeaderNode',
	'{76A8F762-B6B5-4B18-916C-EC7C17B22618}' : 'ModelLeaderNodesEnumerator',
	'{5FCCBA74-9BA4-49C7-95D3-FC9E7D76EFB3}' : 'ModelSurfaceTextureSymbols',
	'{E083158B-C56B-4CB0-B637-C56896BDAF1C}' : 'ModelSurfaceTextureSymbol',
	'{85B493F3-342B-4D54-83A1-4EF9C50378D0}' : 'ModelSurfaceTextureSymbolDefinition',
	'{7AD96A84-A539-4220-B9AD-7A2854D518B8}' : 'ModelDimensions',
	'{29C4F94E-2656-4727-8510-2B0DAF6FCEFE}' : 'AngularModelDimensions',
	'{1BFD9261-5C05-4BF4-9A9F-F5323F3C8E69}' : 'AngularModelDimension',
	'{4062D31A-F8CE-4D38-B50A-6D8B1FB50D94}' : 'ModelDimensionDefinition',
	'{C66A1C65-43C3-4F1C-A22C-089F3F03349A}' : 'ModelDimension',
	'{B513304D-05B5-4DD7-AA23-E4BF2F120406}' : 'ModelAnnotationText',
	'{607CC753-5796-4409-85F4-9EA576EAA417}' : 'LineSegment',
	'{A765255E-0264-4316-9F81-F5B051281001}' : 'AngularModelDimensionDefinition',
	'{17BE1D0D-0A2B-4A92-9CB2-A9725D391143}' : 'DiameterModelDimensions',
	'{098FDC37-8060-4944-AD0E-B55FEC55CA8C}' : 'DiameterModelDimension',
	'{5FCEA8CE-F9AE-4216-8AAD-2530EC41B619}' : 'DiameterModelDimensionDefinition',
	'{D60D7065-70F2-4E41-AE17-17E36EE573DF}' : 'LinearModelDimensions',
	'{7D6FF00B-9613-4E95-AA2F-484E089AAEA3}' : 'LinearModelDimension',
	'{84385A0E-4B73-48FE-B948-CB83894F2E61}' : 'LinearModelDimensionDefinition',
	'{7C6BCC40-95D1-4B47-AE7F-A5EBFEF95851}' : 'RadiusModelDimensions',
	'{672C4DAF-1B67-4131-8F53-9274F42E44E9}' : 'RadiusModelDimension',
	'{62D66B29-1EA9-48CA-A6C6-6D6FF7785213}' : 'RadiusModelDimensionDefinition',
	'{C5BF9314-D319-44A4-BDFF-16142CE92D58}' : 'ModelHoleThreadNotes',
	'{2BAE3F08-F0AE-4B03-A432-E3A3C22408F6}' : 'ModelHoleThreadNote',
	'{90ED1343-7C9E-4042-9664-93D821AF88CC}' : 'ModelHoleThreadNoteDefinition',
	'{59B2196B-616D-41FC-A7B9-FFAD0334B48D}' : 'HoleClearanceInfo',
	'{B97AC4F4-708A-431E-90BA-AFDCC6623A84}' : 'ModelLeaderNotes',
	'{5194100D-435F-4C85-A922-6BD3E4CC9C36}' : 'ModelLeaderNote',
	'{3614BB38-60E8-42E0-84E1-A0045BFB25D4}' : 'ModelLeaderNoteDefinition',
	'{498E2A5A-76DD-4059-BB54-300D026EC79D}' : 'ModelDatumIdentifiers',
	'{FA169DD0-A365-49D9-9572-F0F23F2B634E}' : 'AnnotationPlaneDefinitionsEnumerator',
	'{45EEBC4D-5D77-4D15-A138-4522B26F1631}' : 'ModelCompositeAnnotations',
	'{0C71D10A-6A99-42EB-8563-6D7F2DD934EF}' : 'ModelGeneralNotes',
	'{88C68B3A-B9B0-45DD-873C-FA0187B80E62}' : 'ModelGeneralNote',
	'{6EE0926D-4482-4469-8AE3-C90231C60713}' : 'ModelGeneralNoteDefinition',
	'{828F3709-2B6A-4CCE-942D-DC8A3FD92D44}' : 'GeneralNoteSymbolDefinitions',
	'{949C0CAF-E83D-4AEB-B734-7DA77D913967}' : 'GeneralNoteSymbolDefinition',
	'{0CB0F042-1627-49BF-B430-619A3AD6FADC}' : 'SketchEventsObject',
	'{3B71CB69-62FB-40D1-BEF9-3B0C255C8DD4}' : 'SketchEventsSink',
	'{579B848D-41FD-4A4E-87F8-58A213360623}' : 'SketchEvents',
	'{5FDB5E25-C96F-11D5-8DF9-0010B541CAA8}' : 'Sketch',
	'{8006A072-ECC4-11D4-8DE9-0010B541CAA8}' : 'GeometricConstraints',
	'{B5461257-09AA-11D5-8DEC-0010B541CAA8}' : 'GeometricConstraint',
	'{8006A074-ECC4-11D4-8DE9-0010B541CAA8}' : 'CoincidentConstraint',
	'{B546124D-09AA-11D5-8DEC-0010B541CAA8}' : 'SketchEntity',
	'{8006A026-ECC4-11D4-8DE9-0010B541CAA8}' : 'SketchConstraintsEnumerator',
	'{DD8AB7FC-77D4-4EA8-83A9-A0C868DABFC0}' : 'ReferenceComponent',
	'{9E0BA9CA-E916-11D2-B785-0060B0F159EF}' : 'ReferencedFileDescriptor',
	'{9FEBA8BF-6BB5-421E-82DE-F1C4A1639C70}' : 'Layer',
	'{1A58DFEF-0B8C-44DF-97AF-4DAC85734B04}' : 'DrawingStylesManager',
	'{415A6C89-2B25-4884-B2E3-78BC8CAB9AC2}' : 'DrawingStandardStylesEnumerator',
	'{55DBDB4E-BC61-4D53-84F6-86CF24267DD8}' : 'DrawingStandardStyle',
	'{A5AFB9DC-4066-4800-A459-E4A7E4E433B6}' : 'Style',
	'{E8528224-258B-471F-81E3-1F276425BC39}' : 'ObjectDefaultsStyle',
	'{3697D2E9-C4C2-4FF5-A60D-F5EC68EACD27}' : 'DimensionStyle',
	'{A907AEC1-A78F-11D5-8DF8-0010B541CAA8}' : 'TextStyle',
	'{7E4D60AD-496E-4336-96AA-5A2C6178C836}' : 'LeaderStyle',
	'{04B1FC27-4477-491B-A640-3C313E9AC402}' : 'BalloonStyle',
	'{9CB10C50-7F27-4E55-BADE-15A308DB8820}' : 'FeatureControlFrameStyle',
	'{97B2D2E2-78EA-4838-B140-2BBAB4D8E7A9}' : 'HoleTableStyle',
	'{F329734C-AAC4-40B9-A1A0-A051679C1EC7}' : 'SurfaceTextureStyle',
	'{AD4D6527-A103-4FF5-8433-FB90C52B9473}' : 'CentermarkStyle',
	'{A957DFC5-7AC5-497F-A7AF-5438FAFAD6B4}' : 'TableStyle',
	'{6C65399A-B4E9-42DB-8659-6E13E4B07050}' : 'PartsListStyle',
	'{4758367B-5DAF-4CE3-BDF1-189FAD8D6BD2}' : 'RevisionTableStyle',
	'{0134748C-7F24-467B-9DF2-6647677B125F}' : 'DimensionStylesEnumerator',
	'{29F0D467-C114-11D2-B77F-0060B0F159EF}' : 'DrawingDocument',
	'{1405C19D-F8AC-41AD-AAB2-D0923BD45C15}' : 'ReferenceKeyManager',
	'{189559A8-0C9B-4F77-93E9-8330AAAD7943}' : 'SelectSet',
	'{1907E11C-C275-4008-95FA-9AC7539E1A7C}' : 'SelectionPreferences',
	'{95C6C576-FC7A-4B16-B565-BFABEF69B013}' : 'InventorVBAProject',
	'{24FAC734-1A3D-404E-A28B-7CC1AD47DCA1}' : 'InventorVBAComponents',
	'{611EDF7B-009C-4871-B3F9-69E1B4A61C1E}' : 'InventorVBAComponent',
	'{E83434B4-B12D-4A6F-A2DC-BFA52D3C5FA7}' : 'InventorVBAMembers',
	'{FBC2D851-EC7F-4D70-B13C-98B57B785E97}' : 'InventorVBAMember',
	'{BAB06F80-7165-484C-88DF-7D8A0004A76D}' : 'InventorVBAArguments',
	'{25944748-FC4C-4214-A0AC-627BDF178793}' : 'InventorVBAArgument',
	'{D3EDB5BC-7B47-42B9-9D77-F3A2676EC15B}' : 'DocumentSubType',
	'{545F2567-592E-45DA-A262-77BD7E546F7A}' : 'HighlightSet',
	'{B1DA2E33-F616-41D4-917A-CEB1138058D0}' : 'DocumentInterests',
	'{36DB2A89-F970-4C03-AA8A-7864122D553B}' : 'DocumentInterest',
	'{AAF23B5F-E2FE-471C-85AA-E37FCE6DE651}' : '_DocPerformanceMonitorObject',
	'{C2083475-A259-414A-BED9-FC43291F4455}' : '_DocPerformanceMonitorSink',
	'{89832854-67B3-4DBF-B8E6-715435D51FE2}' : '_DocPerformanceMonitor',
	'{AE621339-6CA8-486C-BF06-E683D2EE3A8E}' : '_SegPerformanceMonitor',
	'{9E0BA9CB-E916-11D2-B785-0060B0F159EF}' : 'ReferencedFileDescriptors',
	'{DD60CA37-AB7B-491F-AD9E-C9DF3B4B5BBB}' : 'HighlightSets',
	'{206B59AE-22A6-11D4-B7A8-0060B0F159EF}' : 'Sheet',
	'{206B59B2-22A6-11D4-B7A8-0060B0F159EF}' : 'DrawingViews',
	'{206B59B1-22A6-11D4-B7A8-0060B0F159EF}' : 'DrawingView',
	'{1644E1D7-9BD5-11D5-8DF7-0010B541CAA8}' : 'DrawingSketches',
	'{1644E1D5-9BD5-11D5-8DF7-0010B541CAA8}' : 'DrawingSketch',
	'{C173A075-012F-11D5-8DEA-0010B541CAA8}' : 'DimensionConstraints',
	'{B5461259-09AA-11D5-8DEC-0010B541CAA8}' : 'DimensionConstraint',
	'{C173A077-012F-11D5-8DEA-0010B541CAA8}' : 'OffsetDimConstraint',
	'{8006A016-ECC4-11D4-8DE9-0010B541CAA8}' : 'SketchLine',
	'{B546124B-09AA-11D5-8DEC-0010B541CAA8}' : 'SketchEntitiesEnumerator',
	'{08A3AC40-A684-4F8B-8033-7D0FE23AFBE3}' : 'SketchBlock',
	'{2C9F06C7-9124-43FE-B6D9-703620D53DA7}' : 'SketchBlocksEnumerator',
	'{F393AB2C-8A8B-4B69-9F0D-91FFA842A53F}' : 'SketchBlockDefinition',
	'{8006A032-ECC4-11D4-8DE9-0010B541CAA8}' : 'SketchArcs',
	'{8006A046-ECC4-11D4-8DE9-0010B541CAA8}' : 'SketchArc',
	'{8006A022-ECC4-11D4-8DE9-0010B541CAA8}' : 'SketchPoint',
	'{C173A091-012F-11D5-8DEA-0010B541CAA8}' : 'Arc2d',
	'{5DF860B1-6B16-11D3-B794-0060B0F159EF}' : 'Curve2dEvaluator',
	'{744FFECE-189A-4ACC-8BCF-8F959D5E4EAE}' : 'Arc3d',
	'{8006A018-ECC4-11D4-8DE9-0010B541CAA8}' : 'SketchLines',
	'{8006A024-ECC4-11D4-8DE9-0010B541CAA8}' : 'SketchPoints',
	'{8006A034-ECC4-11D4-8DE9-0010B541CAA8}' : 'SketchSplines',
	'{8006A048-ECC4-11D4-8DE9-0010B541CAA8}' : 'SketchSpline',
	'{49CB4BBA-872A-11D3-8524-0060B0F0B5B7}' : 'BSplineCurve2d',
	'{1236D237-9BAC-4399-8CFB-66CB6B7FD5CA}' : 'SketchSplineHandle',
	'{C173A08D-012F-11D5-8DEA-0010B541CAA8}' : 'LineSegment2d',
	'{49CB4BB9-872A-11D3-8524-0060B0F0B5B7}' : 'BSplineCurve',
	'{16372AAE-1133-4C4C-9A48-D9305D8358F3}' : 'SketchOffsetSplines',
	'{063D7617-E630-4D35-B809-64D6695F57C0}' : 'SketchOffsetSpline',
	'{8006A036-ECC4-11D4-8DE9-0010B541CAA8}' : 'SketchEllipses',
	'{8006A04A-ECC4-11D4-8DE9-0010B541CAA8}' : 'SketchEllipse',
	'{49CB4BB8-872A-11D3-8524-0060B0F0B5B7}' : 'EllipseFull2d',
	'{49CB4BB7-872A-11D3-8524-0060B0F0B5B7}' : 'EllipseFull',
	'{C173A089-012F-11D5-8DEA-0010B541CAA8}' : 'SketchEllipticalArcs',
	'{C173A087-012F-11D5-8DEA-0010B541CAA8}' : 'SketchEllipticalArc',
	'{C173A095-012F-11D5-8DEA-0010B541CAA8}' : 'EllipticalArc2d',
	'{C1066E40-4E2F-45C2-A5AB-E2B4D1B84A1E}' : 'EllipticalArc',
	'{8006A038-ECC4-11D4-8DE9-0010B541CAA8}' : 'SketchCircles',
	'{8006A04C-ECC4-11D4-8DE9-0010B541CAA8}' : 'SketchCircle',
	'{49CB4BB6-872A-11D3-8524-0060B0F0B5B7}' : 'Circle2d',
	'{49CB4BB5-872A-11D3-8524-0060B0F0B5B7}' : 'Circle',
	'{A907AE97-A78F-11D5-8DF8-0010B541CAA8}' : 'TextBoxes',
	'{A907AE99-A78F-11D5-8DF8-0010B541CAA8}' : 'TextBox',
	'{6359FE67-0814-4847-9F33-72E0BB9EB688}' : 'SketchFixedSplines',
	'{DCEF44A1-7A80-4A0A-937C-A349AF8A9233}' : 'SketchFixedSpline',
	'{64D6BFDF-5B47-48C1-AC74-1BE2C24757B2}' : 'SketchImages',
	'{C00FE3F4-2D75-4409-93FB-9B72913C073C}' : 'SketchImage',
	'{135F0952-BF41-444D-A962-8A7805AB2E78}' : 'SketchControlPointSplines',
	'{D5F8CF99-AF1F-4089-A638-F6889762C1D6}' : 'SketchControlPointSpline',
	'{C38DE680-2374-487B-86F8-E3DA8012DE66}' : 'SketchEquationCurves',
	'{6D7C3BDC-9CE1-4F23-82CC-2F001A326F89}' : 'SketchEquationCurve',
	'{523EF757-245A-11D5-8DEC-0010B541CAA8}' : 'Profiles',
	'{8006A03A-ECC4-11D4-8DE9-0010B541CAA8}' : 'Profile',
	'{B5461253-09AA-11D5-8DEC-0010B541CAA8}' : 'ProfilePath',
	'{B5461255-09AA-11D5-8DEC-0010B541CAA8}' : 'ProfileEntity',
	'{4735D53B-FEF2-4671-9430-3D60964D850B}' : 'RegionProperties',
	'{31B11F76-0E31-45DF-8BE6-409EE5416DC5}' : 'Wires',
	'{A267D26D-EA7D-444F-8D54-7316BF10DD96}' : 'Wire',
	'{5DF86094-6B16-11D3-B794-0060B0F159EF}' : 'EdgeUses',
	'{5DF8608D-6B16-11D3-B794-0060B0F159EF}' : 'EdgeUse',
	'{5DF8608E-6B16-11D3-B794-0060B0F159EF}' : 'Edge',
	'{5DF8608F-6B16-11D3-B794-0060B0F159EF}' : 'Vertex',
	'{5DF86095-6B16-11D3-B794-0060B0F159EF}' : 'Edges',
	'{8DC730F1-A15F-4547-A279-69B7A9FAE657}' : 'EdgeCollection',
	'{5DF8608C-6B16-11D3-B794-0060B0F159EF}' : 'EdgeLoop',
	'{2C16787F-83FF-11D4-8DDB-0010B541CAA8}' : 'PlanarSketch',
	'{3C83A20C-1648-40C3-9A28-FFDE72124D2C}' : 'ProjectedCuts',
	'{21E8F0AC-DFCD-4800-B07A-6E0C492CC447}' : 'ProjectedCut',
	'{A9C5B884-2122-4DBB-A94E-EB75ED78A160}' : 'SketchBlocks',
	'{C173A079-012F-11D5-8DEA-0010B541CAA8}' : 'TwoPointDistanceDimConstraint',
	'{C173A07B-012F-11D5-8DEA-0010B541CAA8}' : 'TwoLineAngleDimConstraint',
	'{C173A07D-012F-11D5-8DEA-0010B541CAA8}' : 'ThreePointAngleDimConstraint',
	'{C173A07F-012F-11D5-8DEA-0010B541CAA8}' : 'DiameterDimConstraint',
	'{C173A081-012F-11D5-8DEA-0010B541CAA8}' : 'RadiusDimConstraint',
	'{FD350F5E-E3C9-4268-BCF4-0DEA91B6F8EF}' : 'ArcLengthDimConstraint',
	'{C173A085-012F-11D5-8DEA-0010B541CAA8}' : 'TangentDistanceDimConstraint',
	'{6ABB821F-4962-11D5-8DEE-0010B541CAA8}' : 'EllipseRadiusDimConstraint',
	'{BBCEA345-055B-4625-ABCA-582C6BF7E440}' : 'OffsetSplineDimConstraint',
	'{A7993C2A-CFCA-4455-BC79-B15952DBF102}' : 'SketchFillRegions',
	'{920C0497-59BF-4F6C-A45C-8C8AA72750CF}' : 'SketchFillRegion',
	'{E72E9ED9-8A10-4292-9792-96FA51ECD810}' : 'AutomatedCenterlineSettings',
	'{E49C9290-6D71-4C14-8B15-3595306A49D6}' : 'DrawingCurvesEnumerator',
	'{1C98EA42-27FC-4BFA-84E4-D29C7A11F889}' : 'DrawingCurve',
	'{D05367DD-3A18-47DC-A618-7550582CEEDA}' : 'DrawingCurveSegments',
	'{EEE9F58F-FD0B-4862-AE21-BAE203DFE23E}' : 'DrawingCurveSegment',
	'{1DA08DFE-88EB-4ABE-8FA8-34FD098D65AA}' : 'DrawingViewEventsObject',
	'{F777456B-314C-4F8E-87E0-196CB7FC8D32}' : 'DrawingViewEventsSink',
	'{4A1FD94B-337F-43F7-AA7C-BA33B076B1EB}' : 'DrawingViewEvents',
	'{C9216F3D-E886-4E75-89AB-D7665FA14AB1}' : 'DrawingViewLabel',
	'{96E36D73-DFEC-4CF8-9DB3-F97F01A41A23}' : 'OriginIndicator',
	'{1880ABD8-B826-4258-A2F1-31B5E5740FA6}' : 'BreakOperations',
	'{ABCACDBB-5EAF-4AF5-86A0-FB2DB0502D5D}' : 'BreakOperation',
	'{600D4AE6-12FB-47E9-86E6-46C8C2A9161E}' : 'BreakOutOperations',
	'{5D175430-8A8D-47F7-AABE-50C2E9B65D89}' : 'BreakOutOperation',
	'{9CF770DE-2A15-4069-A057-AB247ACCFAFC}' : 'SectionDrawingView',
	'{3B39A185-9BED-4494-993C-26762D8A2D5F}' : 'DetailDrawingView',
	'{A907AE85-A78F-11D5-8DF8-0010B541CAA8}' : 'PartsLists',
	'{A907AE87-A78F-11D5-8DF8-0010B541CAA8}' : 'PartsList',
	'{A907AE89-A78F-11D5-8DF8-0010B541CAA8}' : 'PartsListColumns',
	'{A907AE8B-A78F-11D5-8DF8-0010B541CAA8}' : 'PartsListColumn',
	'{A907AE8D-A78F-11D5-8DF8-0010B541CAA8}' : 'PartsListRows',
	'{A907AE8F-A78F-11D5-8DF8-0010B541CAA8}' : 'PartsListRow',
	'{A907AE91-A78F-11D5-8DF8-0010B541CAA8}' : 'PartsListCell',
	'{3DFE3282-5B67-431A-A890-040098957C1C}' : 'Balloons',
	'{A5F6343C-7FE9-431E-BF12-A7308A57CE91}' : 'Balloon',
	'{B3721DAB-0BAD-4296-8C1E-6608FC0F6049}' : 'BalloonValueSets',
	'{380ED49C-ADD8-47EC-B99E-10D00CE618D7}' : 'BalloonValueSet',
	'{3538A9B3-0A9F-4B3E-9FC9-3272AB0D7C2B}' : 'DrawingBOMRow',
	'{148682B7-6B44-4FF0-8C10-AB21D276602E}' : 'BOMRow',
	'{C5AC2A12-6439-4CB5-BA1E-45765296285E}' : 'ComponentDefinitionsEnumerator',
	'{BCDD5058-E7D5-4E88-8EF8-8D6370E0CBA3}' : 'BOMRowsEnumerator',
	'{2FBF7141-4414-423B-9F95-3C6489DC47B9}' : 'DrawingBOMCell',
	'{1290504E-696F-4480-8126-04A65C7DA45E}' : 'DrawingBOM',
	'{F78F8237-3CAA-467D-AB38-6998DF84B3BE}' : 'DrawingBOMColumns',
	'{A36A7AD1-DDBD-4858-B025-D3F6C2042BC8}' : 'DrawingBOMColumn',
	'{6ADEEB5C-21C6-4995-91AA-7FD0CE1D0073}' : 'DrawingBOMRows',
	'{77D4A0A3-255E-42A8-B0F5-41FE5007BCCE}' : 'Leader',
	'{48F6DB32-6623-4944-BBF1-12A26E47107A}' : 'LeaderNode',
	'{26C1C5B1-44AE-4180-8118-EDF2B8CB220B}' : 'LeaderNodesEnumerator',
	'{A907AEB9-A78F-11D5-8DF8-0010B541CAA8}' : 'TitleBlock',
	'{A907AEB7-A78F-11D5-8DF8-0010B541CAA8}' : 'TitleBlockDefinition',
	'{A907AEAF-A78F-11D5-8DF8-0010B541CAA8}' : 'Border',
	'{A907AEB3-A78F-11D5-8DF8-0010B541CAA8}' : 'BorderDefinition',
	'{2A6C1D0D-FAF8-4A31-A9FB-39761F36F814}' : 'CustomTables',
	'{88F528C1-AE9A-457B-8A19-A6224F473A62}' : 'CustomTable',
	'{151E96E1-59DA-4732-B025-4AA7A1C9AF27}' : 'Columns',
	'{70984603-E322-4AC8-B6DE-2F5A31AF0910}' : 'Column',
	'{2022FEE8-01DA-481F-A515-D2D89C787EA8}' : 'Rows',
	'{8AF87EC1-B613-43DB-9FF6-E0D489B68DAE}' : 'Row',
	'{CE3FEA37-5793-4814-B9E4-88C84DC0BEEE}' : 'Cell',
	'{A2F174A9-9D82-4AF1-B80C-67FB45B59923}' : 'TableFormat',
	'{DB2B25D3-66F3-47CC-9DBF-D6B7468EE76E}' : 'RevisionTables',
	'{644AE247-EFBA-49FA-9F55-384CA82DB549}' : 'RevisionTable',
	'{CBC02A91-4346-4459-8A47-C845B0A4051F}' : 'RevisionTableColumns',
	'{C802F139-6C51-4A73-ABAE-BF5E88687E00}' : 'RevisionTableColumn',
	'{C5EDE080-C83A-4D7F-9560-B867FD29DFD6}' : 'RevisionTableRows',
	'{FB83111D-DED9-462D-9BC5-95A6933ADF4C}' : 'RevisionTableRow',
	'{63C5D5FD-8348-4246-BE53-619E8C48EC6F}' : 'RevisionTableCell',
	'{8C0B72C6-CFC6-4B2D-8A89-1DE890D9F65B}' : 'HoleTables',
	'{13A31354-BFF7-45CC-B749-2CE174780E77}' : 'HoleTable',
	'{A80294E5-6638-47F4-948A-A31A9F9CBC36}' : 'HoleTableColumns',
	'{A2E47B01-25D6-4047-BC17-FA7F71B18599}' : 'HoleTableColumn',
	'{73886374-D415-4797-8E3A-A2CA9115D924}' : 'HoleTableRows',
	'{E41AB38F-1708-4CAB-AA12-A29E5B3CE6FA}' : 'HoleTableRow',
	'{E232F1FF-D6C3-421F-B650-AFAC768279D5}' : 'HoleTableCell',
	'{CA779A92-76AD-4CD4-ACDB-7F06D73A089E}' : 'HoleTag',
	'{3A4B5B27-8B78-4584-83B5-6A088C6B87FF}' : 'DrawingNotes',
	'{33A71A9E-0E21-4B70-A688-604C897D3A5A}' : 'DrawingNote',
	'{395CFC80-16C4-4289-A9F3-06E09E329D95}' : 'GeneralNotes',
	'{5C204B1E-BE7E-489A-A842-7A800A7CE348}' : 'GeneralNote',
	'{4B5F98A9-D670-4DDF-A7CE-8AFCEE0990CA}' : 'UnitAttributes',
	'{08DCE0A8-28F0-4513-A655-010AD06BC874}' : 'LeaderNotes',
	'{04AAEAB9-6EAD-412C-B69A-D8EE4D924798}' : 'LeaderNote',
	'{E521F56F-13D5-4D80-95BA-10CB3B2F5918}' : 'ChamferNotes',
	'{C71B52F5-89E4-486C-B80E-8AC74650EB34}' : 'ChamferNote',
	'{206AFE1A-FAFA-4DAF-A569-1AF60672D63B}' : 'BendNotes',
	'{F5DA8C39-2BD7-4E77-BE94-81743E81ACC9}' : 'BendNote',
	'{46D8F255-F1A2-4C52-8D4B-29C02C8198FF}' : 'PunchNotes',
	'{D23F0671-F983-4D09-8E5A-2BAB64BFB549}' : 'PunchNote',
	'{DDB3F084-C3BC-4A46-8B6A-A169466514BF}' : 'HoleThreadNotes',
	'{C1516EB6-AEA2-412F-B1D0-9C609D152E21}' : 'HoleThreadNote',
	'{AEFA0FB8-139F-469C-8765-26AEA8C0A175}' : 'DimensionText',
	'{63E2B412-8EDA-496C-BAF6-A28928F74091}' : 'DrawingDimension',
	'{A907AEE3-A78F-11D5-8DF8-0010B541CAA8}' : 'DefaultBorder',
	'{A907AED9-A78F-11D5-8DF8-0010B541CAA8}' : 'SketchedSymbols',
	'{A907AED5-A78F-11D5-8DF8-0010B541CAA8}' : 'SketchedSymbol',
	'{A907AED3-A78F-11D5-8DF8-0010B541CAA8}' : 'SketchedSymbolDefinition',
	'{50DE4356-9814-490A-8932-18E72420930E}' : 'AutoCADBlocks',
	'{C7A9F576-7180-4DEE-BCC7-8E9DEABECEC4}' : 'AutoCADBlock',
	'{C7131135-82E7-45EA-BB86-15DA083F6A04}' : 'AutoCADBlockDefinition',
	'{682CEB3B-365E-4863-B103-BCC368FBA896}' : 'FeatureControlFrames',
	'{F3E768AB-B2BC-42B4-B95F-ED49BE550257}' : 'FeatureControlFrame',
	'{4A558EB0-274A-4EF6-90A0-222A720A778E}' : 'FeatureControlFrameRows',
	'{7CD6C780-663E-4187-8D35-D132C99F6918}' : 'FeatureControlFrameRow',
	'{F828B7C4-4B02-4B69-8D22-8BC7BA9D6243}' : 'SurfaceTextureSymbols',
	'{7FF4B4DA-DF87-4E58-8727-ADEBA3B6452B}' : 'SurfaceTextureSymbol',
	'{70E4E4A0-D090-41AF-8B0A-FFDB9F97B58B}' : 'SurfaceTextureSymbolDefinition',
	'{FD30DCC9-A6E8-44B1-85B0-D7D8AE1580E5}' : 'DrawingDimensions',
	'{A0F72CD2-B7A3-4EBA-9CDB-47F42BC74777}' : 'GeneralDimensions',
	'{EE21CD75-39FD-4683-BE24-BFBB9CA66EB4}' : 'GeneralDimension',
	'{294E366C-86B9-4CF7-9CF9-10D83787D2A6}' : 'GeneralDimensionsEnumerator',
	'{B0E8CB6F-9451-4AFC-B8D3-A157ACDCBB0F}' : 'LinearGeneralDimension',
	'{6FD094BA-90C4-4C9D-A3B9-DF3A398ECE26}' : 'BaselineDimensionSet',
	'{5BC0F92E-9C6A-4887-9B29-E1831F845DB2}' : 'ChainDimensionSet',
	'{5D81FF33-0E80-4FC7-A02B-D955952B2EC9}' : 'AngularGeneralDimension',
	'{8C1619BB-08F8-458D-B1B9-DEE4B63A3D07}' : 'RadiusGeneralDimension',
	'{98D51E77-8775-4472-8AB0-50BCA8F56023}' : 'DiameterGeneralDimension',
	'{EEB73D62-BB10-4FDA-84B2-B27521C833A1}' : 'OrdinateDimensions',
	'{3DA40E6A-7ED7-4B2C-A2E5-3FCE98B44077}' : 'OrdinateDimension',
	'{71BA345E-F3F9-49C9-917C-D7DFC284A07F}' : 'OrdinateDimensionSet',
	'{A3788117-9A81-4D70-A8C8-C3FF3895E3D2}' : 'OrdinateDimensionsEnumerator',
	'{F2930064-7C6A-4FF7-8B87-D98EAC520AA1}' : 'BaselineDimensionSets',
	'{ACC86380-BE3B-48F1-A3D0-91E6ED2E2A82}' : 'OrdinateDimensionSets',
	'{C9D63CDD-B82A-4CD9-82EB-CE937569197E}' : 'ChainDimensionSets',
	'{0945D4EC-0E81-4062-8AC1-E4DE4BB8CBF9}' : 'Centermarks',
	'{37697A9E-01B1-4581-B52D-B8758FBA364E}' : 'Centermark',
	'{3DC9DC2A-8A78-43BE-BDB5-E6F1162980BB}' : 'Centerlines',
	'{05EC93C4-CC47-450C-A826-FEC6692AD526}' : 'Centerline',
	'{206B59AF-22A6-11D4-B7A8-0060B0F159EF}' : 'Sheets',
	'{1DF75C0E-591B-45B3-8233-37924B5019DB}' : 'SheetFormat',
	'{892AF496-C31A-431A-9B15-39FA10940A86}' : 'AutoCADBlockDefinitionsEnumerator',
	'{A907AEBF-A78F-11D5-8DF8-0010B541CAA8}' : 'TextStyles',
	'{A907AEB1-A78F-11D5-8DF8-0010B541CAA8}' : 'BorderDefinitions',
	'{A907AEB5-A78F-11D5-8DF8-0010B541CAA8}' : 'TitleBlockDefinitions',
	'{A907AED1-A78F-11D5-8DF8-0010B541CAA8}' : 'SketchedSymbolDefinitions',
	'{A86A47DC-AAFE-4565-9E26-CBEEB2C1C8E5}' : 'SketchedSymbolDefinitionLibraries',
	'{A4AE6207-A45C-4454-9CF6-867D56403BD1}' : 'SketchedSymbolDefinitionLibrary',
	'{3E1A7894-35A3-41C3-9AF9-1E501AD1D747}' : 'LibraryFolders',
	'{90602DB0-0BE4-48E2-864E-D853D3542959}' : 'LibraryFolder',
	'{98E6F703-DF38-4C29-85A2-A8266869668E}' : 'LibrarySketchedSymbolDefinitions',
	'{3B1375EE-4B13-48AA-8A03-EDFDAEA85651}' : 'LibrarySketchedSymbolDefinition',
	'{E493FF48-3A9A-4A71-9C0D-27D79B3138C2}' : 'DrawingSettings',
	'{02BCE85C-478B-4A66-8668-6579602A0EB6}' : 'SketchSettings',
	'{27716230-E826-46E8-90FB-923D38D6F6F8}' : 'DrawingEventsObject',
	'{FA561B14-D9E1-4ABD-B6E6-CC8A6A88B268}' : 'DrawingEventsSink',
	'{C10BEC9D-DBA2-4035-9D15-11EA363B9A00}' : 'DrawingEvents',
	'{81710E0C-B8F1-4D04-BDDF-AC92C274CC81}' : 'DisabledCommandList',
	'{1ABBBF4A-8946-4A44-BFAE-F3200B41AA40}' : 'ControlDefinition',
	'{9C88D3A9-C3EB-11D3-B79E-0060B0F159EF}' : 'CommandManager',
	'{68D1E13F-F6A4-47FD-AAC0-5545A57B712B}' : 'InteractionEventsObject',
	'{F1C0EFF2-5035-4DDD-8086-060590676024}' : 'InteractionEventsSink',
	'{5C5381D9-CB23-4BD1-885F-744E8C90B9BB}' : 'InteractionEvents',
	'{21F3FEA8-2DF7-47B5-9C4C-33BB28E97D1C}' : 'SelectEventsObject',
	'{2E19A8EE-1E70-4AE4-8C1E-06DAE3BBABB2}' : 'SelectEventsSink',
	'{89444C1E-456C-4684-B029-3A5E3A89988C}' : 'SelectEvents',
	'{70B77812-4E3A-4499-8F8D-6AB6C6BDC5A5}' : 'MouseEventsObject',
	'{C18BB14E-4FEF-478B-BF34-4690DE9BFC6C}' : 'MouseEventsSink',
	'{26EC46CE-6FFC-4605-8BB0-5C6198790433}' : 'MouseEvents',
	'{6886F155-F98E-4287-BF33-F63CB776B6B2}' : 'PointInferenceEnumerator',
	'{6886F154-F98E-4287-BF33-F63CB776B6B2}' : 'PointInference',
	'{BD32F579-5C70-453E-BD6F-41D11EF640FD}' : 'KeyboardEventsObject',
	'{AB510BBF-B893-47F7-ACC6-8F22836C5D8C}' : 'KeyboardEventsSink',
	'{1D36C391-7C11-45B6-A818-687BA77FD2AC}' : 'KeyboardEvents',
	'{0466D05C-72BF-45E4-A1C6-3FA76AF8812C}' : 'TriadEventsObject',
	'{5401A856-D03A-4418-AAA2-F1B677FA410D}' : 'TriadEventsSink',
	'{68BC4B61-96FC-4D5D-B4B5-10AEAC7EC05A}' : 'TriadEvents',
	'{05E71BA9-6F04-4325-A3EA-1E2BEA94E4C2}' : 'ManipulatorEventsObject',
	'{4DF6BEBE-5642-49CC-B365-BCC424F9C2F6}' : 'ManipulatorEventsSink',
	'{45DAC6D1-55CB-4ECC-A295-CFA18A1463F3}' : 'ManipulatorEvents',
	'{691AF5CB-83DC-4AF2-B689-F70AFB0D5020}' : 'InteractionGraphics',
	'{6AAD65B4-5F61-42C1-830A-A45C60809D76}' : 'MeasureEventsObject',
	'{3C75ADFE-18C0-42BF-A83D-D0E539BD1F7D}' : 'MeasureEventsSink',
	'{6CFC2B95-2B15-486D-A100-0B83DA795626}' : 'MeasureEvents',
	'{DBC99CB5-8EB0-4D45-BAC7-DE9D532FDD04}' : 'MiniToolbarObject',
	'{B6B0211A-D77D-4D79-A529-7D8612C9A7A3}' : 'MiniToolbarSink',
	'{D5DA4F07-3728-4B95-9D14-5FF0ED96992E}' : 'MiniToolbar',
	'{79093216-BF48-46A2-9BFA-2D15CCB8BADD}' : 'MiniToolbarControls',
	'{F4D9FAC9-D5F7-4FB5-8324-16CA73F349FF}' : 'MiniToolbarControl',
	'{F6A7B996-5EB9-4DC4-99D9-3919C36FB802}' : 'MiniToolbarButtonObject',
	'{54D7BD09-6FA0-46F5-B427-F2432560A8C3}' : 'MiniToolbarButtonSink',
	'{06C9E562-0C16-4D86-8EB7-2513D279C81C}' : 'MiniToolbarButton',
	'{3D7599FE-1A8A-47D8-A353-5C48B819A55D}' : 'MiniToolbarCheckBoxObject',
	'{7DDF539F-7AFE-44BD-BAF9-BBAE51A93721}' : 'MiniToolbarCheckBoxSink',
	'{16ADC90A-A29D-40A9-93E4-4C858E8C7830}' : 'MiniToolbarCheckBox',
	'{7DF3C716-A1C7-4D3F-83C0-5D06A3D7F05C}' : 'MiniToolbarDropdownObject',
	'{8AAC5924-81F8-4760-9BA0-3BD408FA7BA5}' : 'MiniToolbarDropdownSink',
	'{F3393F71-A68F-442E-A03E-1B06B09D96A9}' : 'MiniToolbarDropdown',
	'{F22EBF2F-9F55-45FD-96DB-AABFBD40C177}' : 'MiniToolbarListItem',
	'{F7844415-30E0-4507-8BC0-F8AF990B3B38}' : 'MiniToolbarComboBoxObject',
	'{5A213EAD-8C62-4EE8-B99A-61A09F2F56E3}' : 'MiniToolbarComboBoxSink',
	'{834C1008-E416-4616-A66B-262175D8E852}' : 'MiniToolbarComboBox',
	'{4E97BC3C-1235-44DE-8B31-571FA40955B5}' : 'MiniToolbarValueEditorObject',
	'{334FE9E9-7C63-4924-8ADC-42DB57B7B688}' : 'MiniToolbarValueEditorSink',
	'{899DB1B0-F06A-4856-AADC-561B79C0E1A8}' : 'MiniToolbarValueEditor',
	'{6299A1B5-4F87-4209-B024-B002D3438E61}' : 'MiniToolbarSliderObject',
	'{2F9E3271-4E14-4B76-9581-602AED994066}' : 'MiniToolbarSliderSink',
	'{560ACA74-2C16-428E-9D63-08569BD33300}' : 'MiniToolbarSlider',
	'{AAC6E2B5-64B0-440C-A5A2-2AED0D4D7191}' : 'MiniToolbarTextEditorObject',
	'{32F5072E-8F1B-4889-898F-A512619D7D74}' : 'MiniToolbarTextEditorSink',
	'{E0813E5B-4E25-4192-B86B-0A284E558D5D}' : 'MiniToolbarTextEditor',
	'{7E765E87-446D-451C-9B54-F9714B157BE9}' : 'MiniToolbarTextBoxObject',
	'{C3DB869D-CA34-4269-BAEC-BB08F8FD7CB3}' : 'MiniToolbarTextBoxSink',
	'{A496E43B-EA92-4927-ACEA-465985F840A6}' : 'MiniToolbarTextBox',
	'{2772058F-17D8-4969-8D46-51860F09AC9B}' : 'UserInputEventsObject',
	'{711F30CD-A00B-4015-93A8-397EC8F5A284}' : 'UserInputEventsSink',
	'{9235396D-0350-11D3-B787-0060B0F159EF}' : 'UserInputEvents',
	'{EF0F253F-6AF9-40A8-BD13-B136E00B6588}' : 'CommandBar',
	'{67B1BC45-4518-4DB9-A5D3-C0364374BB80}' : 'CommandBarControls',
	'{4BF433DE-1B2F-4ADE-B71C-0C826CF2CC88}' : 'CommandBarControl',
	'{DBADC913-8652-4B4E-B13E-B356CC4E9BEE}' : 'ButtonDefinitionObject',
	'{9B5D2EC6-A4BD-4B3A-8A34-069EE52B009D}' : 'ButtonDefinitionSink',
	'{CD3A37C9-E647-41AA-B0D9-4EED2A875789}' : 'ButtonDefinition',
	'{4CF7D720-1E41-4049-8C1A-70C980D11667}' : 'ControlDefinitionEventsObject',
	'{AB5EF2D1-EAEB-4A4A-A86B-24BF0F2111BD}' : 'ControlDefinitionEventsSink',
	'{BEB3104E-2019-49E0-BC17-F5759998D9FE}' : 'ControlDefinitionEvents',
	'{5189E676-CC1A-4901-98E7-EC85130FDB63}' : 'ProgressiveToolTip',
	'{2F800161-0E4D-4953-A0B7-E55EE05E039B}' : 'MacroControlDefinition',
	'{91B9E6B9-B526-45A8-A7FD-0D2FFD1D6EF5}' : 'ComboBoxDefinitionObject',
	'{ACC63CB3-EBF2-48E3-A0F4-48E3FC13ECED}' : 'ComboBoxDefinitionSink',
	'{60F87ABB-0D3B-47D0-A6A9-E9AAC919EF31}' : 'ComboBoxDefinition',
	'{828DB6DB-AE56-4DB4-A765-216D9159A18C}' : 'RadialMarkingMenu',
	'{DE07F599-C9C0-4843-8EFE-D5083EBEFB1D}' : 'CommandControls',
	'{E0519C23-A426-4FA3-BB30-AC5FBEAD137E}' : 'CommandControl',
	'{AE2CB260-129A-494C-9F8C-AD8140271E8A}' : 'CommandCategories',
	'{6B821DA7-B56B-44FC-859F-4DABA658C6E2}' : 'CommandCategory',
	'{B9D982C4-3FFF-4796-AD6D-C6D1F16D7BA9}' : 'ControlDefinitions',
	'{FA403DAE-32E0-4C17-BB7C-CD3626A9BFA9}' : 'DragContext',
	'{2F5EC0C5-5335-4677-BB14-5621C1140D1B}' : 'EnvironmentManager',
	'{4E27C06E-4D6A-4E53-9F84-32A0643623CF}' : 'Environment',
	'{16EF0082-3213-4E37-AF75-5CB2BF738741}' : 'CommandBarList',
	'{C2FEB1BC-115B-443B-A18C-F88B2FCBB7BA}' : 'PanelBarObject',
	'{30A44C19-C3F4-483B-8835-A0A13B849AC0}' : 'PanelBarEventsSink',
	'{3283562C-885D-4693-9C77-4A60865FD185}' : 'PanelBar',
	'{3AB23287-16A5-4B3B-964B-00C27869CD23}' : 'Ribbon',
	'{3AF77BAF-EECD-4301-823D-9B604FE5C176}' : 'UserInterfaceManager',
	'{6364B6D5-2994-46A5-8F53-03F63958B056}' : 'CommandBars',
	'{A1C8AD17-F4C3-4424-982C-9D628A5A4ECA}' : 'EnvironmentList',
	'{D23D422B-C248-4EA4-98AF-9E6390C99964}' : 'Environments',
	'{4B01DD28-A1AF-4387-9F24-2B87442C1E94}' : 'UserInterfaceEventsObject',
	'{9BC9A7EC-A0AD-433B-BB3C-9AC30C9030E4}' : 'UserInterfaceEventsSink',
	'{4195A929-D003-467F-ADC6-11FB53A103EA}' : 'UserInterfaceEvents',
	'{4AA83B95-08F8-4415-9397-4BB5E8103290}' : 'Ribbons',
	'{B32BC09F-4DC6-4655-A457-8B7E8934CAAA}' : 'CommandControlsEnumerator',
	'{FE97EF73-E784-47FB-AA0B-D1891A8F1DF4}' : 'DockableWindows',
	'{3A32960B-A64E-4257-B24F-240C7E68C065}' : 'DockableWindow',
	'{32958A3F-CEA1-4390-946D-3D2F2E92675B}' : 'DockableWindowsEventsObject',
	'{863F993F-413C-4965-B391-CE4CF47616DB}' : 'DockableWindowsEventsSink',
	'{66D80FFD-2C33-4F55-8A78-EBF0A094CEEE}' : 'DockableWindowsEvents',
	'{1A88CE14-0590-4C13-B58A-C9B7FA1458C5}' : 'WebBrowserDockableWindow',
	'{176AA199-DDEA-4CA9-B7EC-0437918DF800}' : 'BalloonTips',
	'{BDAFC08A-5CAC-4E5A-B715-F2BCAFFD5282}' : 'BalloonTipObject',
	'{321398AC-E78C-43DF-B1A6-5BE90C133680}' : 'BalloonTipSink',
	'{1C7C9D34-E0E8-40D6-BA67-820B97B4C966}' : 'BalloonTip',
	'{1CE97D79-6535-4D0F-9A51-57734766BEDC}' : 'RibbonTabs',
	'{734FDACC-45FD-487A-AC60-02CE0522FF00}' : 'RibbonTab',
	'{7693ED6C-807E-443A-A3C0-A63010E5625A}' : 'RibbonPanels',
	'{916EFE1C-6493-4712-92D7-CD789914321A}' : 'RibbonPanel',
	'{228EA2B9-974A-48DF-8E17-7EAE50A79AFD}' : 'RadialMarkingMenus',
	'{32E4A31B-C5E8-11D2-B77F-0060B0F159EF}' : 'GenericObject',
	'{EF8803D3-9ADF-4B81-9097-6529ED782861}' : 'SheetSettings',
	'{6AC3D773-1202-450D-9CD2-3557B1395C64}' : 'SheetFormats',
	'{68517DF3-9E1D-44AA-B12D-08880086D61A}' : 'DrawingBOMs',
	'{FC290B65-544A-4F65-B812-092CB93AA421}' : 'AutoCADBlockDefinitions',
	'{528C9A32-4173-420A-AD05-B6FBF8382212}' : 'Parameters',
	'{652F6A52-8B8A-4CEF-B1DC-C78751914993}' : 'ModelParameters',
	'{916D7FDB-CFE6-4FB1-8921-694DC9CD2793}' : 'ModelParameter',
	'{12959B9F-4EF1-4834-83C1-7950F2321878}' : 'ReferenceParameter',
	'{8510D6EA-9A97-4CC9-A2A8-221FFC610AB4}' : 'UserParameter',
	'{1304BB1D-95AE-4738-80F8-CCCA1ABCFF6B}' : 'ReferenceParameters',
	'{2FF370FA-BB1C-4C92-BB10-06D94CC8F8F3}' : 'UserParameters',
	'{53D15C9C-4920-4B58-8804-8567A94D1643}' : 'ParameterTables',
	'{5250C13F-196F-442E-86E8-68C87B75CABE}' : 'ParameterTable',
	'{0E4C2356-1844-43F1-BAFA-45AA948EDAD8}' : 'TableParameters',
	'{B1F0562A-BC71-44E3-89B6-5583BB50CD09}' : 'TableParameter',
	'{ADE1D7A7-3CF2-49E7-8476-79677765D850}' : 'CustomParameterGroups',
	'{81342C4A-E898-4566-AA9B-735E88874E56}' : 'CustomParameterGroup',
	'{321D3FD9-A57F-4CDE-AD39-FD1EEE22543C}' : 'DerivedParameterTables',
	'{B9831DEF-A198-48C1-8023-F5F05E55B092}' : 'DerivedParameterTable',
	'{D4C98D93-FA6C-4602-8EB8-2709938BFE74}' : 'DerivedParameters',
	'{0BDE54D4-8527-46BE-B2DC-7E9A5AED8AB9}' : 'DerivedParameter',
	'{D4AAD36D-D0D1-4BFC-9C3A-C4718D3D9209}' : 'TextStylesEnumerator',
	'{062F6086-60DC-4550-93C5-A9B8CEA89ADB}' : 'ObjectDefaultsStylesEnumerator',
	'{1010554D-5E7D-4D43-A381-89B57B51A708}' : 'LayersEnumerator',
	'{3CF51EB9-B426-482F-98B0-8CE17BDCDEED}' : 'Styles',
	'{9BAC756F-6695-4C8B-A25C-16D29002F114}' : 'LeaderStylesEnumerator',
	'{7D85BA17-75C5-4EBE-AA18-F7E60AE25733}' : 'BalloonStylesEnumerator',
	'{852C83B9-26EC-4FDA-89D5-E031523AEE01}' : 'FeatureControlFrameStylesEnumerator',
	'{1DCB7001-C7CD-4637-AC67-296CEB47A86B}' : 'SurfaceTextureStylesEnumerator',
	'{1FA42157-89A8-4DA0-A943-888BF014E072}' : 'HoleTableStylesEnumerator',
	'{8E9F0865-0AE2-4AAC-8E67-0CED8434114C}' : 'CentermarkStylesEnumerator',
	'{F829B171-412E-4642-8034-AEC013FCFDC5}' : 'PartsListStylesEnumerator',
	'{50C3C4B3-5029-44E8-BF12-C1D09530CCF5}' : 'RevisionTableStylesEnumerator',
	'{E0B90B3E-0907-49B2-8E51-438C950F3A4B}' : 'TableStylesEnumerator',
	'{8006A076-ECC4-11D4-8DE9-0010B541CAA8}' : 'CollinearConstraint',
	'{8006A078-ECC4-11D4-8DE9-0010B541CAA8}' : 'ConcentricConstraint',
	'{8006A07E-ECC4-11D4-8DE9-0010B541CAA8}' : 'EqualLengthConstraint',
	'{8006A080-ECC4-11D4-8DE9-0010B541CAA8}' : 'EqualRadiusConstraint',
	'{8006A082-ECC4-11D4-8DE9-0010B541CAA8}' : 'GroundConstraint',
	'{8006A084-ECC4-11D4-8DE9-0010B541CAA8}' : 'HorizontalConstraint',
	'{8006A086-ECC4-11D4-8DE9-0010B541CAA8}' : 'HorizontalAlignConstraint',
	'{8006A088-ECC4-11D4-8DE9-0010B541CAA8}' : 'MidpointConstraint',
	'{8006A08A-ECC4-11D4-8DE9-0010B541CAA8}' : 'ParallelConstraint',
	'{8006A08C-ECC4-11D4-8DE9-0010B541CAA8}' : 'PerpendicularConstraint',
	'{8006A08E-ECC4-11D4-8DE9-0010B541CAA8}' : 'SymmetryConstraint',
	'{8006A090-ECC4-11D4-8DE9-0010B541CAA8}' : 'TangentSketchConstraint',
	'{8006A092-ECC4-11D4-8DE9-0010B541CAA8}' : 'VerticalConstraint',
	'{8006A094-ECC4-11D4-8DE9-0010B541CAA8}' : 'VerticalAlignConstraint',
	'{8FFF6DFE-F659-4C77-81E5-DD9B70A37D90}' : 'SmoothConstraint',
	'{E4C09561-E779-4A00-A835-E8D43E08A290}' : 'Sketch3D',
	'{FD1878BB-56AD-44CD-9186-11BC84E584A4}' : 'SketchEntity3D',
	'{85C83167-947D-46E2-A802-92D529B48E37}' : 'SketchConstraints3DEnumerator',
	'{6CBA9E79-C13B-46ED-BB14-6541A63B1A16}' : 'SketchEntities3DEnumerator',
	'{B1340A33-EB0D-4609-BA1E-B98A3D173794}' : 'Profiles3D',
	'{2A8678EA-A024-469A-80DC-D1EAD67847A3}' : 'Profile3D',
	'{D7347916-69D8-4972-AEBE-95BE5672BED2}' : 'ProfilePath3D',
	'{142C71BE-1254-4947-9192-382BCC511F46}' : 'ProfileEntity3D',
	'{2307500B-D075-4F5D-815D-7A1B8E90B20C}' : 'SketchPoint3D',
	'{4AF3870E-AB8B-4567-94B5-C1850D292111}' : 'SketchArcs3D',
	'{6129AB00-E4D1-45AD-B3AE-A873BDF452BF}' : 'SketchArc3D',
	'{87056D9A-B0B2-4BD0-A6EC-51E9D893A502}' : 'SketchLine3D',
	'{3A62D311-C21A-4DD3-83C0-A23507CA385E}' : 'SketchLines3D',
	'{3BCDEC54-2F73-4114-A7CB-ACF5E823B67D}' : 'SketchPoints3D',
	'{FA48B024-CC3B-458F-B0EB-6FE4CBEC35DD}' : 'SketchCircles3D',
	'{8D562D7A-4F0B-4EC8-8737-47DD28FB7323}' : 'SketchCircle3D',
	'{7A7BD889-E944-41FC-A34F-474465F0894E}' : 'SketchEllipses3D',
	'{8F014D19-4B2F-4DD1-9010-FE75815C297C}' : 'SketchEllipse3D',
	'{08C74C78-5F8D-40B3-9D57-4507D5CEA79C}' : 'SketchEllipticalArcs3D',
	'{C3CB1896-B26C-4862-8652-5208013D95A7}' : 'SketchEllipticalArc3D',
	'{611271CA-48EE-4EBF-9ACD-CCD081142400}' : 'SketchSplines3D',
	'{61FC7221-543B-4885-9546-B700267C98D1}' : 'SketchSpline3D',
	'{5DBD70FD-AB80-4074-B105-EB28F2CB397A}' : 'SketchSplineHandle3D',
	'{85A24FF2-F0E9-4BC4-9A69-34F8C683B41A}' : 'GeometricConstraints3D',
	'{0DE9D15F-7E51-4861-BD72-050A86BA17AD}' : 'GeometricConstraint3D',
	'{0456FF0D-196E-4C72-989D-D86E3DD32955}' : 'TangentConstraint3D',
	'{E8BE2118-716C-40FD-8BC0-2517B253E4F9}' : 'CollinearConstraint3D',
	'{38876920-588A-4F80-A4B1-1F2E3562FB19}' : 'GroundConstraint3D',
	'{73919DC1-220E-4EC9-B716-072D6046A3AD}' : 'ParallelConstraint3D',
	'{2035E584-09E7-4B18-9698-014DEF44B10E}' : 'PerpendicularConstraint3D',
	'{8E02BFEC-2C95-4685-83B8-E215F98BA844}' : 'CustomConstraint3D',
	'{281176E3-4EDC-4F4E-9804-6716B7B9059D}' : 'SmoothConstraint3D',
	'{843FEEB5-A0EF-4C5B-8939-4F9B574119D8}' : 'CoincidentConstraint3D',
	'{28DD48C9-8D70-11D4-8DDE-0010B541CAA8}' : 'WorkPoint',
	'{4FAB4F91-4998-4B1C-9717-8CDF1BD7377E}' : 'MidpointConstraint3D',
	'{8675C60E-CE43-4722-AB95-C41479862B66}' : 'ParallelToXAxisConstraint3D',
	'{76FE6138-9B22-40E6-AE41-98AE40609A45}' : 'ParallelToYAxisConstraint3D',
	'{50FB8693-BA00-47C5-BD0B-D03F1B545354}' : 'ParallelToZAxisConstraint3D',
	'{879211BF-E1DA-4EC6-BB14-35A030C132E7}' : 'ParallelToXYPlaneConstraint3D',
	'{35BB39D2-FBCF-4780-BC9C-6CF50B268EED}' : 'ParallelToYZPlaneConstraint3D',
	'{005E9B5E-B6E5-4670-97C6-0A6EA4B6CE2D}' : 'ParallelToXZPlaneConstraint3D',
	'{0C797F20-90F4-42F3-89B2-786880D1883A}' : 'EqualConstraint3D',
	'{93E69636-D11D-4044-BAC8-CD1DE3E6BC1E}' : 'OnFaceConstraint3D',
	'{80DBF4D7-FEC3-454C-BF1C-65BCDB27188C}' : 'SketchFixedSplines3D',
	'{7A5B2F53-5756-4261-B6F1-4B5C3CDE1226}' : 'SketchFixedSpline3D',
	'{B4F71C8B-BC8D-47F1-A327-9275F5FB443D}' : 'SilhouetteCurves',
	'{F9CB0F15-28B0-4D98-A658-F906D8B0D965}' : 'SilhouetteCurve',
	'{3C934EFD-E26A-4940-BA5A-66908C16AA92}' : 'DimensionConstraints3D',
	'{460D3833-0485-4B61-8A1A-C9E8008FAFCC}' : 'DimensionConstraint3D',
	'{1EA98FE3-C2EA-4025-8B42-7F91BD2E8DFC}' : 'TwoLineAngleDimConstraint3D',
	'{39930637-A840-4819-AB86-EFE9CCB21BD1}' : 'PointAndPlaneDistanceDimConstraint3D',
	'{C124F1E0-1B29-481D-A0CB-BA8A8AB69764}' : 'TwoPointDistanceDimConstraint3D',
	'{04A196FD-3FBB-43EF-9A79-2735B3B99214}' : 'LineLengthDimConstraint3D',
	'{90943B1A-D344-4227-8219-D1C6090697BB}' : 'RadiusDimConstraint3D',
	'{E045F7F0-7E93-4212-AA63-5F77EECB5625}' : 'SplineLengthDimConstraint3D',
	'{745A04C4-8445-412A-AFA7-33E778DA3059}' : 'SketchControlPointSplines3D',
	'{A4126F98-E952-4997-BD2D-209D4788F70F}' : 'SketchControlPointSpline3D',
	'{01BAC9F1-F900-4E57-9FDB-F12232AEC9D2}' : 'SketchEquationCurves3D',
	'{67863AC3-95B7-4386-8A51-449E44AC2FBC}' : 'SketchEquationCurve3D',
	'{9F672C49-E28B-4239-8F7B-BF3FA7FD5071}' : 'IntersectionCurves',
	'{25FF655F-9C78-4C55-9166-51E299DB6565}' : 'IntersectionCurve',
	'{A5620F8C-EEF1-4BD5-8C45-2C2327EFD42F}' : 'OnFaceCurves',
	'{173A0AA0-589E-4DC0-BDA9-8F5F10F8AF72}' : 'OnFaceCurve',
	'{B88938D1-2BE1-42D5-BD17-B4A7498C1B60}' : 'HelicalCurves',
	'{314DEB20-A0E9-4F72-8C44-D9B28D2CA3E7}' : 'HelicalCurve',
	'{C726DA3F-7695-4786-BB9E-EFF55388C855}' : 'HelicalCurveDefinition',
	'{111D8480-B19C-449F-84A8-3541A6B62253}' : 'HelicalCurveConstantShapeDefinition',
	'{597DC0FA-350A-418D-B183-450AB1FB041E}' : 'HelicalCurveVariableShapeDefinition',
	'{40AA25E1-641B-4765-9904-65F26FA457FF}' : 'HelicalCurveShapeDefinitionRows',
	'{2E61B5D9-3348-452C-8444-593CFD702693}' : 'HelicalCurveShapeDefinitionRow',
	'{221D9E13-D105-485A-B538-1E3FB7250A71}' : 'StyleEventsObject',
	'{A52071CF-BF9F-45BA-A7D5-E5AAA2682B4D}' : 'StyleEventsSink',
	'{4732A4F0-D435-4F10-8548-4DBE68276D58}' : 'StyleEvents',
	'{FB4D47B9-777E-49C5-99CB-9CE5C345D66E}' : 'RepresentationEventsObject',
	'{AFD8E323-2B44-4657-89F2-4C50233D287A}' : 'RepresentationEventsSink',
	'{955CB4BF-782F-4A58-8538-4E1028EA5D20}' : 'RepresentationEvents',
	'{29F0D465-C114-11D2-B77F-0060B0F159EF}' : 'AssemblyDocument',
	'{81F414A9-1062-46BB-A5EE-26575E90DCF0}' : 'ModelingSettings',
	'{42E1EF4D-7D8F-49EA-95A4-B4661D4983AA}' : 'UserCoordinateSystemSettings',
	'{C45BCCBE-2E53-4C8F-B76A-E6B7815E87E4}' : 'Materials',
	'{57CFD4EC-1776-48D3-B5C4-7B6E015D0541}' : 'Material',
	'{9DACF05E-4734-4D7E-986A-EE320F8A85C7}' : 'LightingStyle',
	'{9F512CF6-D755-4539-A0A5-E346F4B89AE1}' : 'Lights',
	'{755B3C6B-3A92-4702-96AC-686382A91278}' : 'Light',
	'{A5B827BD-83C7-4CCA-8DCA-06CD10C2237E}' : 'LightingStyles',
	'{1B73EA84-1B63-4F24-B295-B50EA9215C26}' : 'ObjectVisibility',
	'{575F2831-2B6A-11D4-B7A8-0060B0F159EF}' : 'AssemblyComponentDefinitions',
	'{F2780C41-65D5-43E1-A259-E05D08ED1659}' : 'DisplaySettings',
	'{A12C6DFA-6381-41A2-9037-13AFE5B1EFBD}' : 'GroundPlaneSettings',
	'{7289A75E-C37E-468C-904F-B2BADC61F272}' : 'Assets',
	'{BED3CF92-D335-4DC0-BA98-76F2E8A6A963}' : 'OGSSceneNode',
	'{1915251D-AC20-4EFC-A0EE-43FBEF266925}' : 'OGSRenderItemsEnumerator',
	'{429D036C-4F9D-4F72-9F77-AB5789FCC6E9}' : 'OGSRenderItem',
	'{E8DC5B4C-F562-4911-AFBC-41961F55C140}' : 'OGSSceneNodesEnumerator',
	'{4E1C27BA-D992-411F-9DE2-BD630285E4B3}' : 'DesignViewRepresentation',
	'{B25D15A6-B823-42FF-9ABB-781A3043ECB0}' : 'RepresentationsManager',
	'{1154D44F-DED2-4457-B862-8631D4D69FC6}' : 'PositionalRepresentations',
	'{DD22F707-6FC9-481B-A3FD-44FDA2D695A2}' : 'PositionalRepresentation',
	'{AA044AA2-D685-11D3-B7A0-0060B0F159EF}' : 'AssemblyConstraint',
	'{6D634B29-2066-44CA-AA97-D87A2C95A172}' : 'iMateResult',
	'{56C3574C-13A4-46AB-B981-4B45784B2156}' : 'AssemblyConstraintsEnumerator',
	'{359AC6D9-E239-4825-BA81-DD8E433FBD1E}' : 'iMateResultsEnumerator',
	'{928894AE-2111-43EB-B77C-4E1A7388CD75}' : 'iMateDefinition',
	'{EB7E9B67-F77A-4ACE-A3CB-1D5C93F7EE9D}' : 'LayoutConstraint',
	'{AC581AF3-E3C8-4011-9140-3B64D555FA05}' : 'FlushConstraint',
	'{9048CE40-F6A5-422D-A816-CBE5E03B28D6}' : 'AngleConstraint',
	'{929723D9-517D-4405-A5B5-263E3B02C6C4}' : 'CustomConstraint',
	'{0AEBFB16-385B-4663-B17C-D07F576F2C70}' : 'InsertConstraint',
	'{CEFDC141-B989-4BF3-BDD7-8308D8089FFE}' : 'MateConstraint',
	'{F8F30CD3-A44B-4C8A-B9D2-287361B0BD26}' : 'RotateRotateConstraint',
	'{31737D0F-56F3-40B8-8649-C8A5AB945D80}' : 'RotateTranslateConstraint',
	'{0A73D068-AC6B-4B51-8B6D-913B90A77741}' : 'TangentConstraint',
	'{3CBE8AAD-3D92-11D5-8DEE-0010B541CAA8}' : 'TransitionalConstraint',
	'{C3F06C8B-B0EA-4EC3-9922-1657009774D3}' : 'DriveConstraintSettingsObject',
	'{ED68898D-4062-47D4-AC28-9B8A1F38CE90}' : 'DriveConstraintSettingsSink',
	'{88B090C2-BD7E-47CC-89D3-AA683A3E0297}' : 'DriveConstraintSettings',
	'{F8FEB6D6-1D1A-4472-9429-1FF06A76DB9E}' : 'DriveSettingsObject',
	'{0F13E8B9-A4C2-4477-93CA-FC2CD0D2C1B1}' : 'DriveSettingsSink',
	'{F93BBC7A-1A75-47D8-9E93-FD1B188AB4DB}' : 'DriveSettings',
	'{BA9EC28C-765B-4481-8A8C-20489290B35E}' : 'AssemblySymmetryConstraint',
	'{8112A2AA-0017-4029-81A5-9C18F5E37E92}' : 'ConstraintLimits',
	'{A8E2C150-78E9-4E97-A4A0-BF43936B2A45}' : 'RectangularOccurrencePattern',
	'{CDF65ADD-9C11-4AB9-8F2E-AB6F83FED7C2}' : 'OccurrencePatternElements',
	'{09A5CE88-D529-499E-82EF-246D8DC4F5B3}' : 'OccurrencePattern',
	'{6ABB8219-4962-11D5-8DEE-0010B541CAA8}' : 'OccurrencePatternElement',
	'{6F9AAB22-31DC-4F5A-98ED-8A8693D5BD1C}' : 'CircularOccurrencePattern',
	'{B7B652AD-7411-429D-92AC-663F9183F7F6}' : 'LevelOfDetailRepresentations',
	'{F24F9821-0EE5-4157-A555-45B97DE14D6D}' : 'LevelOfDetailRepresentation',
	'{C6A2B48C-DBBC-4BA9-A98B-6EB63FB78AE4}' : 'DesignViewRepresentations',
	'{5F08DCB5-FE15-4511-9A2E-A3FB10968F2A}' : 'AssemblyEventsObject',
	'{BABF5BBF-9878-11D4-8DE2-0010B541CAA8}' : 'AssemblyEventsSink',
	'{BABF5BC3-9878-11D4-8DE2-0010B541CAA8}' : 'AssemblyEvents',
	'{92E914D0-9FEA-11D6-8E0B-0010B541CAA8}' : '_AssemblySolver',
	'{92E91440-9FEA-11D6-8E0B-0010B541CAA8}' : '_AssemblySolverNodeObject',
	'{92E914A0-9FEA-11D6-8E0B-0010B541CAA8}' : '_AssemblySolverNodeSink',
	'{92E91460-9FEA-11D6-8E0B-0010B541CAA8}' : '_AssemblySolverNode',
	'{560F650A-7084-466C-8308-F14F854D677F}' : 'PublicationEventsObject',
	'{B1DC30D1-7C5F-41F2-A1D9-5D7D4C76C9CA}' : 'PublicationEventsSink',
	'{F3041103-5E4E-4045-806D-24A901AAD449}' : 'PublicationEvents',
	'{29F0D46C-C114-11D2-B77F-0060B0F159EF}' : 'PresentationDocument',
	'{941D7D22-4C65-4E96-B446-086CD1B94572}' : 'PresentationExplodedViews',
	'{1F917159-C90E-4746-A4E3-E543894ADFD3}' : 'PresentationExplodedView',
	'{F30319D0-9C9E-40BC-96AC-62D2E9302E5B}' : 'TrailsEnumerator',
	'{0AD2B1BB-3410-4A43-9926-C3849F69FD2F}' : 'Trail',
	'{8D039683-92D8-4F9E-995C-1FDF01AA16D0}' : 'TrailSegment',
	'{32705861-0597-4BAA-A445-5846AF71C3B7}' : 'PresentationTasks',
	'{AED640A3-73BD-4F63-B15D-FD6D71529BAB}' : 'PresentationTask',
	'{67C4F7E6-7B96-4837-8DD1-B4A6A78FF810}' : 'PresentationSequences',
	'{51CBB633-D1B6-4575-A028-085C4A270C27}' : 'PresentationSequence',
	'{0C8FA54F-425F-4F29-8DD8-4EA0D1CBF23E}' : 'PublicationComponentsEnumerator',
	'{D7EF5F2C-9214-426A-BC93-3DCE96FC6573}' : 'PublicationComponent',
	'{B70FB526-7ED8-4345-B5BE-B7DFB062394C}' : 'Publication',
	'{9FC0A05F-E541-4E76-ADD5-AD36E875A620}' : 'PublicationComponents',
	'{539C3AFE-A915-4086-B2B6-1133E4DC4E51}' : 'Storyboard',
	'{31B59E93-AB77-4236-9F8B-781B150CD754}' : 'PublicationTweaks',
	'{87A90F35-C48D-4BBB-A865-5EBBC267CBC3}' : 'PublicationTweak',
	'{0AA9C1C0-0182-4E85-9A61-B5410F35EA4C}' : 'PublicationTweakDefinition',
	'{91CF45CD-E5CD-47DF-B7AA-ECCA91DC4FA0}' : 'PublicationTrailSegmentsEnumerator',
	'{98BDC540-5F67-4A23-87E8-EC2072999157}' : 'PublicationTrailSegment',
	'{0D1F1D70-2997-462D-90A0-61C5D5E97C85}' : 'PublicationTrail',
	'{86128260-22B9-4841-92C2-977F78B39A96}' : 'PublicationTrailSegments',
	'{A13F8CA8-B7C1-4459-9E89-E5D890336737}' : 'PublicationTweakPath',
	'{7EDBE5DA-6A04-4AF6-B891-6A6139147197}' : 'PublicationTweakPaths',
	'{8EB31EAC-43A6-429E-A06C-7CDC128B4996}' : 'PublicationTrails',
	'{3DD94016-2767-47B0-A331-117EA621C088}' : 'Storyboards',
	'{66C9BA8B-1A75-4A21-BF84-EA4D26E89010}' : 'PublicationMarkedViews',
	'{35D84E9C-ABB8-49CE-831D-62BBC8B0594A}' : 'PublicationMarkedView',
	'{4762B21E-A04D-4479-BCF3-1B105A126455}' : 'PublicationBodiesEnumerator',
	'{54167F8A-A119-41FD-8B5C-895257D45E2C}' : 'PublicationBody',
	'{A8EAF4E3-FD98-4E26-9B99-D7B9D97961FD}' : 'PublicationEdgesEnumerator',
	'{A093F915-6F3B-41C5-A3A6-7943A498DF78}' : 'PublicationEdge',
	'{0EF5B3D1-E19B-423A-BFD8-102D7C0F4A0C}' : 'PublicationFacesEnumerator',
	'{87C8148C-FB68-4E5C-B79A-7648BAC75886}' : 'PublicationFace',
	'{41BECC60-689A-455E-8637-991E384C1C96}' : 'PublicationFaceShell',
	'{D88680AD-1C6E-4C6B-B946-CB1FC8849DDF}' : 'PublicationVerticesEnumerator',
	'{F9F9CB96-EF02-45D5-A8D1-62EDFE3C9F99}' : 'PublicationVertex',
	'{7DB211BE-6367-4245-97F2-4B30F4A79E13}' : 'PublicationFaceShellsEnumerator',
	'{D6DB0745-4B18-4A22-8F03-DD12B0D444E0}' : 'MeshFeatureSets',
	'{8728FC5B-20DF-43CC-A845-F2BFA49163A1}' : 'MeshFeatureSet',
	'{D2EB4CB2-4FC9-4E83-A9BE-71D86E1D5752}' : 'MeshFeature',
	'{5F093D38-605F-42A2-B2D3-38E4A16353F1}' : 'MeshFeatureEntitiesEnumerator',
	'{0466F7FE-1603-4F35-882C-B0B27E17E976}' : 'MeshFeatureEntity',
	'{EB674FEC-0328-44DB-A763-E58F97EDD8DC}' : 'PresentationTweaks',
	'{354F622F-BDFB-4010-A276-46F0EA99AD16}' : 'PresentationTweak',
	'{9F579B5F-27B6-4F2A-A08B-40231EB645D3}' : 'TrailSegmentsEnumerator',
	'{965DB171-5349-455E-8C19-3789DD189792}' : 'Publications',
	'{EF6287D1-E4BF-4978-A5AF-CBCA47EB56E6}' : 'PresentationEventsObject',
	'{4C1CBCCC-487C-48ED-9AB6-7411B020A58E}' : 'PresentationEventsSink',
	'{85F26D84-30C8-44EB-9E34-A74CF096FE36}' : 'PresentationEvents',
	'{B59644DA-CE64-4FAF-BAC6-A064AD00AE41}' : 'PresentationScenes',
	'{C9C41EF2-150B-4B55-8949-0A860D91245C}' : 'PresentationScene',
	'{3851834F-2FC9-4D4A-8739-0C2DB105C795}' : 'PresentationSnapshotView',
	'{B2EFCD07-8F2C-47FB-93D1-22645ECD280C}' : 'PresentationTrails',
	'{C56AC462-1A94-41D4-90C6-AD796A778986}' : 'PresentationTrail',
	'{431E59F3-872A-4293-891B-9B637BB454A0}' : 'PresentationComponent',
	'{00BC5CE8-F355-421B-82AD-B6DFA428156B}' : 'PresentationMeshFeatureSetsEnumerator',
	'{121AEDEB-A983-4AA9-9F88-81DEC638DCFB}' : 'PresentationMeshFeatureSet',
	'{29302798-B225-447C-B37B-300DC28B888C}' : 'PresentationMeshFeature',
	'{AC89451E-1B5B-4E2F-9E94-0050F94041A4}' : 'PresentationMeshFeatureEntitiesEnumerator',
	'{B7635E1F-FF33-424A-B121-4CAC9EBDA9E2}' : 'PresentationMeshFeatureEntity',
	'{6F61D701-A0B1-4E74-97A5-9B3F7ABA36BC}' : 'PresentationBodiesEnumerator',
	'{297560D3-0E33-4208-B903-96C1C5FE181E}' : 'PresentationBody',
	'{C1C31BE3-445F-403A-927B-54840EA62012}' : 'PresentationEdgesEnumerator',
	'{59EE8744-CA2F-4E38-B19A-D99EAACE0219}' : 'PresentationEdge',
	'{05C7DEC5-9B50-4AA8-9263-7A8AA35F1834}' : 'PresentationFacesEnumerator',
	'{BF527E81-1757-417B-BAA1-F50ED7F40A8F}' : 'PresentationFace',
	'{6A2E6CA4-4138-4FD7-9843-7EBCEC07126D}' : 'PresentationVerticesEnumerator',
	'{DBC6E00A-9233-4A04-BA1E-EFD6C476F9FB}' : 'PresentationVertex',
	'{1AD88D7E-9F07-4657-9410-9AF1E0A734F6}' : 'PresentationComponentsEnumerator',
	'{88666A4B-DC8F-48A2-8748-CB345ABC0B0D}' : 'PresentationTrailSegments',
	'{B35A4214-030A-44C2-8618-E94A05543B23}' : 'PresentationTrailSegment',
	'{12162DC0-9513-405B-8882-8CEDE4CC78C2}' : 'PresentationSnapshotViews',
	'{3D67DF18-9BC6-4470-A9E3-C820CB4E821C}' : 'FileAccessEventsObject',
	'{E51041E7-5DB6-4951-9F76-3ACA9B2E2A66}' : 'FileAccessEventsSink',
	'{32E4A319-C5E8-11D2-B77F-0060B0F159EF}' : 'FileAccessEvents',
	'{9235396B-0350-11D3-B787-0060B0F159EF}' : 'ObjectsEnumeratorByVariant',
	'{A0481EEA-2031-11D3-B78D-0060B0F159EF}' : 'ApplicationAddIns',
	'{A0481EEB-2031-11D3-B78D-0060B0F159EF}' : 'ApplicationAddIn',
	'{0BF73FD9-1253-11D3-B789-0060B0F159EF}' : 'FileLocations',
	'{AE277672-2FDC-11D3-B78F-0060B0F159EF}' : 'TransactionManager',
	'{AE277673-2FDC-11D3-B78F-0060B0F159EF}' : 'TransactionsEnumerator',
	'{AE277674-2FDC-11D3-B78F-0060B0F159EF}' : 'Transaction',
	'{68E4EA6F-3BEA-4F89-9335-F46CDF1AB005}' : 'CheckPointsEnumerator',
	'{B0955199-1373-4868-9B86-4ABB2DC2A684}' : 'CheckPoint',
	'{ABD216FA-7559-4883-93D7-C0A9ECFF19C4}' : 'TransactionEventsObject',
	'{BA8CE4E1-3FC3-414C-A73A-26BDB38ECE70}' : 'TransactionEventsSink',
	'{AE277675-2FDC-11D3-B78F-0060B0F159EF}' : 'TransactionEvents',
	'{D70C53E3-58A6-48CA-95D2-AF6F4AAD04EA}' : 'ChangeManager',
	'{9ACB775D-8E1E-4A38-9121-7E1467526860}' : 'ChangeDefinitions',
	'{4F8D5D47-63F7-4690-A06D-54D7311A2566}' : 'ChangeDefinitionObject',
	'{48DDBD08-5630-4D9A-A71F-8F623A3ABB47}' : 'ChangeDefinitionSink',
	'{A031AE7E-B6DF-49AB-820F-51FF71C1364A}' : 'ChangeDefinition',
	'{62246192-FF8D-4715-997D-09E760061B5C}' : 'ChangeProcessorObject',
	'{5BAB1E1A-F66B-4021-A008-A16E939CA863}' : 'ChangeProcessorSink',
	'{F575FA3E-1825-4671-A825-FD1F09E1EC96}' : 'ChangeProcessor',
	'{97ECB3AE-6C6E-4D8A-A91E-564314494EB8}' : 'TransientGeometry',
	'{CB69F179-558E-11D3-B793-0060B0F159EF}' : 'Line2d',
	'{5DF860A2-6B16-11D3-B794-0060B0F159EF}' : 'Cylinder',
	'{FA34A401-F063-11D3-B7A2-0060B0F159EF}' : 'EllipticalCylinder',
	'{5DF860A3-6B16-11D3-B794-0060B0F159EF}' : 'Cone',
	'{FA34A402-F063-11D3-B7A2-0060B0F159EF}' : 'EllipticalCone',
	'{5DF860A5-6B16-11D3-B794-0060B0F159EF}' : 'Sphere',
	'{5DF860A4-6B16-11D3-B794-0060B0F159EF}' : 'Torus',
	'{5DF860A6-6B16-11D3-B794-0060B0F159EF}' : 'BSplineSurface',
	'{E3B2EB5A-FE46-4DA6-8DDD-6135E2120CB2}' : 'BSplineCurve2dDefinition',
	'{30630D32-6807-4D69-8E77-224FD90A21BF}' : 'BSplineCurveDefinition',
	'{C9EBE756-798A-4E78-8CC4-DA91D7737321}' : 'Polyline3d',
	'{2A1047EF-0B48-413B-92FD-6CA45A488DA6}' : 'Polyline2d',
	'{556DCFA3-BD63-4B13-9C12-D99113AEAEFB}' : 'OrientedBox',
	'{6BA435D7-BBD6-11D4-8DE6-0010B541CAA8}' : 'TransientObjects',
	'{6BA435D9-BBD6-11D4-8DE6-0010B541CAA8}' : 'TranslationContext',
	'{6BA435DB-BBD6-11D4-8DE6-0010B541CAA8}' : 'DataMedium',
	'{FD9487E1-57A9-419B-A365-14323D1B1CD9}' : 'ObjectCollectionByVariant',
	'{BEE271DA-318F-471D-AF24-296B6F59B392}' : 'FileMetadata',
	'{EEB0116A-7B74-4A9C-B2FF-96BC31812249}' : 'InventorVBAProjects',
	'{B00506C6-BEB7-47F6-8B1B-A5CB5DCD09B3}' : 'FileManager',
	'{C029F46A-865A-4466-BE55-DF72750C8865}' : 'FileManagerEventsObject',
	'{CA8E18AF-5EA2-4A45-BA43-FF3914C5C200}' : 'FileManagerEventsSink',
	'{A44AF926-6383-42F0-8B2D-253F82F95ABE}' : 'FileManagerEvents',
	'{C6345819-0FAA-45A0-BF96-3C946F130076}' : 'AssemblyOptions',
	'{DBB345F5-06CB-4B20-96B8-C47EF589ECBE}' : 'GeneralOptions',
	'{5A0B6FAA-1405-4AB1-AFE9-786462FADF33}' : 'ThreadTableQuery',
	'{1470BE5E-D0B2-4177-A484-3528D6B0FC37}' : 'ThreadInfo',
	'{C032137F-6434-40C1-8DEC-763A191D1EE0}' : 'GripSnapOptions',
	'{2389822D-0890-4A2F-8CE3-B5F65E162E96}' : 'SpellCheckOptions',
	'{88032CAE-3F85-4B0E-A4C0-9F76F490DDDC}' : 'CustomDictionary',
	'{D80190AB-F025-4F75-9363-D3522E429A56}' : 'CustomDictionaries',
	'{8B657FE9-BF0A-4AED-B1FB-166229D406B3}' : 'SketchOptions',
	'{F440685C-03F8-49FF-8B68-79E575AF5A5E}' : 'HeadsUpDisplayOptions',
	'{541E7231-CD23-4986-B26D-4C2B4F1E2DBE}' : 'SketchConstraintSettings',
	'{986FCF92-8A47-4DEC-9007-DD852292DE71}' : 'PartOptions',
	'{D39AB98F-45E0-4CAE-A0F2-4490804F2AD3}' : 'Sketch3DOptions',
	'{221277C1-7963-4539-B2E5-E7E16D3C75AA}' : 'DrawingOptions',
	'{A6EC8B79-931A-409E-90CE-3EE28CB9F9F4}' : 'SaveOptions',
	'{EB213A42-0727-48F0-9BCF-C55F6CB4CD78}' : 'FileOptions',
	'{F7EDD327-75BC-4976-A0AE-7696B54D461D}' : 'FileOpenOptions',
	'{9A19AF07-A6BF-43AA-ABF3-870CA1CF329F}' : 'HardwareOptions',
	'{8AC1686D-0646-41D5-A28F-05353181AEBA}' : 'ContentCenter',
	'{2BF92C40-9E07-4F12-B6A3-C5DAA12D3A61}' : 'ContentQueryObject',
	'{6F10D9EC-E95C-489C-A398-5B530FD1D820}' : 'ContentQuerySink',
	'{FD30BB1E-44E3-4AB5-9035-9715ABEB9649}' : 'ContentQuery',
	'{2B4C4468-F71B-44EE-BAC6-C68CD4F8DDA1}' : 'CategoryManager',
	'{BFB40FAA-DEC6-4C84-BBA2-8FD424F3C564}' : 'FamilyManager',
	'{2B24FE45-C9E2-4590-BA7E-F7DB0E5A683F}' : 'MemberManager',
	'{FC6C5BEB-A2CE-4249-8C31-6B0E1E8030A9}' : 'QueryManager',
	'{C3E0CCFC-A6F5-4C54-83E4-3A2CBF11D5D7}' : 'LibraryManager',
	'{069D986F-6DED-4D48-900F-B53674E46499}' : 'ContentCenterEventsObject',
	'{6C6BEFAC-FECC-47A9-8A4C-68210FE441C3}' : 'ContentCenterEventsSink',
	'{D8AF1BF3-67C1-4EB2-8DA0-6E7625B5291E}' : 'ContentCenterEvents',
	'{52223C79-EAAC-45CB-B000-35DBB1494A3D}' : 'ContentCenterDialog',
	'{F55C4A2E-FEBB-4EEA-872D-C54B481B0948}' : 'ContentCenterDialogEventsObject',
	'{26F03E86-7DA4-4789-AACC-DE231C4C35E5}' : 'ContentCenterDialogEventsSink',
	'{87359527-E87E-456C-BDD3-F82FACBABAD2}' : 'ContentCenterDialogEvents',
	'{3DD6B742-71A1-438D-BB71-5CACFA2AACBE}' : 'ContentTreeViewNode',
	'{2CB6EA8B-44E3-4C93-BB2A-531D62EBD934}' : 'ContentTreeViewNodesEnumerator',
	'{239A8027-E757-4A2E-B8DC-9203A644401F}' : 'ContentFamiliesEnumerator',
	'{30E22548-6DE0-43B7-A8EE-E379A9C86F7D}' : 'ContentFamily',
	'{E06998C3-E510-47D3-BE8D-2CD348F24456}' : 'ContentTableColumns',
	'{20C36669-DC84-413C-84A7-4D0983BAD319}' : 'ContentTableColumn',
	'{F8CA1F67-2904-4C91-88F3-F79683227118}' : 'ExpressionLimits',
	'{8BEE2F07-0ACD-4A3C-A5BC-E064C8C0DBA8}' : 'ContentTableRows',
	'{1C310044-05CF-4B79-9829-FE41BD1EB1A6}' : 'ContentTableRow',
	'{2F27448C-CB52-4D34-87AE-6D75E01F5623}' : 'ContentTableCell',
	'{2B03891E-1B59-4576-8160-C61EA6E6D0DC}' : 'iFeatureOptions',
	'{CEF827E8-5A0A-452D-83BB-1A88815C1601}' : 'NotebookOptions',
	'{48694BB1-0E75-4A39-94E0-C7C133C23305}' : 'DisplayOptions',
	'{DA7E3A1C-5473-4CC3-8E19-25F8DE00C0A6}' : 'ShadedDisplayOptions',
	'{75091477-A808-4B93-AF11-14C0CD466611}' : 'WireframeDisplayOptions',
	'{78B3596A-176A-43F5-A65C-4BDFFC042236}' : 'MeasureTools',
	'{0420658E-CCD1-4100-BFA1-AD78AA655551}' : 'LanguageTools',
	'{2BFE4397-C369-4CEF-90C9-D5C8AE90BC9F}' : 'TransientBRep',
	'{4D662CE2-D29B-42E0-BA74-715C311E5630}' : 'SurfaceBodyDefinition',
	'{7F842490-A580-4A3A-AF94-DF8E5D292A42}' : 'EdgeDefinitions',
	'{F8B3014D-CA2D-40F4-B2A3-FA00E23105A1}' : 'EdgeDefinition',
	'{F3ACEE71-EC98-43F5-AC33-D0BDE47609EE}' : 'FaceDefinition',
	'{9A9B007B-18C5-4C27-BBA5-1D8F7E9B9A30}' : 'EdgeLoopDefinitions',
	'{F1779764-61F6-4C25-8B5D-6A6F41B57709}' : 'EdgeLoopDefinition',
	'{ECEA0373-8BE9-4970-A696-C967A9718017}' : 'EdgeUseDefinitions',
	'{6307798C-50E3-4E9E-B502-038DA82B7C74}' : 'EdgeUseDefinition',
	'{40E01FF0-E437-4C55-83A4-8E3FA8B19225}' : 'VertexDefinition',
	'{41473886-B1F1-4E65-9BEB-36F729B6A9F1}' : 'LumpDefinitions',
	'{27AAE3A7-29EC-4C49-9845-97318E4C6905}' : 'LumpDefinition',
	'{1B28061F-6494-47D6-B8A4-3F6EF0DF0642}' : 'FaceShellDefinitions',
	'{BB41DDFD-351A-4AC7-9294-0FF1D2710C07}' : 'FaceShellDefinition',
	'{34EE0736-EB0C-47F4-A4DA-D28AE8D91BFF}' : 'FaceDefinitions',
	'{29440031-7A2B-4713-907C-DCCE79375669}' : 'WireDefinitions',
	'{9F5047CD-939F-4F15-930C-5C77CEB50BAA}' : 'WireDefinition',
	'{4B427038-81A6-4E75-A633-CF7CCBDD8160}' : 'WireEdgeDefinitions',
	'{D29F9AF1-3383-40AC-94BA-69057A213AAD}' : 'WireEdgeDefinition',
	'{F5BB5A51-A89B-425E-A747-23CD25D3C186}' : 'VertexDefinitions',
	'{DB93184E-4A45-4C38-96B4-42051502413D}' : 'ApplicationUtilities',
	'{E8D1DB25-5BBF-4635-B2A9-2ECC3A150373}' : 'MoldDefinition',
	'{CB5F8603-7F21-4B44-A5C1-CD471AB5EA08}' : 'MoldSplitResult',
	'{6D78B55D-0148-442F-9EF5-E00611FCD8FF}' : 'RunoffSurfaceDefinition',
	'{7B550B22-4519-43D2-9A9E-5EC0D9FFCCD6}' : 'ErrorManager',
	'{C7CECA91-B8BD-4C0E-A998-FBFD9BE85416}' : 'MessageSection',
	'{650A171B-40E1-4C3B-B55E-DFB3D31C2CB8}' : 'ContentCenterOptions',
	'{D93EE206-0CA6-401E-B74E-0D9E4F924751}' : 'StylesManager',
	'{DDD3ADB9-30D8-4E01-8E88-42ABF8645AD4}' : 'MaterialsEnumerator',
	'{F6F33557-6984-11D5-8DF3-0010B541CAA8}' : 'DebugInstrumentationObject',
	'{F6F3355B-6984-11D5-8DF3-0010B541CAA8}' : 'DebugInstrumentationSink',
	'{F6F33559-6984-11D5-8DF3-0010B541CAA8}' : 'DebugInstrumentation',
	'{DDC2F383-3824-49E3-837C-7387D4775893}' : '_AppPerformanceMonitor',
	'{369933DF-0F63-46AA-919B-17C91F385C9E}' : 'TestManager',
	'{A4555442-8328-402E-BBF5-EDC7D808E522}' : 'TestCases',
	'{3588F0A6-950E-402A-BFB1-C0ECB1B2EE44}' : 'TestCase',
	'{52D6C08A-B387-4F4C-A2E3-4F3CFFF276CE}' : 'TestProgram',
	'{2190DB7B-9EAB-45D5-B9E0-B7FE50E1F50B}' : 'TestInputOutput',
	'{D88ABC2A-BA2E-4E03-AABE-E052F004A177}' : 'TestResult',
	'{8378680D-EA06-405D-986A-8406E0E874B0}' : 'TestResults',
	'{ED859179-A285-41B4-A736-55215294134D}' : 'TestPrograms',
	'{66B08E3B-4411-44C0-9A17-2C818A5BB08F}' : 'TestConfiguration',
	'{127400A4-792F-4C40-892E-1AEEA1BBF1E2}' : 'EnumType',
	'{6E68C1F1-A6AF-4235-8E86-AB031F7813E3}' : 'PresentationOptions',
	'{DF8C6267-186F-4A45-8BD4-2545484B102E}' : 'AssetLibraries',
	'{B4A5B240-ED5B-4F0F-B5C7-A1D21FB85939}' : 'ReferenceKeyEventsObject',
	'{4DA70A52-6AE0-4674-95A6-6D7E563CD589}' : 'ReferenceKeyEventsSink',
	'{D893A325-547B-4DE2-8F8B-BD9594025979}' : 'ReferenceKeyEvents',
	'{60C6DD49-AE1F-4937-A6EF-844A85C7D052}' : 'CustomDataEventsObject',
	'{C59649BA-7BE5-42DD-8839-625556A813F0}' : 'CustomDataEventsSink',
	'{D20F6BBC-3EE9-4511-9467-8BED325214EC}' : 'CustomDataEvents',
	'{BC3FDF84-449A-4C14-A825-473FDB60C433}' : 'PluginLicenseManager',
	'{FA98595D-E7A6-4C19-810D-AC891DA24402}' : 'PluginLicenseManagerEventsObject',
	'{80334E55-A73F-45EC-A1D9-EE2A8F5BDD5C}' : 'PluginLicenseManagerEventsSink',
	'{061D42F2-7082-4AEA-94CC-A1D7344C1E37}' : 'PluginLicenseManagerEvents',
	'{2C16787B-83FF-11D4-8DDB-0010B541CAA8}' : 'ViewsEnumerator',
	'{9C88D3AA-C3EB-11D3-B79E-0060B0F159EF}' : 'HelpManager',
	'{2A922EEA-AE03-4C69-9986-D79D5A5A24DA}' : 'HelpEventsObject',
	'{39E63B3F-3A40-4735-9C8F-012AFB75F087}' : 'HelpEventsSink',
	'{285898F7-E731-44FA-B327-540394EBE313}' : 'HelpEvents',
	'{BC985A7D-4B44-4089-870D-0AEE95D5E86A}' : 'EnvironmentBaseCollection',
	'{09E02BBB-8953-4E69-8686-B0AADCFF8D02}' : 'EnvironmentBase',
	'{582865AB-F113-4939-8796-336EA266F8B2}' : 'CommandBarBase',
	'{51BAA695-F419-4D00-B6C5-7C32F4114562}' : 'CommandBarBaseCollection',
	'{917CE8E7-741A-48A3-8E15-89A6DA053C40}' : 'ColorScheme',
	'{817C825E-2D55-4E09-A69E-789E9753959D}' : 'ColorSchemes',
	'{BA80AE34-5BB2-4C90-BFDE-64DA56286813}' : 'FileDialog',
	'{5993FFB7-877A-4AFA-9BAA-73D627DE0D39}' : 'FileDialogEventsObject',
	'{BF078925-9AC1-485E-9638-4DE87CABBCB7}' : 'FileDialogEventsSink',
	'{8CBEA17E-7987-4C21-B3AA-429602F6BAA8}' : 'FileDialogEvents',
	'{388C8482-AC37-4E41-8B59-DC4A2F6BFE45}' : 'ThemeManager',
	'{3D157428-294A-4446-A33D-6BEA664F61D7}' : 'ProgressBarObject',
	'{6322C608-F92C-4CBB-9C17-B1661DA641AB}' : 'ProgressBarSink',
	'{8574FEAB-B050-439E-AC97-9704A217E5A1}' : 'ProgressBar',
	'{C4F1B40A-B7A7-4F92-A9A4-CF8B1DDDE124}' : 'FileUIEventsObject',
	'{63AD687A-3898-44E2-B857-C9DAD84FC9EC}' : 'FileUIEventsSink',
	'{70109AAA-63C1-11D2-B78B-0060B0EC020B}' : 'FileUIEvents',
	'{F2BD70CA-061C-45C4-B057-88526074C390}' : 'CameraEventsObject',
	'{839AA92C-F073-4BB6-9657-51061150E17C}' : 'CameraEventsSink',
	'{DB89B455-6C7F-4008-986F-05D5218DA204}' : 'CameraEvents',
	'{0169EC1F-0694-4353-B28D-3D74B59402D0}' : 'TutorialsManager',
	'{B894B815-AEF1-4FAA-938A-2131E2E5190F}' : 'WebViews',
	'{077CE0DB-81E9-4A4C-B0D3-C5C33B3128A4}' : 'WebBrowserDialogs',
	'{42ACC897-4782-4BB7-9F3F-1C3167372D3D}' : 'WebBrowserDialog',
	'{97040303-12F3-4AE3-952E-FA2C15EB5665}' : 'WebBrowserDialogEventsObject',
	'{0D5E3454-9140-4731-96D3-F86A47C1678F}' : 'WebBrowserDialogEventsSink',
	'{2424A785-6BD9-450C-BF69-1D79626DFBC7}' : 'WebBrowserDialogEvents',
	'{1052B04A-487B-446C-AAAD-90CD3BCCAC9E}' : 'FactoryTableDialog',
	'{A9427B73-D39C-4DA3-9330-3CEB71ECA2B9}' : 'BrowserFoldersEnumerator',
	'{9D063FDB-B597-49B0-8DBC-7EB3D5F715B8}' : 'BrowserFolder',
	'{9BD8EE46-BA95-4CDF-BC13-8C912B4582AE}' : 'SearchBox',
	'{2E7E650F-4051-46F0-96AD-E42CC1C5F980}' : 'SearchBoxEventsObject',
	'{E35E9F66-6F21-467A-A44B-D3CBD0920E8B}' : 'SearchBoxEventsSink',
	'{7C5B6E61-446E-4D01-A3F9-77A28AC9E6F1}' : 'SearchBoxEvents',
	'{9C8B2909-8C33-481E-8CF5-9C269B4E54DC}' : 'ClientNodeResources',
	'{9ACFBDEF-B81B-4B4D-8EA6-8453F1DD6285}' : 'ClientNodeResource',
	'{CABA7470-1B47-492D-A62E-EE7213257C05}' : 'ClientBrowserNodeDefinitionObject',
	'{B142CBF7-AE52-4AC4-ADAB-7A36A2A9A834}' : 'ClientBrowserNodeDefinitionSink',
	'{53318B1D-70C7-4BB0-9103-73ABFA0B3094}' : 'ClientBrowserNodeDefinition',
	'{EF126FC8-7582-4E15-B5DC-194EEE2CEEDA}' : 'BrowserPanesEventsObject',
	'{B159D948-7FC9-4D48-B482-FC7FD152AFCA}' : 'BrowserPanesSink',
	'{F1B96719-11ED-44A6-9AAB-34BC6D05F8EF}' : 'BrowserPanesEvents',
	'{FAD47DA5-3A14-4A2C-9A70-7BCDD992D8A7}' : 'NativeBrowserNodeDefinitionObject',
	'{11D880AF-2B60-4816-A74A-73526CFE6FDD}' : 'BrowserNodeDefinitionSink',
	'{CF10C244-F350-4155-97FD-34A35D996272}' : 'NativeBrowserNodeDefinition',
	'{5F24EB5E-169E-47C1-9C3D-401A01F4415B}' : 'SurfaceGraphics',
	'{0B8D52D2-8147-4407-B2E3-D982ED775F0C}' : 'SurfaceGraphicsFaceList',
	'{18757DD9-20E4-4DF9-9585-1AC6D0B941FB}' : 'SurfaceGraphicsFace',
	'{977D767F-C958-44E8-AB59-8F7267DEBBA1}' : 'SurfaceGraphicsEdgeList',
	'{834BFEF4-D052-4139-93F2-D4F08F3A3121}' : 'SurfaceGraphicsEdge',
	'{C11F6667-E5D4-4A7E-8C47-70AA423E7758}' : 'SurfaceGraphicsVertexList',
	'{7C9B84A9-127C-42B6-A0A7-6CDC39B98CDE}' : 'SurfaceGraphicsVertex',
	'{C958801B-73D0-4031-B9F6-5CDBCE975ABC}' : 'ComponentGraphics',
	'{07F8CD55-9194-4CDB-8403-6BFC4F99D1EE}' : 'BOMQuantity',
	'{5DF86023-6B16-11D3-B794-0060B0F159EF}' : 'ComponentDefinitionReferences',
	'{5DF8601F-6B16-11D3-B794-0060B0F159EF}' : 'ComponentDefinitionReference',
	'{AA044AA3-D685-11D3-B7A0-0060B0F159EF}' : 'AssemblyConstraints',
	'{2FA1D3CF-EAFF-4D47-9E13-E5B074C1565C}' : 'MassProperties',
	'{F2286BBF-D48E-4F85-A613-A48AF46893BC}' : 'InterferenceResults',
	'{FA452CED-C585-4568-BACD-C3DBFAC85D97}' : 'InterferenceResult',
	'{1112CDE3-CD39-4004-8E74-0C019C73F380}' : 'OccurrencePatterns',
	'{773C0E8F-2C4C-4871-93F7-AF9483171461}' : 'FeatureBasedOccurrencePattern',
	'{28DD48B5-8D70-11D4-8DDE-0010B541CAA8}' : 'WorkAxes',
	'{28DD48B7-8D70-11D4-8DDE-0010B541CAA8}' : 'WorkAxis',
	'{46785C3B-7F4A-11D4-8DDB-0010B541CAA8}' : 'WorkPlanes',
	'{46785C3D-7F4A-11D4-8DDB-0010B541CAA8}' : 'WorkPlane',
	'{28DD48C7-8D70-11D4-8DDE-0010B541CAA8}' : 'WorkPoints',
	'{AE309209-288A-4083-BEAB-7DFB7EC9947D}' : 'iMateDefinitions',
	'{F5C82F4B-9B32-488E-920A-31F065B1AD77}' : 'AngleiMateDefinition',
	'{BAC6577B-6985-4B55-BADC-8113EFF69A3C}' : 'CompositeiMateDefinition',
	'{4A943DD0-592A-4E36-8E2C-D2E9DD54B2F5}' : 'FlushiMateDefinition',
	'{425EAA71-D590-4893-AFAB-012380A7CEBA}' : 'MateiMateDefinition',
	'{4FE10280-6679-4500-B7CE-411995D157E7}' : 'InsertiMateDefinition',
	'{6025C779-5DFB-4B1D-B2C9-E7CDD5D18B5F}' : 'RotateRotateiMateDefinition',
	'{06460F0C-B76C-49E4-B24A-3C60142219B9}' : 'RotateTranslateiMateDefinition',
	'{C78E43C1-DB92-414A-9B45-352DFAC434E4}' : 'TangentiMateDefinition',
	'{9788ECD5-7355-4AFC-8784-B139CAC98DF3}' : 'iMateResults',
	'{8AF6DB71-B75D-4D21-A837-4A6699E972BC}' : 'BOM',
	'{12A24FCF-4CBD-403D-9E32-ECE5DC3297E9}' : 'BOMViews',
	'{5538440B-E168-4C38-B817-56F50B538C96}' : 'BOMView',
	'{89B5C2F2-A577-41F7-953A-916CF31BC7D5}' : 'Features',
	'{2D38284B-DEAD-48C3-905D-02D1B7432699}' : 'ChamferFeatures',
	'{539ACB89-A1F6-43E4-BC0A-BDCE1B127584}' : 'ChamferFeature',
	'{8415AC9D-CA60-4AD8-8F79-CE03F00F573D}' : 'ChamferDefinition',
	'{5042E6DE-5FE2-49E6-9371-75554E6A1046}' : 'PartialChamferEdges',
	'{FAD37762-2B83-491D-AB61-CD746D1EBE65}' : 'PartialChamferEdge',
	'{F05DFBBD-F824-48A1-8272-A62F1A524F42}' : 'ExtrudeFeatures',
	'{2FD8A7F5-B548-4E12-9D65-FF47FD063F8C}' : 'ExtrudeFeature',
	'{8B6FA30B-DC7A-4603-8793-445D70FF073E}' : 'PartFeatureExtent',
	'{3098A39F-CCD6-4163-8ADC-2E9504F3E00C}' : 'ExtrudeDefinition',
	'{94ABF5D8-E979-494E-84D3-883672074BD4}' : 'FilletFeatures',
	'{7DE603B3-DAA7-4364-BC8B-77295B53D1DB}' : 'FilletFeature',
	'{448C7AED-838C-44DB-87FC-2D18E74AA05A}' : 'FilletDefinition',
	'{A40068C9-5681-4B3D-961A-1C6360B20BFE}' : 'FilletRadiusEdgeSet',
	'{C6C1652F-6D5B-495D-B7E5-F4DEB205BA25}' : 'FilletSetbackVertex',
	'{325CFE17-8D9E-4977-A3B3-97AC9D827CD9}' : 'FilletSetback',
	'{9374403D-49B0-4DA3-A4CA-55DDAB40D8E1}' : 'FilletConstantRadiusEdgeSet',
	'{A335F5F6-7194-409E-94A7-45B617264920}' : 'FilletVariableRadiusEdgeSet',
	'{3C16D9FD-5F89-4669-B637-B356887583D1}' : 'FilletIntermediateRadius',
	'{237CB3F2-314E-4211-92DC-D69C15BF1B64}' : 'FilletConstantRadiusFaceSet',
	'{FDBEDE20-57AB-44CC-9A84-31E4D730E85D}' : 'FilletFullRoundSet',
	'{A0DB05CD-57E9-47C9-9D33-E648BB57226A}' : 'HoleFeatures',
	'{ABA7FFC5-E604-498E-B1B1-B829D4E059EC}' : 'HoleFeature',
	'{8924897F-3F00-4220-BF8A-76CADC5A10DD}' : 'HolePlacementDefinition',
	'{F5BFBDBA-35EE-424D-A3AD-8D87B22484CF}' : 'HoleTapInfo',
	'{D4D0315D-6874-4E69-9BBB-6E3D28B9122A}' : 'TaperedThreadInfo',
	'{2BC16E62-07F5-4106-B5BD-58C7C660DA2C}' : 'SketchHolePlacementDefinition',
	'{06AC6A50-B820-406B-995A-DDA0CCE3E2F5}' : 'LinearHolePlacementDefinition',
	'{71F90E58-8C83-4C68-9B75-2E14F8BF3A23}' : 'ConcentricHolePlacementDefinition',
	'{1993ABC5-7080-4CB1-9CE3-406B4B70B951}' : 'PointHolePlacementDefinition',
	'{8EB2E33C-2CF3-41E6-9B08-C0C0D15DF5EE}' : 'RevolveFeatures',
	'{87F4CA2E-5700-4FC7-A283-8E2D90FE5F61}' : 'RevolveFeature',
	'{CADFFDB1-11E6-4684-A35E-7EE2064AA46C}' : 'SweepFeatures',
	'{773586BE-A5CE-422F-9036-FAFC8451F011}' : 'SweepFeature',
	'{86338055-4538-47A0-BD9B-06A8C4BD8D93}' : 'Path',
	'{6B9C5A03-557E-477A-A6E4-D2E00FB5B812}' : 'PathEntity',
	'{3D70E84F-AC86-4734-8A36-1672FE750893}' : '_SweepDefinition',
	'{938C8A20-C60B-47C8-A9F4-CDAA7CE06095}' : 'SweepDefinition',
	'{1DD4A980-A4A8-4BEA-8691-FA05F1BAAC95}' : 'SolidSweepDefinition',
	'{ADA699FB-D9E7-4879-A1A3-86D9F2C6F57F}' : 'RectangularPatternFeatures',
	'{58B0C13D-27CC-4F06-93FD-0524B69E6578}' : 'RectangularPatternFeature',
	'{82B32371-11B8-467E-B57E-0112DDD4BB65}' : 'FeaturePatternElements',
	'{1A60195B-72BF-4714-9392-1212EC6260CB}' : 'FeaturePatternElement',
	'{07291B94-27DD-4EAD-BC9A-9123FF5EF420}' : 'RectangularPatternFeatureDefinition',
	'{E2E51C17-C894-45AF-9827-988D38C283C7}' : 'CircularPatternFeatures',
	'{7BB0E824-4852-4F1B-B43C-7F729A3D7EB8}' : 'CircularPatternFeature',
	'{311AF9CD-27E4-48F9-8117-955692A98376}' : 'CircularPatternFeatureDefinition',
	'{26C57F9F-A6AC-4FCD-BE7C-DAE2F0940E8E}' : 'MirrorFeatures',
	'{12BF1F8A-5679-468F-A820-DA5532624CEA}' : 'MirrorFeature',
	'{3026FC98-A183-45C8-84BF-D4EF802A5629}' : 'MirrorFeatureDefinition',
	'{DC6DA623-B4F1-4185-B954-92F92F3C8E21}' : 'SketchDrivenPatternFeatures',
	'{CD9F482B-1EE9-4F16-AEFD-2C5934AC17CC}' : 'SketchDrivenPatternFeature',
	'{B2B45853-725F-4E73-86D1-8B550B5CACD7}' : 'SketchDrivenPatternDefinition',
	'{04370FAD-4F3A-4589-A7F8-6DFA839522D3}' : 'MoveFaceFeatures',
	'{837D8FB2-848D-4A3B-8F83-ECCFDCAC2766}' : 'MoveFaceFeature',
	'{B0A76319-7649-4B77-9159-0975E700253B}' : 'MoveFaceDefinition',
	'{68AF2955-0901-433D-B7C3-D91D637DD21C}' : 'ClientFeatures',
	'{3FD23B6F-222D-485D-A9E8-164C497B17F8}' : 'FaceOffsetFeatures',
	'{31C63BA8-7EB4-4816-A367-F99A12691690}' : 'FaceOffsetFeature',
	'{20C6159F-9ACD-4AA6-B616-1CC57A6F91CA}' : 'FaceOffsetDefinition',
	'{FD93BF70-B8C9-4CEE-8AEB-AAC34B534803}' : 'FaceOffsetPreview',
	'{B148630A-2ECA-4159-8FF2-77CD1B7A79A5}' : 'MidSurfaceFeatures',
	'{247E2AC0-3948-4DD9-88A1-0AC87A794BC7}' : 'MidSurfaceFeature',
	'{6E9FA739-9CD7-49D3-85B9-72F260BFBF52}' : 'MidSurfaceThicknesses',
	'{08389E18-6E84-499B-8F1F-09AC53003178}' : 'MidSurfaceThickness',
	'{D0786DD9-AD8A-431B-B2A9-388211ABD7DD}' : 'ThreadFeatures',
	'{F8957621-7E89-4CB8-AFCA-CE11A556E7A2}' : 'ThreadFeature',
	'{B2CB30BD-4B68-4D6C-8A07-3122FE52E6B9}' : 'StandardThreadInfo',
	'{B76D6529-D84D-4A66-8215-58B6A32D56A9}' : 'iAssemblyFactory',
	'{18517A46-ABB7-4285-94B4-35B3277880F1}' : 'iAssemblyTableRow',
	'{290EC1FE-2BB5-46E8-AB41-919D7455740D}' : 'iAssemblyTableCell',
	'{C7AF47E6-3FDE-469F-B258-85FE0390E7DA}' : 'iAssemblyTableColumns',
	'{90821476-EE63-4328-BC9F-164D0BBF6F9C}' : 'iAssemblyTableColumn',
	'{CE99120C-2AEC-4916-AB66-C14F780325A7}' : 'iAssemblyTableRows',
	'{1DC369B0-C6C9-42B7-BA0F-5A2AB9CA79AE}' : 'FactoryOptions',
	'{29049E48-996E-4799-8DA6-778A0B82AB54}' : 'iAssemblyMember',
	'{A03B2CAF-A5F8-4522-BF79-CF4D497DCF4E}' : 'PlanarSketches',
	'{E09DAF1C-7738-4CDB-B26B-5DE6A2B37573}' : 'RigidBodyResults',
	'{CBE24DE3-529E-4039-BFDF-D014844691F0}' : 'RigidBodyGroups',
	'{611952AC-F765-4950-8863-36C465FA2370}' : 'RigidBodyGroup',
	'{1C4A4777-E52F-405F-BABA-7ED0931E81C0}' : 'RigidBodyJoints',
	'{1C0E39F2-15F3-41EA-94C1-62AD59AD25D9}' : 'RigidBodyJoint',
	'{15AD2867-FEE2-4A5B-9F07-FDC0A4FF5C72}' : 'AssemblyJointsEnumerator',
	'{9C7891F4-F438-445A-AD22-8FB29E343231}' : 'AssemblyJoint',
	'{AB9D8E26-4BEC-4E22-84B0-B1ECDED332D8}' : 'AssemblyJointDefinition',
	'{D0BD7B89-04B5-4165-8E8D-1DB705A02E47}' : 'UserCoordinateSystems',
	'{F0854465-652D-4375-98A4-7C875BFE7A9C}' : 'UserCoordinateSystem',
	'{598714D9-653D-4D2B-B7BB-139C3E9E38B1}' : 'UserCoordinateSystemDefinition',
	'{47005682-42D1-4831-A4BC-63AD38B98D6E}' : 'BIMComponent',
	'{03B09E04-FA49-40EA-AE2D-FF7972025350}' : 'BIMComponentDescription',
	'{34ACFD9F-B9B0-4D81-B44C-55AEEAEE16BC}' : 'BIMComponentPropertySets',
	'{5F89369C-998C-4AD6-B59D-FBA9AFDCFB65}' : 'BIMComponentPropertySet',
	'{A145B58E-E928-4180-951B-D7E652298E2A}' : 'BIMComponentProperty',
	'{7C1BEFD9-4296-4794-B3A2-8025809570D8}' : 'BIMConnectors',
	'{12DA4D02-DCE6-4F08-ADEB-9EE13C559C52}' : 'BIMConnector',
	'{E41CA526-545A-4782-A383-C44FC7523552}' : 'BIMConnectorDefinition',
	'{2D6BA5C4-3929-44A3-8D59-5A173034BBF1}' : 'BIMCableTrayConnectorDefinition',
	'{744F35C4-CD6F-46C3-87B8-80425AB4AFA2}' : 'BIMConduitConnectorDefinition',
	'{1FE852AA-E1B7-4160-8F8D-302E0B46BC52}' : 'BIMDuctConnectorDefinition',
	'{1F222D21-CBB5-4FC4-A6CF-0387224A7F2C}' : 'BIMElectricalConnectorDefinition',
	'{E52803C6-7F1E-4D7B-9C0E-D4FA6BFFA00D}' : 'BIMPipeConnectorDefinition',
	'{99C8344C-60E3-46CA-A32D-1EF2010EB01D}' : 'BIMConnectorLinks',
	'{8E05BCC6-20B2-477A-A318-CB7116D8D0A7}' : 'BIMConnectorLink',
	'{7771DA50-AFDF-4E9A-9055-1CAA9B9CFFE5}' : 'SimulationManager',
	'{7771DA51-AFDF-4E9A-9055-1CAA9B9CFFE5}' : 'DynamicSimulations',
	'{7771DA52-AFDF-4E9A-9055-1CAA9B9CFFE5}' : 'DynamicSimulation',
	'{7771DA58-AFDF-4E9A-9055-1CAA9B9CFFE5}' : 'DSJoints',
	'{055EC022-CD9B-4983-97E2-2EC073939046}' : 'DSJoint',
	'{055EC023-CD9B-4983-97E2-2EC073939046}' : 'DSJointDefinition',
	'{055EC024-CD9B-4983-97E2-2EC073939046}' : 'DSDegreesOfFreedom',
	'{055EC025-CD9B-4983-97E2-2EC073939046}' : 'DSDegreeOfFreedom',
	'{7771DA56-AFDF-4E9A-9055-1CAA9B9CFFE5}' : 'DSValue',
	'{7771DA57-AFDF-4E9A-9055-1CAA9B9CFFE5}' : 'DSValueGraph',
	'{055EC026-CD9B-4983-97E2-2EC073939046}' : 'DSResults',
	'{055EC027-CD9B-4983-97E2-2EC073939046}' : 'DSResult',
	'{7771DA53-AFDF-4E9A-9055-1CAA9B9CFFE5}' : 'DSLoads',
	'{7771DA54-AFDF-4E9A-9055-1CAA9B9CFFE5}' : 'DSLoad',
	'{7771DA55-AFDF-4E9A-9055-1CAA9B9CFFE5}' : 'DSLoadDefinition',
	'{7771DA59-AFDF-4E9A-9055-1CAA9B9CFFE5}' : 'DSSettings',
	'{B4D0EB63-4D3B-42A6-BE38-855EB5DA68E3}' : 'VisibleOccurrenceFinder',
	'{EF706A55-28C3-41A6-8D99-EE900BDBCD9D}' : 'AssemblyJoints',
	'{715899F9-C5E6-4A31-96C7-151D74A852B8}' : 'PointClouds',
	'{6E45ED1A-92ED-469A-9CE0-79C26C9CB5E5}' : 'PointCloud',
	'{10DE860A-67D1-47ED-A23A-291BD48E25E9}' : 'PointCloudRegions',
	'{E34C07F3-B8FF-4181-ADC4-DEE3D6550961}' : 'PointCloudRegion',
	'{F20B72F3-D856-45E8-A71A-0753F12D7A10}' : 'PointCloudScans',
	'{A962939B-0A11-490F-AC66-DC0FDAA3DD75}' : 'PointCloudScan',
	'{AADD24A8-0094-41C6-BF61-C79E700AA1E2}' : 'PointCloudCrops',
	'{2D5EB497-6E4D-4B66-B185-EB6C7C188F2F}' : 'PointCloudCrop',
	'{D2F65CFD-A8D7-44D1-8262-9FD5BCA8FECA}' : 'ImportedComponents',
	'{239475B6-6DCA-4683-B410-A5788BF2077B}' : 'ImportedComponent',
	'{903F1E1B-1A0E-4344-820B-CDD9619C0FDC}' : 'ImportedComponentDefinition',
	'{22D71B5C-2F5E-4A1B-9328-ABE89F78ABC6}' : 'iMateDefinitionsEnumerator',
	'{5DF86093-6B16-11D3-B794-0060B0F159EF}' : 'EdgeLoops',
	'{5DF86096-6B16-11D3-B794-0060B0F159EF}' : 'Vertices',
	'{8BC9C1AA-4238-4112-A5FC-15F3765E5336}' : 'TextureMaps',
	'{AF6AFE3F-4249-410E-A4F8-9399EE807D30}' : 'TextureMap',
	'{D96060F8-0E08-4E73-8D5E-37F506A1A738}' : 'TextureCoordinateSet',
	'{AD3341ED-F50C-46F3-AB93-601CA37413E6}' : 'PartFeaturesEnumerator',
	'{5C93A2CD-ECCA-4998-9DC4-D439BD9FE3DB}' : 'DraftAnalyses',
	'{9C9D6F69-F26B-4311-A688-17C04EC292BE}' : 'DraftAnalysis',
	'{BB075EDC-49B3-4F03-8737-5E20737B1AEB}' : 'AnalysisManager',
	'{5DF86022-6B16-11D3-B794-0060B0F159EF}' : 'ComponentDefinitions',
	'{46AEA719-4302-11D4-B7AB-0060B0F159EF}' : 'ComponentOccurrenceProxy',
	'{206B59B0-22A6-11D4-B7A8-0060B0F159EF}' : 'DraftingStandard',
	'{46AEA72F-4302-11D4-B7AB-0060B0F159EF}' : 'EdgeProxy',
	'{46AEA72C-4302-11D4-B7AB-0060B0F159EF}' : 'EdgeLoopProxy',
	'{46AEA72D-4302-11D4-B7AB-0060B0F159EF}' : 'EdgeUseProxy',
	'{46AEA72B-4302-11D4-B7AB-0060B0F159EF}' : 'FaceProxy',
	'{46AEA72E-4302-11D4-B7AB-0060B0F159EF}' : 'FaceShellProxy',
	'{1435773B-06FC-46E8-B965-5845697D2A6B}' : 'SweepGraphics',
	'{C6DE930F-09D7-487F-A4C9-401AA8B19879}' : 'GraphicsNodeProxy',
	'{5B94A1C2-5FA9-4093-87DD-11B7115B9F02}' : 'OccurrencePatternElementProxy',
	'{46AEA729-4302-11D4-B7AB-0060B0F159EF}' : 'SurfaceBodyProxy',
	'{46AEA730-4302-11D4-B7AB-0060B0F159EF}' : 'VertexProxy',
	'{3E0ED07A-F5ED-46BF-8903-EBC1B409A270}' : 'AssetTexture',
	'{CC1FB682-EF98-4FE5-9934-143CFB8C65B1}' : 'ChoiceAssetValue',
	'{5F0359BB-A074-4CD1-98EF-F66DAE4649E9}' : 'FloatAssetValue',
	'{48D3D9AD-F3F0-41E8-B4D8-6DA2533CCFC9}' : 'IntegerAssetValue',
	'{4479E5B2-48BF-4760-BA24-0A0CE854DF24}' : 'BooleanAssetValue',
	'{9D7514D7-EA00-4F2D-8F66-0E395B21C284}' : 'ColorAssetValue',
	'{AD623DC3-5354-483D-99A1-C7ADDB0C06CF}' : 'TextureAssetValue',
	'{9ADC4649-06DC-449E-ABE8-5DCA6F4C7788}' : 'StringAssetValue',
	'{0FC5FA72-0397-4522-9E58-764385FA9B69}' : 'FilenameAssetValue',
	'{186F6C0F-C3A2-4798-9685-C773181074C1}' : 'ReferenceAssetValue',
	'{A095B86B-84EF-4364-888E-1F6F03EAA73F}' : 'MaterialAsset',
	'{8530B3FF-DBD2-4C75-A6EC-0755B8229AE7}' : 'ApprenticePrintManager',
	'{F90311E1-7249-40AF-A597-8AFF681BFA93}' : 'ApprenticeDrawingPrintManager',
	'{C343ED83-A129-11D3-B799-0060B0F159EF}' : 'ApprenticeServerDocument',
	'{59D3FA3A-ACE0-11D3-B79A-0060B0F159EF}' : 'ApprenticeServerDocuments',
	'{9CAF98A3-33EA-11D3-B78F-0060B0F159EF}' : 'FileSaveAs',
	'{C343ED82-A129-11D3-B799-0060B0F159EF}' : 'ApprenticeServer',
	'{C343ED84-A129-11D3-B799-0060B0F159EF}' : 'ApprenticeServerComponent',
	'{4F589652-207C-11D4-B7A5-0060B0F159EF}' : 'ApprenticeServerDrawingDocument',
	'{EF42229B-CAC3-488D-BCC4-C992FC7795AE}' : 'InventorServerObject',
	'{71A0E8AF-8F3E-485D-BB40-7C98163F9C14}' : 'VbaApplication',
	'{F8841598-132A-4A18-BE1F-EBDD2067C648}' : '_VbaImplementationEvents',
	'{AB36A045-09FE-4A67-8637-E08CC2735092}' : '_VbaApplication',
	'{49A9C1BC-D718-4DCB-AAD8-8FB4285EFA45}' : 'AliasFreeformFeature',
	'{8DE224FA-1DA2-4B05-BE2B-3E7FB6361FC2}' : 'AliasFreeformFeatureProxy',
	'{3C007201-8D66-47BD-AD94-2012FF75C4C5}' : 'AliasFreeformFeatures',
	'{AF22C0E0-AEBC-4009-BD3E-85EBF9C9ED58}' : 'AnalyticEdgeWorkAxisDef',
	'{076FFE46-6694-42EE-9F7F-E61F71434845}' : 'AngleConstraintProxy',
	'{312EFE2A-648A-4715-85F4-B7A1EF02CCB9}' : 'AngleExtent',
	'{CFA8AC15-B4C1-4703-A672-DAED79017FF3}' : 'AngleiMateDefinitionProxy',
	'{95137870-2785-4E40-BE13-1D23D6CDF348}' : 'AngularModelDimensionProxy',
	'{6A979CE4-093B-4D91-9C67-CFE4D38C27E3}' : 'AnnotationPlaneProxy',
	'{E8057590-7265-4294-9D82-1A93BF64178F}' : 'LinearModelDimensionProxy',
	'{744023BD-507E-43EA-B378-60D2F553C51E}' : 'RadiusModelDimensionProxy',
	'{68E038B4-ED9F-4FE9-A4E0-8ABE96A474CB}' : 'DiameterModelDimensionProxy',
	'{02F3D9FA-F750-4C1B-8A2E-A2C5BB99C76C}' : 'AnnotationPlanes',
	'{3FC94EB5-AEBD-4F3F-A2A4-B6CE57113C01}' : 'InventorServer',
	'{B6B5DC40-96E3-11D2-B774-0060B0F159EF}' : '_Application',
	'{E3571299-DB40-11D2-B783-0060B0F159EF}' : 'ApplicationAddInSite',
	'{C343ED7B-A129-11D3-B799-0060B0F159EF}' : 'Command',
	'{93224595-EAF4-4AE2-9604-16A2854AFF4B}' : 'ButtonDefinitionHandlerObject',
	'{96750E11-92EA-457A-BF5E-6FA15C44B8EE}' : 'ButtonDefinitionHandlerEventsSink',
	'{35A16D52-2DE8-4DF8-B8EB-83110BACD270}' : 'ButtonDefinitionHandler',
	'{EBB974BD-2A69-4125-899A-5752878B7E55}' : 'EnvironmentBaseHandlerObject',
	'{165776AC-95DC-4BD0-8288-BE844390282F}' : 'EnvironmentBaseHandlerEventsSink',
	'{6947535C-49CA-43FC-8B6D-95ACFE104275}' : 'EnvironmentBaseHandler',
	'{CAEB520A-F52E-4F2B-AE02-CE0BF9944814}' : 'DocumentSubTypeHandlerObject',
	'{94F1E029-984C-4DDC-9B12-003982C02E06}' : 'DocumentSubTypeHandlerEventsSink',
	'{66D547CF-949A-4B31-BC1B-AF002DC97D2B}' : 'DocumentSubTypeHandler',
	'{E3571293-DB40-11D2-B783-0060B0F159EF}' : 'ApplicationAddInServer',
	'{0562B816-F05F-4293-AF39-D2F640E42740}' : 'SheetMetalComponentDefinition',
	'{DA33F1A5-7C3F-11D3-B794-0060B0F159EF}' : 'PartFeatures',
	'{1D09051E-D674-4ABE-BEC9-5A58016455B1}' : 'NonParametricBaseFeature',
	'{2C30965F-FD0D-4D6E-AC98-797F2F0E2DEB}' : 'CoilFeatures',
	'{B9036BF2-EBE0-4593-92B6-DBCD421C6BDF}' : 'CoilFeature',
	'{0218B59B-0CE5-4CA1-9A3B-F7D266C4E75F}' : 'DecalFeatures',
	'{9C693BB0-7C99-4D06-961E-99936273C492}' : 'DecalFeature',
	'{91BDBCAB-AC12-4216-ACE4-4F561D7DD4BD}' : 'DeleteFaceFeatures',
	'{4CDC6B45-25DB-442E-BF8B-12C87365788E}' : 'DeleteFaceFeature',
	'{730B9714-80D2-4009-8904-1AEF4EAF3F23}' : 'EmbossFeatures',
	'{6A0A9BAD-53F2-4254-A34E-9262F980B5CE}' : 'EmbossFeature',
	'{C77D9639-C58A-4E5A-BAE0-14966E37DDEE}' : 'FaceDraftFeatures',
	'{EA1D0D38-93AD-48BB-84AC-7707FAC29BAF}' : 'FaceDraftFeature',
	'{8A551127-A520-46FD-A9C4-5ECD271576FC}' : 'FaceDraftDefinition',
	'{E15EF363-30C7-420B-91DE-B76BE5F6007F}' : 'FreeformFeatures',
	'{88C36A1E-2212-4E9C-BBDB-3155DC8C06E9}' : 'FreeformFeature',
	'{69F95DF7-6F84-4FF8-8060-AB921DF1E4F1}' : 'DirectEditFeatures',
	'{602389D5-6C6A-4368-A6F2-47D54FA1FBA4}' : 'DirectEditFeature',
	'{DE936728-E326-4EE4-A671-9AC25F43868C}' : 'DirectEditOperations',
	'{86EF3B55-8CEB-45E8-9C9C-5F4430679B7C}' : 'DirectEditOperation',
	'{1426BDF8-DD91-4FF0-AD8D-BB0EC8797B24}' : 'KnitFeatures',
	'{E408524C-B7A1-4F17-921E-160774F4DE5D}' : 'KnitFeature',
	'{97D6B280-1D62-48E6-B4B9-007F25F7A3A5}' : 'BoundaryPatchFeatures',
	'{16B36EBE-2DFA-4474-B11B-DF3D57C109B0}' : 'BoundaryPatchFeature',
	'{4FF4C556-DB2C-4FD7-A7E5-06C171C18D7B}' : 'BoundaryPatchDefinition',
	'{4CD53A13-201C-402A-A729-EFEB24A1417C}' : 'BoundaryPatchLoops',
	'{4DF199B9-D7C8-4770-9954-2EFF94867CEC}' : 'BoundaryPatchLoop',
	'{24A0170B-C253-4A3C-9639-5DE9818A8F31}' : 'LoftFeatures',
	'{F7DDBE1D-2C8E-48B9-9E52-FC0BFB7D59A6}' : 'LoftFeature',
	'{E405BACE-0EE8-4427-B6BE-82CC11F9CC35}' : 'MapPointCurves',
	'{52909F65-AE2E-4997-B3F5-527FE09BF5BE}' : 'MapPointCurve',
	'{3E43E559-0053-402D-BE5F-4AC170C11A04}' : 'LoftRails',
	'{02466B5A-9C4B-48C4-BFA0-5590DB014745}' : 'LoftRail',
	'{FBEBA281-9346-4AC6-B324-6CEB7318BEBE}' : 'LoftDefinition',
	'{F8FBACE4-75A7-4493-B2D8-492AC937F3E5}' : 'LoftSectionDimensions',
	'{3138A370-A692-42B1-8C91-7981A9A0F12C}' : 'LoftSectionDimension',
	'{59E208A8-BB82-4322-92D6-DA364F8B9AB0}' : 'NonParametricBaseFeatures',
	'{559C5073-6378-47FD-AA38-DE0BB46A9268}' : 'NonParametricBaseFeatureDefinition',
	'{3CBD2849-0258-4583-9CE0-578A71CB7483}' : 'ReplaceFaceFeatures',
	'{5D8B9732-07F2-4E90-A4AB-C98FB56944A1}' : 'ReplaceFaceFeature',
	'{436A627D-919B-4B92-B242-268F7266D8A1}' : 'RibFeatures',
	'{D65B8777-CF40-4542-9A0F-28F2F6EF0678}' : 'RibFeature',
	'{5B078EF2-5839-4B6A-97D1-BB8F5D9CFD78}' : 'RibDefinition',
	'{85672B0C-EA86-4DF1-B223-51DD72F29566}' : 'BossSets',
	'{FB1FDFB0-239C-4040-9B22-7ACACCFFE82E}' : 'BossSet',
	'{721CC25E-D96C-4E25-BED5-04EF710574B4}' : 'RuledSurfaceFeatures',
	'{E58169E1-CCA4-432A-9626-A37ABF5F287E}' : 'RuledSurfaceFeature',
	'{148406BE-AC67-4E05-B5E9-A427269D3A28}' : 'RuledSurfaceDefinition',
	'{89A80CCD-6F08-462F-98CB-BD062E77E8D4}' : 'RuledSurfaceEdgeFacePairs',
	'{7E763E3B-84CB-4D77-B4F1-C18A1BEF0EA6}' : 'RuledSurfaceEdgeFacePair',
	'{3B4B3DE9-7B05-47A7-975A-2C370BBBF974}' : 'ShellFeatures',
	'{E861980A-A56F-416A-BF52-876C8A06CE4E}' : 'ShellFeature',
	'{C80E7C12-B126-45F2-A228-704248D58530}' : 'ShellDefinition',
	'{0F8F253B-5ED8-4AE0-9C62-3DEFDCCD0BC4}' : 'ShellThicknessFaceSet',
	'{209DF795-8088-4158-969C-0CC120E0A2A3}' : 'SplitFeatures',
	'{78D752FD-9090-4AEA-9CF2-247ABA9D1936}' : 'SplitFeature',
	'{F59CE3B0-44CC-4FB5-9C81-7234A25DD381}' : 'ThickenFeatures',
	'{97E8752C-E818-41FF-8C13-D10B6FBC522F}' : 'ThickenFeature',
	'{347FB32C-79ED-4A5B-89B1-7B14FF6A9CA8}' : 'ReferenceFeatures',
	'{298849A9-ECAB-4234-9675-6FAA66A95E4D}' : 'ReferenceFeature',
	'{EAADC3AE-D599-495E-A56C-FA79AE3E8848}' : 'SculptFeatures',
	'{7E2A1EB5-F770-45BD-8DC5-8FEE60664D9F}' : 'SculptFeature',
	'{65A5B1BC-9F61-4F5D-A113-66EDC3DAAAC0}' : 'SculptSurface',
	'{109C1DF4-2290-44AC-9E90-A108D090B4E9}' : 'TrimFeatures',
	'{98588913-EE07-4969-8939-3DFDEE09180E}' : 'TrimFeature',
	'{4A355C86-508E-4A45-80C3-001139E9FD81}' : 'ExtendFeatures',
	'{2DADCD08-8ED5-4F71-88BF-481E8B0E9847}' : 'ExtendFeature',
	'{3E39E3B3-FA8E-463D-A191-6D7A7CB8E7AE}' : 'BendPartFeatures',
	'{2CBE5BA6-3501-4389-AF3F-AD114C0DAB5A}' : 'BendPartFeature',
	'{D50258F5-140B-4AE1-BCC7-3CB2438B04E1}' : 'iFeatures',
	'{98675AD1-A109-43DE-A7D7-1612BC503E0E}' : 'iFeature',
	'{358B0B8E-D2C7-4D76-AAC6-33009864424E}' : 'iFeatureDefinition',
	'{AF669E3B-2FC3-4731-96C4-2CC724B98E60}' : 'iFeatureInputs',
	'{6A89E379-03FC-440E-A655-6111E86247A1}' : 'iFeatureInput',
	'{5F15A208-8871-42B9-8421-D0555100A7D9}' : 'iFeatureTable',
	'{F0684BBA-73A5-45B8-8D38-E64A53735C9E}' : 'iFeatureTableRow',
	'{ABC49BF6-3E83-45A6-AF98-059245620FF4}' : 'iFeatureTableCell',
	'{34295D6D-002B-40DC-B1E9-E0D658532EF0}' : 'iFeatureTableColumn',
	'{82B8F63A-474B-4DAC-AE2D-E9F5E9BB2C2E}' : 'iFeatureTableColumns',
	'{4A66B607-4991-4FA2-A361-CD8424A99A70}' : 'iFeatureTableRows',
	'{3C69FF6F-6ADD-4CF5-8E9B-32CBD2B6BBF7}' : 'iFeatureTemplateDescriptor',
	'{41E90FED-639B-468D-A09E-30363D40DE7F}' : 'SketchesEnumerator',
	'{010971C0-0359-4820-A5EA-5EB9E6FFDA76}' : 'CombineFeatures',
	'{2D0B10A8-711C-4352-AEE1-C8465CBDC36B}' : 'CombineFeature',
	'{972006AB-5037-4850-AF98-8D3B5A55C1F4}' : 'MoveFeatures',
	'{F0AF7CF3-7F4E-4A34-B384-7C98CE2843B2}' : 'MoveFeature',
	'{61899B80-0F4D-49F5-A3FF-E727155139FD}' : 'MoveDefinition',
	'{279EB42E-C733-4AA9-BFA8-2A8FCF2B2A4D}' : 'FreeDragMoveOperation',
	'{8A11BC6C-E0A4-4954-851A-A5E43144046C}' : 'MoveAlongRayMoveOperation',
	'{1E4085FD-7428-4EA1-B3EF-B2ADDD7F8F5C}' : 'RotateAboutLineMoveOperation',
	'{BC1B0D6F-086B-43CC-91CC-6BEF7D7E35C1}' : 'MoveOperation',
	'{A110C93B-A3B5-4717-A697-87EA0126216F}' : 'BossFeatures',
	'{16DC54D8-5357-4ECC-9EB5-E4BDD7DB287C}' : 'BossFeature',
	'{6AC23513-A004-4DC5-B77D-6D18BCB5E43E}' : 'GrillFeatures',
	'{5EC2AE01-F47C-4E11-B8CD-67A017E07132}' : 'GrillFeature',
	'{2AD0B878-13E1-4BB0-BDFF-BBAA7DA553DD}' : 'LipFeatures',
	'{5404EF69-8B8C-4CCF-BC9B-D9BC8B4F4A2E}' : 'LipFeature',
	'{0E000A5B-67FD-4B23-A312-E6E5F444C045}' : 'RestFeatures',
	'{669AFAAA-7F38-44FB-B50A-161D5C713C69}' : 'RestFeature',
	'{9B108AAB-237A-460D-BC99-40FAF5EABD65}' : 'RuleFilletFeatures',
	'{A783590A-7480-4A9E-BDA3-D805C2CD7281}' : 'RuleFilletFeature',
	'{ED254D15-6E11-409A-83A0-BB085F017204}' : 'SnapFitFeatures',
	'{BC465119-C96D-4E6C-B5FE-AE114280B6A0}' : 'SnapFitFeature',
	'{FACF4224-09C8-4856-A2B8-6EAA1BFCB5CA}' : 'UnwrapFeatures',
	'{93392430-44EA-4C19-887F-86717E2EDDF8}' : 'UnwrapFeature',
	'{95E4A10F-0335-4C06-8B61-065A485AE9C8}' : 'UnwrapDefinition',
	'{C44DF7B9-A598-407F-AE04-2594D11B9DC7}' : 'CoreCavityFeatures',
	'{8C1243A8-F557-4626-A5F1-8B9F988B2EFC}' : 'CoreCavityFeature',
	'{6486F293-4BCF-42EA-91A3-08C82ADBED52}' : 'CoreCavityDefinition',
	'{45D64D2D-8D31-4ABD-BB94-E55F0879A90C}' : 'ReferenceComponents',
	'{CF891949-B3AD-4A38-9254-7CAFE0F3B7F6}' : 'DerivedPartComponents',
	'{6D7C8AC8-722D-46C8-B6D9-F6001F1EDD2D}' : 'DerivedPartComponent',
	'{BEBB7A1A-2E50-4C62-A4E1-64B2E9A18AE6}' : 'ReferenceFeaturesEnumerator',
	'{79B234B7-D73B-43B2-91BC-75A419703C12}' : 'DerivedPartDefinition',
	'{90A1D182-6B1E-49C2-9DAF-3A74B31BE6D4}' : 'DerivedPartEntities',
	'{FB78F43A-8F10-40F3-8C04-62EEA948C716}' : 'DerivedPartEntity',
	'{EC6AB9BC-0F8E-49E6-B809-09E5962BA707}' : 'Sketches3DEnumerator',
	'{14A842C0-8BD2-431B-B1DA-A487A6E35B18}' : 'SketchBlockDefinitionsEnumerator',
	'{F41437F2-9B75-4C35-857C-98646F87B551}' : 'DerivedPartUniformScaleDef',
	'{11C8C1C5-74AB-415F-AE6B-F358CE0FDA4C}' : 'DerivedPartTransformDef',
	'{E9AFE0F2-46D5-4022-B668-F0AE494C48B1}' : 'DerivedPartCoordinateSystemDef',
	'{A52D98FA-2E72-4170-ABB4-6D10C2BCB095}' : 'DerivedAssemblyComponents',
	'{A1D2EAAD-28A1-4692-BC13-883879C68894}' : 'DerivedAssemblyComponent',
	'{18DED264-417F-4B81-828C-B8806397C7C3}' : 'DerivedAssemblyDefinition',
	'{DEB206F5-3467-4860-869E-97479BA38D36}' : 'DerivedAssemblyOccurrences',
	'{4DEAC0A5-E998-4958-8344-D866385CECF2}' : 'DerivedAssemblyOccurrence',
	'{2520A915-6F04-4248-B5A3-05B15E651FD9}' : 'iFeatureTemplateDescriptors',
	'{62F5FBCA-EC38-48F5-9CA7-1D38FED4D443}' : 'iFeatureComponents',
	'{2B7A8B03-DD00-4DB8-94F9-9BFF87DB8C06}' : 'iFeatureComponent',
	'{12EC238A-7178-44C6-BF92-F95F87CD7592}' : 'DerivedAliasComponents',
	'{61B9A367-8CCB-4868-A573-CCE62C5C35B6}' : 'DerivedAliasComponent',
	'{1EAA55EA-9631-4A9F-95BA-752C3924E6EF}' : 'DerivedFuturePartComponents',
	'{6F9B064A-7DCD-4AD2-ADFD-05B54952C498}' : 'DerivedFuturePartComponent',
	'{3A6CBA65-5300-4F62-BEB6-4C37C22E10E6}' : 'DerivedFuturePartDefinition',
	'{846AA6A0-434A-42AD-9529-A4D1755802A8}' : 'DerivedFutureAssemblyComponents',
	'{566CDFED-4434-47A8-997A-EAD9265A6B9F}' : 'DerivedFutureAssemblyComponent',
	'{5BA9F691-6325-48B1-A248-4A1E46C315B5}' : 'DerivedFutureAssemblyDefinition',
	'{A4B4E128-2739-4B52-8849-1E19DC7AE4C9}' : 'DerivedFutureAssemblyOccurrences',
	'{8A641557-B2B8-4D91-9106-177EEC2B9F2E}' : 'DerivedFutureAssemblyOccurrence',
	'{6CFEA047-E49B-4BD9-92F6-F982D7AFBBDA}' : 'ShrinkwrapComponents',
	'{82917413-0741-40A5-BAAC-B9E244FFE57A}' : 'ShrinkwrapComponent',
	'{AE5289FB-69D3-4331-BC05-0043FB896B45}' : 'ShrinkwrapDefinition',
	'{07FB0B7F-D08F-473F-8EF0-A5E6B4CBA3BC}' : 'Sketches3D',
	'{5987714B-D55A-4AED-8AE5-97C062EC1F68}' : 'WorkSurfaces',
	'{D136B45B-7B03-4027-9759-AECD06393300}' : 'WorkSurface',
	'{CE45B869-6097-4A49-81B4-0FB7A350079C}' : 'PartEventsObject',
	'{BABF5BAF-9878-11D4-8DE2-0010B541CAA8}' : 'PartEventsSink',
	'{BABF5BB7-9878-11D4-8DE2-0010B541CAA8}' : 'PartEvents',
	'{B9F30FBA-DABE-4327-AAB3-65E2160135C1}' : 'iPartFactory',
	'{2DB692B1-9CA2-40CA-AD6B-D1250C063724}' : 'iPartMember',
	'{A8DB137E-896E-4B61-8813-E49040BBE99E}' : 'iPartTableRow',
	'{901E43F5-403A-45C8-A93C-E9509386BB74}' : 'iPartTableCell',
	'{4C9E5B40-4741-4AD9-AACC-47C2BAD5E903}' : 'iPartTableColumns',
	'{8B3FEE20-C49D-495B-AA3E-B90AE49B736B}' : 'iPartTableColumn',
	'{B01CC9E0-93E8-4482-9321-D8F52A7AB213}' : 'iPartTableRows',
	'{BC450138-0F96-4342-BC2C-239747CD4797}' : 'SketchBlockDefinitions',
	'{496CD658-85F0-449A-BA13-9B94962ACBEA}' : 'ModelToleranceFeatures',
	'{10F5BF67-5FAB-44DD-B1D8-BCE056E71000}' : 'ModelDatumReferenceFrames',
	'{8227B88D-4834-487E-8DC1-92DACA5D9E02}' : 'ModelDatumReferenceFrame',
	'{E0DA41A0-C0DA-4BA9-807E-ED6514657F7E}' : 'ModelDatumReferenceFrameDefinition',
	'{5B9228F3-FB28-487E-9EC2-D948901CA89F}' : 'SheetMetalStyles',
	'{46A4AA12-70D3-4BEC-B059-D285F084B979}' : 'SheetMetalStyle',
	'{F69435CA-41FA-4FDC-8E07-2D677A30AB2C}' : 'UnfoldMethod',
	'{5D0AB9A7-FCDB-4815-837B-BDCADEE5CEB2}' : 'UnfoldMethods',
	'{A7E07EA5-369D-11D6-8E02-0010B541CAA8}' : 'FlatPattern',
	'{1D32B73F-D1F8-4E1C-80B9-590FA6F008B2}' : 'FlatBendResults',
	'{F7EC4513-DB91-4D3D-ABB6-699D301F4387}' : 'FlatBendResult',
	'{AE99EE3F-A9E9-498C-AE33-C919105745F4}' : 'Bend',
	'{22A94C59-66DE-4B31-BA10-BCBB774B4AAF}' : 'FlatPunchResults',
	'{CFC1C004-270D-4C19-BBE5-5D380A2A7D7E}' : 'FlatPunchResult',
	'{75A1BC5F-78FC-4E62-99C7-623813E36C43}' : 'FlatPatternFeatures',
	'{AB61EB61-7785-4854-9498-8210B3DA80B2}' : 'CornerChamferFeatures',
	'{8B72B033-1F46-4D07-8B26-6E9A718A1533}' : 'CornerChamferFeature',
	'{E16AEA74-FC21-4762-85D9-A4B20B06A095}' : 'CornerChamferDefinition',
	'{5908F091-036B-49E5-9685-3228EB2EE3E2}' : 'CornerRoundFeatures',
	'{3822A30C-5DAB-449B-8AAA-BDA9DEF3FBF5}' : 'CornerRoundFeature',
	'{21BBAED3-F2FD-4A60-9AE4-7A10A8E2BC2D}' : 'CornerRoundDefinition',
	'{289220CD-E245-473D-B626-114D97F9EDCB}' : 'CornerRoundEdgeSet',
	'{994CF5C9-F097-43AB-8741-76D5DD3DC2BA}' : 'CutFeatures',
	'{CB8542A0-1559-4E06-BAAE-EFA0BFEF86A7}' : 'CutFeature',
	'{3B809336-2821-4E36-B2A1-31B987537E57}' : 'CutDefinition',
	'{C08C777F-2E1B-469D-A1A7-E379ED046444}' : 'PunchToolFeatures',
	'{0DC3C610-F23D-44AD-B688-A47CAB5B04CB}' : 'PunchToolFeature',
	'{B534FD24-88CA-435C-95D5-F0DB0FB0238D}' : 'CosmeticBendFeatures',
	'{B9694561-1C36-4D14-9930-4B8152E1984F}' : 'CosmeticBendFeature',
	'{D092DF11-377A-47AA-92DA-664BE32DDDD4}' : 'ASideDefinition',
	'{F98E10EB-6BA5-461D-A3D7-5A90CCE47734}' : 'FlatPatternOrientations',
	'{830E9463-F267-4A8E-8CE5-8D417295459D}' : 'FlatPatternOrientation',
	'{BF8CF130-DAD5-444E-9DED-16AD1178DE2F}' : 'FlatPatternPlates',
	'{938A5052-5007-48B1-9629-D00898FD6855}' : 'FlatPatternPlate',
	'{AA1A04EB-B571-4568-86E6-7732B8330E9C}' : 'BendsEnumerator',
	'{6047CD23-889D-458D-9AFF-3CD3EB248BAA}' : 'ASideDefinitions',
	'{4E19FF37-38A9-494F-AC1E-557D5D01CDB4}' : 'AssemblyJointProxy',
	'{0249C8A3-806D-4A1D-8BC0-4699BE1203AF}' : '_Document',
	'{E12CF633-9F24-427A-A6F9-D5A7D7BCB314}' : '_VbaImplementationAssemblyEvents',
	'{E60F81E1-49B3-11D0-93C3-7E0706000000}' : '_AssemblyDocument',
	'{E4FA0888-2179-4CB4-9277-B103A9C40812}' : 'AssemblySymmetryConstraintProxy',
	'{F9885CB4-7B68-45E3-953F-B287BE1C6FAF}' : 'AssemblyWorkAxisDef',
	'{62F1DC23-FB86-4D0C-81B3-05BF2CD775F4}' : 'AssemblyWorkPlaneDef',
	'{8E3A45D9-4432-4408-B261-12E725F97A5D}' : 'AssemblyWorkPointDef',
	'{AE27E3D2-63C8-4D39-B2CA-A6387AE5D7B3}' : 'BendConstraint',
	'{9533BA5C-A32F-45DA-AE06-32EBE35E8CFF}' : 'BendConstraintProxy',
	'{CA6A960F-9215-4EF3-AFFC-A90D277BEF4F}' : 'BendOptions',
	'{54E4411A-7349-4591-991E-9F930A01EB83}' : 'BendDefinition',
	'{BBC883B2-B5E1-44C9-A98F-E7221FC17F3D}' : 'BendFeature',
	'{E6885A36-3C1C-43A1-9206-81706779DA32}' : 'BendFeatureProxy',
	'{DAA25411-1CB8-4FE2-8F10-1E98740E0889}' : 'BendFeatures',
	'{D54EA6F2-9FB4-43A3-A0C6-C93AF9991E28}' : 'BendPartFeatureProxy',
	'{6B73769B-1859-4202-87D4-2E508FC9434C}' : 'BIMExchangeServer',
	'{C7EAA071-3EFA-4D2F-87BD-C41ABA98C678}' : 'BossFeatureProxy',
	'{1F878EE1-06B7-4C7F-9339-920BEFCFE63D}' : 'RibFeatureProxy',
	'{6F18AA5B-56B7-4880-90A5-190322278B8D}' : 'BoundaryPatchFeatureProxy',
	'{FE15F632-2312-46D7-86C9-5EEAAC85F7B3}' : 'CenteredWidthExtent',
	'{4286D377-DC30-4195-9A04-E2C5A29AA72A}' : 'CentroidWorkPointDef',
	'{0E1AE204-AD92-497C-A48C-979715C3A035}' : 'ChamferFeatureProxy',
	'{E6478D92-2EBD-4363-8C27-A6891E942DBB}' : 'CircularOccurrencePatternProxy',
	'{1CA68293-D200-42E3-B54E-FEB349B302D3}' : 'CircularPatternFeatureProxy',
	'{CAD5C3C6-C42C-4F1A-A6E2-5D8746198027}' : 'ClientApplication',
	'{EF375552-9B4F-4384-9775-4D4EE910DA33}' : 'ClientFeatureProxy',
	'{BDC1CFE2-865D-46A5-83C9-8FDAD55EA7F0}' : 'ClientFeatureElementProxy',
	'{ECD82FDD-5B8F-4515-B3CE-1ED92B94C11F}' : 'CoilFeatureProxy',
	'{C7A68C71-14FA-11D6-8E01-0010B541CAA8}' : 'CoincidentConstraintProxy',
	'{BFA33A07-C4CE-4CAD-89BC-AF2C49FD5029}' : 'CoincidentConstraint3DProxy',
	'{C7A68CD1-14FA-11D6-8E01-0010B541CAA8}' : 'CollinearConstraintProxy',
	'{4FDD2BD0-33C6-4EB0-90CE-4EEA2B181738}' : 'CollinearConstraint3DProxy',
	'{665564D4-83B4-4B86-A365-CAA6B0EBA6C2}' : 'CombineFeatureProxy',
	'{E538F3DF-5386-4537-ABDB-82C476C4274D}' : 'CommandBarButton',
	'{32429DA6-B712-4638-8C53-B1EEE7C1D18B}' : 'CommandBarPopUp',
	'{AE0AA5DD-80A7-4094-B58C-06304422CE34}' : 'CompositeiMateDefinitionProxy',
	'{C7A68CD3-14FA-11D6-8E01-0010B541CAA8}' : 'ConcentricConstraintProxy',
	'{EF118F14-C2D2-4DF4-910A-3438FBEC2817}' : 'ConcentricConstraint3D',
	'{6B64AAF5-85DF-4FB5-ACAB-717DBBEE7DA4}' : 'ConcentricConstraint3DProxy',
	'{8D389B94-12D9-4150-BC67-B64B560E743F}' : 'ContourFlangeDefinition',
	'{37076B79-AB7A-4E6B-8E9D-8D68D28C272E}' : 'CornerOptions',
	'{2390C0D0-A03F-4526-B4B1-7FBFC3C9A66E}' : 'ContourFlangeFeature',
	'{7DBA9100-AFA9-407A-A91C-A9CC7A079565}' : 'CornerFeature',
	'{F69024F9-970E-4223-82DD-6B4F0E3AF57F}' : 'CornerDefinition',
	'{159DE5F6-0CF1-48F6-87AA-2865091762D3}' : 'ContourFlangeFeatureProxy',
	'{A7AF22DD-A689-4BEA-84BF-AEE3496BB26E}' : 'ContourFlangeFeatures',
	'{1492BD29-4122-41C8-AA02-B871BC06CCA1}' : 'ContourRollFeature',
	'{206F590B-1854-41A8-9ACE-CB18BCF1154B}' : 'ContourRollFeatureProxy',
	'{762B1B03-F049-467E-8BFC-DB28CF0DAD27}' : 'ContourRollFeatures',
	'{71360893-BD99-4D41-96CD-A3BD2AE0DB4D}' : 'CoreCavityFeatureProxy',
	'{DDD17D41-9A17-4ADD-BDB2-E2701A524903}' : 'CornerChamferFeatureProxy',
	'{64868FC5-AFD9-4602-A5D5-02D93B65BB05}' : 'CornerFeatureProxy',
	'{63F4004E-C9FE-4B75-A7CB-F526543A5C29}' : 'CornerFeatures',
	'{F8B2175E-285B-4787-B12A-6E485CA1885B}' : 'CornerRoundFeatureProxy',
	'{7958ED54-7E29-490B-9963-BF61E39E98E0}' : 'CosmeticBendFeatureProxy',
	'{FFC0E573-23C5-4DB1-A1DC-F6B12EA2907B}' : 'Weld',
	'{D857DD50-A568-4AA5-BB97-DA1B5C460F63}' : 'CosmeticWeldDefinition',
	'{7338F36B-6CD8-4296-90AE-EFEAC0FED72B}' : 'CosmeticWeld',
	'{4A2D7396-8300-4424-B9B7-EB9A8CA5D89E}' : 'CosmeticWelds',
	'{FFFA6714-4FA1-4191-B746-8F0493DF7C06}' : 'CurveAndEntityWorkPointDef',
	'{5E600148-DA27-47DD-8286-E38CC9466B2F}' : 'CustomConstraintProxy',
	'{5E46D694-BC48-4071-9B6A-8A7F6DDBB685}' : 'CustomConstraint3DProxy',
	'{061C46D9-4A71-40EB-9DDC-4D425A6ABE3E}' : 'CutAcrossBendsExtent',
	'{58370C0B-5F01-422A-AA66-DC7FD8AAC4CD}' : 'CutFeatureProxy',
	'{3BE697C4-0242-46F3-A420-27E86761D1D7}' : 'DecalFeatureProxy',
	'{FA1ACA84-839B-4F18-97FA-5AA81875B0EB}' : 'DeleteFaceFeatureProxy',
	'{51182028-01DC-4629-AD22-8BFF0D74FA1A}' : 'DerivedAliasComponentProxy',
	'{D2E7C9A2-CB9A-4619-B0AA-B7BA2870CDEE}' : 'DerivedAssemblyComponentProxy',
	'{6D54C427-62E1-4EB9-A4DC-DA926F059819}' : 'ShrinkwrapComponentProxy',
	'{1B986C9A-B329-45B0-B682-95F04FF16E87}' : 'DerivedPartComponentProxy',
	'{C7A68CFB-14FA-11D6-8E01-0010B541CAA8}' : 'DiameterDimConstraintProxy',
	'{080ECFB1-9C78-4A73-8FC9-7A438D08B3A6}' : 'DirectionAndDistanceMoveDefinition',
	'{8F25CE45-DF1F-4669-BAA8-E2042ED68811}' : 'DistanceAndAngleChamferDef',
	'{E17AC68F-D333-4DF4-BBAD-BDD9B8377C9C}' : 'DistanceChamferDef',
	'{A7D32953-D38C-4EB4-B9D0-79F7275B37C1}' : 'DistanceExtent',
	'{335DE8A2-438A-4B8C-B331-18107E0E328F}' : 'DistanceFromFaceExtent',
	'{3C49109C-CDDD-4D4F-A4F3-A0CA3E9EF7F2}' : 'DistanceHeightExtent',
	'{296442E1-7AB3-46B9-8494-7FBB585F6B50}' : '_VbaImplementationDrawingEvents',
	'{BBF9FDF1-52DC-11D0-8C04-0800090BE8EC}' : '_DrawingDocument',
	'{55C72DAA-3307-43D6-89F0-CBF7DD348E4D}' : 'DrawingPrintManager',
	'{457D2D49-6354-461E-AE0F-2C42B371D313}' : 'DSServer',
	'{E59EEDF7-48F4-4328-AF62-EBBE19BD09C1}' : 'EdgeWidthExtent',
	'{C7A68CFF-14FA-11D6-8E01-0010B541CAA8}' : 'EllipseRadiusDimConstraintProxy',
	'{152C858E-87FE-45AD-867B-80622EF4B8AC}' : 'EmbossFeatureProxy',
	'{A89E388A-13C9-4FFA-B777-9C0E1C81F136}' : 'EndOfFeatures',
	'{C7A68CD9-14FA-11D6-8E01-0010B541CAA8}' : 'EqualLengthConstraintProxy',
	'{C7A68CDB-14FA-11D6-8E01-0010B541CAA8}' : 'EqualRadiusConstraintProxy',
	'{039A89FA-EBE5-4D7D-AC2F-46A67FE7D824}' : 'EqualConstraint3DProxy',
	'{F057A860-3896-4C4A-87CB-E634F9BA681B}' : 'ExtendFeatureProxy',
	'{C75F478E-81C5-4E92-BC2A-630E598E34E5}' : 'ExtrudeFeatureProxy',
	'{5874F2D8-29C2-4D48-91C2-BB239564CF26}' : 'FaceDraftFeatureProxy',
	'{67BD386A-CC79-48F0-BCFF-6C25FFBF59AA}' : 'FaceFeatureDefinition',
	'{600E3CEE-1600-4999-ACE4-7CED6483BECE}' : 'FaceFeature',
	'{6DEF95B4-C5EF-4FBA-AEE9-B9486F648CAB}' : 'FaceFeatureProxy',
	'{C0D71AC3-E085-4A0E-85FF-549C000BA1E7}' : 'FaceFeatures',
	'{B134AF6F-7FE5-4485-B5E8-493541D94E3F}' : 'FeatureBasedOccurrencePatternProxy',
	'{57184DE5-2055-47CD-BC40-0277AD066D70}' : 'FeatureDimensionProxy',
	'{B4298554-2144-4054-A4EA-81888D6F6997}' : 'FeaturePatternElementProxy',
	'{4F16A71E-1337-40DE-B13F-DB996F9A716E}' : 'FilletFeatureProxy',
	'{28DD48C5-8D70-11D4-8DDE-0010B541CAA8}' : 'FixedWorkAxisDef',
	'{2C16786F-83FF-11D4-8DDB-0010B541CAA8}' : 'FixedWorkPlaneDef',
	'{28DD48D5-8D70-11D4-8DDE-0010B541CAA8}' : 'FixedWorkPointDef',
	'{5475DDC1-3397-46D6-A7A3-E1C34FA5BD7E}' : 'FlangeFeature',
	'{3978BB7A-4A07-475B-BD57-13A05A343EDB}' : 'FlangeDefinition',
	'{494427B8-E911-4706-9814-35980AC5621D}' : 'FlangeFeatureProxy',
	'{F9B17D1C-6918-44FE-B072-7B4F00CD2BB3}' : 'FlangeFeatures',
	'{F1904548-5E12-4B16-B798-8177BD9F7F38}' : 'FlatPatternSettings',
	'{F36456A4-780C-4CA6-B420-5DBEFFBBCA7D}' : 'FlushConstraintProxy',
	'{2A87493C-AFCD-42D8-A4AE-8385513E63E9}' : 'FlushiMateDefinitionProxy',
	'{4594DFB7-06DB-4707-9F10-B42F740EE37D}' : 'FoldFeature',
	'{0AE09AED-1DFB-41D3-B640-E0E9A24FA8C0}' : 'FoldDefinition',
	'{10FCE1AE-95AF-49F4-99FD-B391C181212F}' : 'FoldFeatureProxy',
	'{2B564484-AF79-47BF-836B-15F288717791}' : 'FoldFeatures',
	'{FA24DA04-D875-4E23-AD4E-312F5B7EC61A}' : 'FreeformFeatureProxy',
	'{C7FD7CEA-3C30-4BCF-A6E4-A458D3A0F728}' : 'DirectEditFeatureProxy',
	'{8A4D2830-7D4A-49E5-99BC-3E6C760463E7}' : 'DirectEditOperationProxy',
	'{F6A6A22F-70E4-418E-BC65-F39947C6D1E7}' : 'DirectEditMoveOperation',
	'{3B833858-7410-47C9-BCAD-F3BE5DEA191D}' : 'DirectEditMoveOperationProxy',
	'{047BD59F-24A4-40D2-A47E-6FED9726BA88}' : 'DirectEditSizeOperation',
	'{3181BFE4-BAD1-4C7A-9107-114093E4238A}' : 'DirectEditSizeOperationProxy',
	'{3913A482-D11A-4B13-A6B1-C1310F935B09}' : 'DirectEditRotateOperation',
	'{264513E0-16F5-4AE8-A80D-46EE06D2C99B}' : 'DirectEditRotateOperationProxy',
	'{A7E03766-451A-4BFB-B4CF-FE7F1F258494}' : 'DirectEditDeleteOperation',
	'{EAFC6907-44B0-482F-A30F-A46E227A57BC}' : 'DirectEditDeleteOperationProxy',
	'{D3067CC6-4526-4797-B62D-54AF0E415A47}' : 'DirectEditScaleOperation',
	'{BC329A16-2294-4C2D-AEAC-AE61F5433C7B}' : 'DirectEditScaleOperationProxy',
	'{D26E4888-3FA1-4A45-94E5-AA1A3A41B4AE}' : 'FreeMoveDefinition',
	'{95852FC2-F171-47D3-9435-A478AFF2353E}' : 'FromToExtent',
	'{78E9A7D5-C2AD-48C2-85D5-3A0A58D2FDA5}' : 'FromToWidthExtent',
	'{9A6F5F04-E0DD-463B-96C3-117B88E7BE25}' : 'FullSweepExtent',
	'{9C88D3A8-C3EB-11D3-B79E-0060B0F159EF}' : 'GeneralPreferences',
	'{92353969-0350-11D3-B787-0060B0F159EF}' : 'GraphicsPreferences',
	'{E19AC563-EC57-4E4A-9FE3-35AEB2C6B59A}' : 'GrillFeatureProxy',
	'{C7A68CDD-14FA-11D6-8E01-0010B541CAA8}' : 'GroundConstraintProxy',
	'{F870DE76-265A-4AD2-BACB-5E0137EF0B3A}' : 'GroundConstraint3DProxy',
	'{33E293A8-9DD6-4B9A-8274-E436A3BB3876}' : 'HelicalConstraint3D',
	'{5DE610F3-F512-4973-B78A-F50669560B4B}' : 'HelicalConstraint3DProxy',
	'{532E5229-0B80-4B9B-968F-69BC150C59CC}' : 'HemDefinition',
	'{D9AB7AE5-6A67-4165-9E0B-0F008C9135B0}' : 'HemFeature',
	'{0F6DEA5E-48E4-49BE-854E-164A89406DDC}' : 'HemFeatureProxy',
	'{DF566DD8-E3A3-45E3-844D-78F8C072ECDC}' : 'HemFeatures',
	'{BB5A14E9-4213-4965-9B76-F9B33C807FB3}' : 'SingleHemDefinition',
	'{4F1B00F2-FA18-46EA-9C2F-97574189230D}' : 'TeardropHemDefinition',
	'{F899D5C4-5961-43ED-A66C-E44A186C1B67}' : 'RolledHemDefinition',
	'{C534F040-9826-411E-8C6F-4A73C3A998FC}' : 'DoubleHemDefinition',
	'{AD86A222-E8A0-4754-A764-65A958389DF5}' : 'HoleFeatureProxy',
	'{C7A68CE1-14FA-11D6-8E01-0010B541CAA8}' : 'HorizontalAlignConstraintProxy',
	'{C7A68CDF-14FA-11D6-8E01-0010B541CAA8}' : 'HorizontalConstraintProxy',
	'{3D65F35E-2F1A-469E-9E5D-E02437A6E3BA}' : 'ReferenceFeatureProxy',
	'{736ED1B9-7434-4044-B439-EEC1AA84CAAE}' : 'iFeatureProxy',
	'{84526202-5E30-403F-8700-397646B4BBD0}' : 'iFeatureEntityInput',
	'{95B2DD02-374C-41C5-998C-7FCF8BDCA452}' : 'iFeatureParameterInput',
	'{77244784-A1C1-429E-A61F-E6E480B8DFEF}' : 'iFeatureSketchPlaneInput',
	'{F302D8D2-7DF4-4AD2-9933-9037EB507A90}' : 'iFeatureVectorInput',
	'{F21B5BBF-DBA8-480A-95A6-83D27D52343B}' : 'iFeatureWorkPlaneInput',
	'{5EA2744B-95DB-4104-B06A-E9BB6712D59E}' : 'iMateResultProxy',
	'{FC6CACA3-208B-40AD-8B3A-0949B6CBBD3A}' : 'ImportedModelEntities',
	'{3F35DB6C-C158-4203-B420-AE4ABCC4B908}' : 'ImportedModelEntity',
	'{AEFCDC34-A275-44DF-8A40-DF4B0BFD215F}' : 'ImportedDWGComponentDefinition',
	'{1EC4F1F9-A5A3-4F48-A4D7-071C588F9C8A}' : 'ImportedDWGLayer',
	'{711D0964-C6EF-4105-B02F-A5D6B14DA971}' : 'ImportedDWGLayersEnumerator',
	'{D2653F5F-C73A-4FAE-9172-EA1B60098B07}' : 'ImportedGenericComponent',
	'{B3D5D60A-6CE4-4F7B-A6A6-88A15E433F95}' : 'ImportedGenericComponentProxy',
	'{53196161-A966-4EE7-9080-3F75C7D5876D}' : 'ImportedGenericComponentDefinition',
	'{35C3BC01-5C75-4BDF-B92E-97205EE57219}' : 'InsertConstraintProxy',
	'{1DC001D8-CAAE-4132-A265-4E17E74A9410}' : 'InsertiMateDefinitionProxy',
	'{D2CF1030-CA32-48F6-8865-298BE7E11CCC}' : 'IntersectionCurveProxy',
	'{5ABB74D4-90C9-490E-A58F-A2FE0986AFBC}' : 'OutOfProcessInventorServerObject',
	'{D4F6BE55-A3E1-4420-BCBB-9E2E98A87226}' : 'OutOfProcessInventorServer',
	'{091BB62A-D3D9-4DBE-B8DA-69D51538AC92}' : 'KnitFeatureProxy',
	'{81807A32-C016-4239-8D61-28B44957393D}' : 'LayoutConstraintProxy',
	'{31B7388A-3B81-4568-B697-9C1F0D09E7AC}' : 'LegacyDistanceHeightExtent',
	'{28DD48CF-8D70-11D4-8DDE-0010B541CAA8}' : 'LineAndFaceWorkPointDef',
	'{28DD48C3-8D70-11D4-8DDE-0010B541CAA8}' : 'LineAndPlaneWorkAxisDef',
	'{18A18CCA-283E-4E06-9358-1949A91CECF1}' : 'LineAndPointWorkAxisDef',
	'{46785C43-7F4A-11D4-8DDB-0010B541CAA8}' : 'LineAndPointWorkPlaneDef',
	'{2C167869-83FF-11D4-8DDB-0010B541CAA8}' : 'LineAndTangentWorkPlaneDef',
	'{2F041963-4B68-415F-BE07-F1FB6C6342A3}' : 'LineLengthDimConstraint3DProxy',
	'{46785C45-7F4A-11D4-8DDB-0010B541CAA8}' : 'LinePlaneAndAngleWorkPlaneDef',
	'{28DD48B9-8D70-11D4-8DDE-0010B541CAA8}' : 'LineWorkAxisDef',
	'{8742661B-564A-4CE3-A32C-6F08894FB760}' : 'LipFeatureProxy',
	'{C16DE191-DEEC-449E-BEF1-1F1220233FB3}' : 'LoftedFlangeDefinition',
	'{A7EA6C3E-D3A4-48BB-B600-E8D1097B9A55}' : 'LoftedFlangeFeature',
	'{87DB004A-F974-4BFE-A8BD-65BA290F2D43}' : 'LoftedFlangeFeatureProxy',
	'{C14E0C19-443E-41D2-95B5-B46AB974CF0D}' : 'LoftedFlangeFeatures',
	'{D3CB21DB-DF14-45FC-ADD6-8E8EED0AECC3}' : 'LoftFeatureProxy',
	'{CF3DEE6F-DBB2-4393-A409-5D0ADC6CB12C}' : 'Machining',
	'{531B0D86-9BDA-4992-8D31-C42A8788000B}' : 'MateConstraintProxy',
	'{619B5213-A92D-4D4B-BE3F-6CA4B1715A78}' : 'MateiMateDefinitionProxy',
	'{C7A68CE3-14FA-11D6-8E01-0010B541CAA8}' : 'MidpointConstraintProxy',
	'{2B2BEA0C-F141-4B3E-B061-1B2C8C6B5D9F}' : 'MidpointConstraint3DProxy',
	'{28DD48D3-8D70-11D4-8DDE-0010B541CAA8}' : 'MidPointWorkPointDef',
	'{3F96EC38-31B5-46BD-B45D-CA049B450786}' : 'MidSurfaceFeatureProxy',
	'{0AD283F9-4020-423B-9C18-A192FEBFA285}' : 'MirrorFeatureProxy',
	'{6BD96D54-7EE0-4E2C-B851-95FA6A9C5236}' : 'ModelCompositeAnnotationProxy',
	'{B879F99D-E87D-4F95-AD7C-8B6EB246C872}' : 'ModelDatumIdentifierProxy',
	'{8B7BBAEA-6709-47A4-9C19-946C8D3D21C0}' : 'ModelDatumReferenceFrameProxy',
	'{E2784ADF-29DA-48AF-BF30-A04DA9B33FF4}' : 'ModelFeatureControlFrameProxy',
	'{0F2F8695-4E4D-465C-B51B-D347C9352AAA}' : 'ModelGeneralNoteProxy',
	'{4F8CBF41-F056-4F52-862E-4AF730389EE2}' : 'ModelHoleThreadNoteProxy',
	'{95B50D6B-D5AC-4331-8957-ADE73D47785A}' : 'ModelLeaderNoteProxy',
	'{EE7ED037-D09F-4FC4-BB55-9D7DBB5C52E6}' : 'ModelSurfaceTextureSymbolProxy',
	'{B0EBE9C5-14C6-4952-A839-B873883547DA}' : 'ModelToleranceFeatureProxy',
	'{F5CB0108-0E0A-416F-AE41-83FAE56D3D10}' : 'MoveFaceFeatureProxy',
	'{70FCCBEE-EF8F-4917-98E0-B26399EAB6CE}' : 'MoveFeatureProxy',
	'{25188AF6-308D-4181-879A-1B1084288928}' : 'NonLinearEdgeWorkPointDef',
	'{0E7B7C43-1EA3-4FA9-95ED-5A1370E81E3F}' : 'NonParametricBaseFeatureProxy',
	'{EEEC1AAC-5A0C-4405-B0A7-63EBCF82A3A3}' : 'NormalToCurveWorkPlaneDef',
	'{B25B8DC2-B557-4E6B-81D2-A7D0C2A992F4}' : 'NormalToSurfaceWorkAxisDef',
	'{8006A07C-ECC4-11D4-8DE9-0010B541CAA8}' : 'OffsetConstraint',
	'{C7A68CD7-14FA-11D6-8E01-0010B541CAA8}' : 'OffsetConstraintProxy',
	'{C7A68CF3-14FA-11D6-8E01-0010B541CAA8}' : 'OffsetDimConstraintProxy',
	'{B8E1A8FF-EE38-49CD-BC33-FBA4E8E6073C}' : 'OffsetSplineDimConstraintProxy',
	'{2EF323DC-CEC7-4E75-9C92-E7571F6653C3}' : 'OffsetWidthExtent',
	'{24339BC2-0B85-4B40-A1DA-1B3473A11B62}' : 'OnFaceConstraint3DProxy',
	'{F5C1C3DB-EE51-4B1A-B754-BA0D82974A31}' : 'OnFaceCurveProxy',
	'{C7A68CE5-14FA-11D6-8E01-0010B541CAA8}' : 'ParallelConstraintProxy',
	'{3163F506-342D-4D68-8AB1-39C306DCA6F6}' : 'ParallelConstraint3DProxy',
	'{071F1650-979B-4FFC-9027-D6E15E251C99}' : 'ParallelToXAxisConstraint3DProxy',
	'{01076B1B-C497-401C-B096-23D432B35BF8}' : 'ParallelToYAxisConstraint3DProxy',
	'{54759E01-984F-4540-8D3F-82EB1EA6BDD6}' : 'ParallelToZAxisConstraint3DProxy',
	'{5224F310-1B50-480C-BDB7-DFF90F6068D9}' : 'ParallelToXYPlaneConstraint3DProxy',
	'{78671AF0-CC9B-4046-B21E-2FC5F075769F}' : 'ParallelToYZPlaneConstraint3DProxy',
	'{205C7990-C5B5-4FE2-BE5C-D5CAC441BF9C}' : 'ParallelToXZPlaneConstraint3DProxy',
	'{DA33F1A3-7C3F-11D3-B794-0060B0F159EF}' : 'PartComponentDefinition',
	'{575F2830-2B6A-11D4-B7A8-0060B0F159EF}' : 'PartComponentDefinitions',
	'{1D23FF98-1FB3-434F-847F-452217821819}' : 'Sketch3DSettings',
	'{4B98058A-A232-47FD-9186-1070297036FB}' : '_VbaImplementationPartEvents',
	'{29F0D463-C114-11D2-B77F-0060B0F159EF}' : 'PartDocument',
	'{4D29B490-49B2-11D0-93C3-7E0706000000}' : '_PartDocument',
	'{75445952-FFF4-405D-B057-E2EFD1B882BC}' : 'PathProxy',
	'{BF000E43-1F0C-464A-A9F3-E1C5EEBA433E}' : 'PathAndGuideRailSweepDef',
	'{7D7EAE29-869F-48FB-AD5E-797AB5B87F65}' : 'PathAndGuideSurfaceSweepDef',
	'{F369E470-65BE-4BB7-B3E8-AB32C9F6CC22}' : 'PathAndSectionTwistsSweepDef',
	'{A19C2D06-4C43-41EC-93EB-AD104ABEE1B9}' : 'PathEntityProxy',
	'{B7FE7553-8DF0-4F70-9798-C85438D3109E}' : 'PathSweepDef',
	'{C173A073-012F-11D5-8DEA-0010B541CAA8}' : 'PatternConstraint',
	'{C7A68CF1-14FA-11D6-8E01-0010B541CAA8}' : 'PatternConstraintProxy',
	'{C7A68CE7-14FA-11D6-8E01-0010B541CAA8}' : 'PerpendicularConstraintProxy',
	'{E2CF70B0-55E2-49E6-81AC-41FD6A6C3DB2}' : 'PerpendicularConstraint3DProxy',
	'{7F1F13A7-39BD-4720-AB79-E17BC3922427}' : 'PitchAndHeightCoilExtent',
	'{83B2573C-3DBB-44C1-B88D-2D12EF0A9EE2}' : 'PitchAndRevolutionCoilExtent',
	'{501F1ACA-00D4-47CF-A0D1-1F4D1BB1A633}' : 'PlanarMoveDefinition',
	'{C7A68CBB-14FA-11D6-8E01-0010B541CAA8}' : 'PlanarSketchProxy',
	'{2C167867-83FF-11D4-8DDB-0010B541CAA8}' : 'PlaneAndOffsetWorkPlaneDef',
	'{46785C4B-7F4A-11D4-8DDB-0010B541CAA8}' : 'PlaneAndPointWorkPlaneDef',
	'{2C16786B-83FF-11D4-8DDB-0010B541CAA8}' : 'PlaneAndTangentWorkPlaneDef',
	'{246ADF11-4A5F-43AF-ADDE-440B0532ED2F}' : 'PointAndPlaneDistanceDimConstraint3DProxy',
	'{28DD48C1-8D70-11D4-8DDE-0010B541CAA8}' : 'PointAndPlaneWorkAxisDef',
	'{66E2ABF7-3454-41E6-9115-62879698C194}' : 'PointAndTangentWorkPlaneDef',
	'{453A1005-42C9-469C-847E-CEA7D550751B}' : 'RipDefinition',
	'{38D353FC-D30E-4B08-B73A-785787D4D7AD}' : 'RipFeature',
	'{2E264D50-AF7C-4FDE-96DA-12EBD46CAB9B}' : 'PointToPointRipTypeDef',
	'{28DD48D1-8D70-11D4-8DDE-0010B541CAA8}' : 'PointWorkPointDef',
	'{1691F301-F2AF-48F4-946F-185CEF9A7EEE}' : 'Preparations',
	'{33DE76BF-3E58-4EF2-AE90-AA540F2A6C52}' : '_VbaImplementationPresentationEvents',
	'{76283A80-50DD-11D3-A7E3-00C04F79D7BC}' : '_PresentationDocument',
	'{C7A68CCB-14FA-11D6-8E01-0010B541CAA8}' : 'ProfileProxy',
	'{75120650-FD69-4DFD-A738-9E5E34F5934B}' : 'Profile3DProxy',
	'{C7A68CCF-14FA-11D6-8E01-0010B541CAA8}' : 'ProfileEntityProxy',
	'{BD923BF8-C5DD-4AE4-B577-0988B48FA89D}' : 'ProfileEntity3DProxy',
	'{C7A68CCD-14FA-11D6-8E01-0010B541CAA8}' : 'ProfilePathProxy',
	'{EA49DCCB-E7AE-4B7D-BEAC-80F835167854}' : 'ProfilePath3DProxy',
	'{1F3DB03A-352E-44EA-807B-8D3C4FCF855C}' : 'ProjectedCutProxy',
	'{B716CEF3-32C9-4A9A-911D-0D1CF52A74C9}' : 'PunchToolFeatureProxy',
	'{C7A68CFD-14FA-11D6-8E01-0010B541CAA8}' : 'RadiusDimConstraintProxy',
	'{F0780498-03E3-471D-A733-92EFAC4FF0EE}' : 'ArcLengthDimConstraintProxy',
	'{8DD13222-E35F-4EEA-93BA-87F73A069481}' : 'RadiusDimConstraint3DProxy',
	'{17FD3E5D-FF18-4E1C-AE86-C9A5A295B2BE}' : 'RectangularOccurrencePatternProxy',
	'{2A705B9C-82D0-4F14-9137-164642028E77}' : 'RectangularPatternFeatureProxy',
	'{6FF869B7-4D60-4A01-9CCA-9F5F71433014}' : 'RefoldFeature',
	'{325DB945-8B2D-4574-A023-A2864A85896A}' : 'RefoldFeatureProxy',
	'{AD87B241-B3FD-475C-B369-AD3C5D3E3E0D}' : 'RefoldFeatures',
	'{63FB8F95-6B59-4039-B9E1-F6D74E1B3716}' : 'ReplaceFaceFeatureProxy',
	'{1B63BB78-7EC2-4D21-A312-A867DCF54110}' : 'RestFeatureProxy',
	'{F0541886-3BF7-4E4D-8A11-D113578E5110}' : 'RevolutionAndHeightCoilExtent',
	'{28DD48BF-8D70-11D4-8DDE-0010B541CAA8}' : 'RevolvedFaceWorkAxisDef',
	'{FD16E33C-AE0F-4CB3-8E44-9C6F2A9A8FF6}' : 'RevolveFeatureProxy',
	'{A77799B5-136D-4FEB-9902-CAEC8E122A24}' : 'RipFeatureProxy',
	'{8A0202C7-6ADF-454C-AF47-09E3027E8E7C}' : 'RipFeatures',
	'{1753D82F-BEAA-4770-82B9-78FFBF2BEC3D}' : 'RotateRotateConstraintProxy',
	'{D9E903E5-29EE-4164-8701-2CB853CFEE99}' : 'RotateRotateiMateDefinitionProxy',
	'{9DFB56E1-F6A4-4D2A-99CE-47CBB8A3145D}' : 'RotateTranslateConstraintProxy',
	'{0BD0BDD4-2716-42A0-B258-09F689CFDFB5}' : 'RotateTranslateiMateDefinitionProxy',
	'{3F51C434-F75E-487F-93A2-5D1438AD5D41}' : 'RuleFilletFeatureProxy',
	'{1CEE32D6-4997-4E37-ADBB-9AE5873BF30D}' : 'RuledSurfaceFeatureProxy',
	'{78F10980-2892-46CD-8F0E-B709A4835B9B}' : 'SculptFeatureProxy',
	'{8C80204E-CFE9-43C8-BFAE-4D022F3E2339}' : 'UnfoldFeatures',
	'{B03877E4-31F6-4B1E-8F38-FCCFD0B0DCAA}' : 'UnfoldFeature',
	'{41ADE507-16D9-4103-BD0C-FA1C196B9DAA}' : 'SheetMetalFeatures',
	'{EE0E6545-A868-4A60-A152-2AF4C5FB44DC}' : 'ShellFeatureProxy',
	'{49F63CD1-212B-4BCB-B43C-5CAF969A2EAC}' : 'SilhouetteCurveProxy',
	'{E8320E6D-E219-4F7C-954C-484A94137FD1}' : 'SinglePointRipTypeDef',
	'{FA39B171-CAA5-4FB2-94D0-4E0DF357D13E}' : 'Sketch3DProxy',
	'{C7A68CC1-14FA-11D6-8E01-0010B541CAA8}' : 'SketchArcProxy',
	'{856FF591-895A-4A94-9FB1-16F5265C91C8}' : 'SketchArc3DProxy',
	'{36B9F8B4-FD23-4AC9-A41F-4778F124C0B7}' : 'SketchBlockProxy',
	'{83C558ED-EC43-41A6-8FCB-36461DF6319B}' : 'SketchBlockDefinitionProxy',
	'{C7A68CC9-14FA-11D6-8E01-0010B541CAA8}' : 'SketchCircleProxy',
	'{D4B12468-31B2-4885-BE17-B55DE2D561AF}' : 'SketchCircle3DProxy',
	'{E3757DA9-1C29-477B-838A-B84E896410B2}' : 'SketchControlPointSplineProxy',
	'{7D3BDDB1-82EF-4AF6-80C2-96BED3462559}' : 'SketchControlPointSpline3DProxy',
	'{31F0000E-C045-438F-8630-24EC11C60ABC}' : 'SketchDrivenPatternFeatureProxy',
	'{C7A68CC5-14FA-11D6-8E01-0010B541CAA8}' : 'SketchEllipseProxy',
	'{A50E48BD-8D0E-4C9A-B3C7-D6EC114ACB3D}' : 'SketchEllipse3DProxy',
	'{C7A68CC7-14FA-11D6-8E01-0010B541CAA8}' : 'SketchEllipticalArcProxy',
	'{DD3E1C70-8EDA-466B-B455-5CCE10BBA910}' : 'SketchEllipticalArc3DProxy',
	'{70180CA4-8BB6-4D2A-B750-E7A17EF35B99}' : 'SketchEquationCurveProxy',
	'{72DDFCC0-DEBA-46D6-AA95-3B4B91E957F6}' : 'SketchEquationCurve3DProxy',
	'{C5195DC5-0D96-45C2-8E51-BE1A305AC086}' : 'SketchFixedSplineProxy',
	'{DBABE302-0C4A-4F2D-B67B-768F87C54E32}' : 'SketchFixedSpline3DProxy',
	'{0FCBB605-3830-4C3F-95F6-76A4CB15F659}' : 'SketchImageProxy',
	'{C7A68CBD-14FA-11D6-8E01-0010B541CAA8}' : 'SketchLineProxy',
	'{BD020927-670F-4F30-943B-75A2EC87E052}' : 'SketchLine3DProxy',
	'{BF18368A-A9B1-4295-9242-18D1AC91F8D3}' : 'SketchOffsetSplineProxy',
	'{C7A68CBF-14FA-11D6-8E01-0010B541CAA8}' : 'SketchPointProxy',
	'{9AA5A91E-286C-4F3E-A93D-863BAFD4B80C}' : 'SketchPoint3DProxy',
	'{C7A68CC3-14FA-11D6-8E01-0010B541CAA8}' : 'SketchSplineProxy',
	'{933CA2AC-EC02-4BA1-9B5B-AFDEDFF20CBF}' : 'SketchSpline3DProxy',
	'{37D2C08C-F2F6-4D4A-9A53-CEBC0A504DA1}' : 'SketchSplineHandleProxy',
	'{7C693E2E-D4D3-433A-A90F-112E3C52E543}' : 'SketchSplineHandle3DProxy',
	'{81D122D0-F88A-485C-BFEA-2968E2F3456D}' : 'HelicalCurveProxy',
	'{22324A8F-65DF-48BC-84CD-8A3B457B6A6E}' : 'SmoothConstraintProxy',
	'{748041B9-77F8-481D-BADA-8F03152C3AF1}' : 'SmoothConstraint3DProxy',
	'{B13C95CF-8B79-4F03-8EF0-BE81A400529F}' : 'SnapFitFeatureProxy',
	'{609506AD-969B-4FEA-9DA5-D2FC535472FA}' : 'SphereCenterPointWorkPointDef',
	'{8D41F569-6407-4C82-A25E-762F6F8AA4B9}' : 'SpiralCoilExtent',
	'{8006A07A-ECC4-11D4-8DE9-0010B541CAA8}' : 'SplineFitPointConstraint',
	'{C7A68CD5-14FA-11D6-8E01-0010B541CAA8}' : 'SplineFitPointConstraintProxy',
	'{641D6ED0-4DF1-4FA3-B04D-86107C00A62B}' : 'SplineFitPointsConstraint3D',
	'{A5F4CA62-8A29-408E-AC56-0B95E44CE781}' : 'SplineFitPointsConstraint3DProxy',
	'{A2D2EF5E-37D0-4B0A-8227-F31A60090C8E}' : 'SplineLengthDimConstraint3DProxy',
	'{38C1B59A-0C1B-4076-A22C-291C34157BBD}' : 'SplitFeatureProxy',
	'{47B53154-8132-47E5-8733-9D9B4268F21C}' : 'SurfaceTextureANSIDefinition',
	'{201C8CF3-0801-49F5-B87E-F39CEA7508D7}' : 'SurfaceTextureBSIDefinition',
	'{90D115A7-34B8-4E35-9242-8B3FAB10CAB5}' : 'SurfaceTextureDINDefinition',
	'{53A282CD-46BF-4A34-BE2D-1CB7FF469B34}' : 'SurfaceTextureGBDefinition',
	'{0B1630B9-41C0-4DCA-BCBC-2E9D0BA096FE}' : 'SurfaceTextureGOSTDefinition',
	'{587A7801-DF86-4DC8-BD20-ADA5FB1193C2}' : 'SurfaceTextureISODefinition',
	'{78B82408-F848-4E5B-A657-67059CC86235}' : 'SurfaceTextureJISDefinition',
	'{2A5668A8-5EA5-45AE-B3DB-A4C7BD2F7E9D}' : 'SweepFeatureProxy',
	'{C7A68CE9-14FA-11D6-8E01-0010B541CAA8}' : 'SymmetryConstraintProxy',
	'{25C0112A-8E78-45F9-A50F-3C4E14AB60E2}' : 'TangentConstraintProxy',
	'{F2BCCD2A-83E0-4528-A039-318A93C7ABBA}' : 'TangentConstraint3DProxy',
	'{C7A68D01-14FA-11D6-8E01-0010B541CAA8}' : 'TangentDistanceDimConstraintProxy',
	'{4FD9CE51-8E4D-4E4B-865F-FC4F0D5A0D5C}' : 'TangentiMateDefinitionProxy',
	'{C7A68CEB-14FA-11D6-8E01-0010B541CAA8}' : 'TangentSketchConstraintProxy',
	'{C18888BF-ACD9-481C-BE9C-F8921846BE2D}' : 'TextBoxProxy',
	'{037C3FDB-8A3C-443F-8CF6-993D3295335C}' : 'TextBoxConstraint',
	'{2F77E2FF-BAD3-43A4-9874-8A99E824E060}' : 'TextBoxConstraintProxy',
	'{92A50081-D0B7-428F-BFF0-B0D277C3AEB0}' : 'TextBoxDefinitionHandler',
	'{D07B4A7B-08EE-4CEA-BC85-525E882714BC}' : 'ThickenFeatureProxy',
	'{E139EE45-18F4-404E-972E-08C6008BD225}' : 'FaceOffsetFeatureProxy',
	'{DA05EA7F-D509-4D65-AA86-AB596110425C}' : 'ThreadFeatureProxy',
	'{28DD48CB-8D70-11D4-8DDE-0010B541CAA8}' : 'ThreePlanesWorkPointDef',
	'{C7A68CF9-14FA-11D6-8E01-0010B541CAA8}' : 'ThreePointAngleDimConstraintProxy',
	'{46785C3F-7F4A-11D4-8DDB-0010B541CAA8}' : 'ThreePointsWorkPlaneDef',
	'{AFEA608B-F136-4BD1-995B-333BCAFDED08}' : 'ThroughAllExtent',
	'{C73A295D-CB57-4B32-AA53-652422FACF65}' : 'ToExtent',
	'{2C292AFE-8044-4E68-AB51-56340FBF0231}' : 'ToHeightExtent',
	'{4E5273FA-20B0-41E3-BB29-03BB6C09B0FE}' : 'ToNextExtent',
	'{E205D028-CE6C-4BE5-AE33-AB6F9770D869}' : 'TorusCenterPointWorkPointDef',
	'{662FBA92-6903-4455-9395-207E48749986}' : 'TorusMidPlaneWorkPlaneDef',
	'{9E7FC002-194A-4CB7-9862-4A3308F586C8}' : 'TransitionalConstraintProxy',
	'{6D92FD04-C569-4F19-8A54-A83B1CBA7080}' : 'TranslateTranslateConstraint',
	'{FBC6B272-3033-4F57-8279-7D70F3FFD508}' : 'TranslateTranslateConstraintProxy',
	'{6ECCBC87-A50D-11D4-8DE4-0010B541CAA8}' : 'TranslatorAddIn',
	'{6ECCBC7F-A50D-11D4-8DE4-0010B541CAA8}' : 'TranslatorAddInServer',
	'{7BCA4B05-379A-4960-BE68-236689EDAEF1}' : 'TrimFeatureProxy',
	'{5B7A8CDA-6F27-4396-9E39-C21A67CA03D3}' : 'TwoDistancesChamferDef',
	'{C7A68CF7-14FA-11D6-8E01-0010B541CAA8}' : 'TwoLineAngleDimConstraintProxy',
	'{407A9D14-6E3A-4F39-9AD6-CDD8873B9FCB}' : 'TwoLineAngleDimConstraint3DProxy',
	'{46785C41-7F4A-11D4-8DDB-0010B541CAA8}' : 'TwoLinesWorkPlaneDef',
	'{28DD48CD-8D70-11D4-8DDE-0010B541CAA8}' : 'TwoLinesWorkPointDef',
	'{28DD48BB-8D70-11D4-8DDE-0010B541CAA8}' : 'TwoPlanesWorkAxisDef',
	'{C0E159EB-2FFE-483E-B4CE-585BEE76E710}' : 'TwoPlanesWorkPlaneDef',
	'{C7A68CF5-14FA-11D6-8E01-0010B541CAA8}' : 'TwoPointDistanceDimConstraintProxy',
	'{5B29EB3A-F2F2-4998-B713-03042554E46C}' : 'TwoPointDistanceDimConstraint3DProxy',
	'{28DD48BD-8D70-11D4-8DDE-0010B541CAA8}' : 'TwoPointsWorkAxisDef',
	'{550A5700-23FB-4E1F-98D6-5BD7D9701ACD}' : 'UnfoldFeatureProxy',
	'{5E480B67-C221-4DB3-B6CF-976A72FCD09B}' : 'UnwrapFeatureProxy',
	'{C7A68CEF-14FA-11D6-8E01-0010B541CAA8}' : 'VerticalAlignConstraintProxy',
	'{C7A68CED-14FA-11D6-8E01-0010B541CAA8}' : 'VerticalConstraintProxy',
	'{D4652AC1-D4B9-4D65-8C2B-942D74411B1C}' : 'VirtualComponentDefinition',
	'{D8DEC5C0-4E92-4D60-B107-6D5FBBA9923A}' : 'WeldBead',
	'{F44EE9AE-7D98-49C7-8634-700050114F38}' : 'WeldBeads',
	'{F3C8A2A2-E9DF-454D-8769-8544374BB882}' : 'Welds',
	'{268D663B-4B37-11D6-8E06-0010B541CAA8}' : 'WeldsComponentDefinition',
	'{9A750C49-0384-4CD8-B1D9-DAADD3E28657}' : 'WeldmentComponentDefinition',
	'{91578449-A1E5-4865-BF53-D297549308B0}' : 'WidthOffsetWidthExtent',
	'{3CBE8AA5-3D92-11D5-8DEE-0010B541CAA8}' : 'WorkAxisProxy',
	'{3CBE8A9F-3D92-11D5-8DEE-0010B541CAA8}' : 'WorkPlaneProxy',
	'{3CBE8AA7-3D92-11D5-8DEE-0010B541CAA8}' : 'WorkPointProxy',
	'{9A104FEF-2749-4112-AA6D-937CB4F44420}' : 'WorkSurfaceProxy',
	'{85577108-087D-4E36-994A-48CA4F1D2AB9}' : 'UserCoordinateSystemProxy',
	'{4EDC3AD5-669B-40A9-A3DC-3261C16F4642}' : 'PointCloudProxy',
	'{3485FEA9-8865-44EE-8F03-72F46DAB0634}' : 'PointCloudPoint',
	'{50325C62-766C-41C2-A97C-8951BD4D0E56}' : 'PointCloudPointProxy',
	'{6B3ECB2F-78BA-492E-9235-E68EA88F66E9}' : 'PointCloudPlane',
	'{E65DEA7B-63C6-4F6E-9FCE-8177FEE904F9}' : 'PointCloudPlaneProxy',
	'{50E1E017-584C-4C7D-8001-4CF9AEAB7E5E}' : 'DWGBlockDefinition',
	'{F5CC3DD7-BC15-476C-853B-3E63BA66A29B}' : 'DWGArcsEnumerator',
	'{6D0B30F0-4279-46EC-8D96-EDD140C3EC72}' : 'DWGArc',
	'{DF1920AB-6CC5-4C6A-AA29-F4D3B0A30BA6}' : 'ImportedDWGComponent',
	'{6B46D5EC-57DE-414D-8ACC-EF1E7C6C1AAF}' : 'DWGEntity',
	'{E2012607-EC0A-4F31-A888-E389AF5667E7}' : 'DWGBlockReferencesEnumerator',
	'{942BDD59-6622-4CF0-BAD6-4F4EAD7A4DCA}' : 'DWGBlockReference',
	'{E825D13E-DAE3-4CA1-A275-5C0A62A67E6B}' : 'DWGEllipticalArcsEnumerator',
	'{E9455662-85DE-499A-9965-81270D314D70}' : 'DWGEllipticalArc',
	'{5F9B0BEB-E30C-4750-A733-1FCFE4218750}' : 'DWGEntitiesEnumerator',
	'{C70B926C-2519-4760-B513-DB4FD170208A}' : 'DWGLinesEnumerator',
	'{18F5F2F4-26CB-49E9-A105-F83638FEFB3E}' : 'DWGLine',
	'{19B7AC3A-9E5C-424E-AE7D-33B805717AF5}' : 'DWGPointsEnumerator',
	'{CE96A92D-B3F9-4607-9E47-30722770F9AD}' : 'DWGPoint',
	'{E25D1002-8B00-4E7A-A6F3-DF7BDCC7A63A}' : 'DWGPolylinesEnumerator',
	'{249D0F99-CAD8-4B05-9A8C-AAF415CEA2DC}' : 'DWGPolyline',
	'{F813785A-FF19-40AC-B383-EC47CB8EBF15}' : 'DWGEntitySegmentsEnumerator',
	'{34F5AE9B-CDD6-49ED-B3AD-AEFB61DD9DC0}' : 'DWGEntitySegment',
	'{8C2B0FE6-3B3F-4897-BD44-806DA59E436A}' : 'DWGPolylines2DEnumerator',
	'{AD47616F-A657-4363-AB07-360A1A38AD44}' : 'DWGPolyline2D',
	'{7CC584DD-262F-45D6-A383-6705655F2435}' : 'DWGPolylines3DEnumerator',
	'{BC6242DB-ABCC-4605-8A0F-9A42F26F9D9C}' : 'DWGPolyline3D',
	'{0FEC3515-6F9A-4BFB-BD87-7070E60B0010}' : 'DWGSplinesEnumerator',
	'{A19EC228-CE1D-4B2D-BE30-584AF42A18AA}' : 'DWGSpline',
	'{AED943D3-0351-4161-8916-0E99234DA2F8}' : 'DWGACMStandardPartsEnumerator',
	'{9EF3521A-24B6-4CE5-8A36-543E8E6C4D4F}' : 'DWGACMStandardPart',
	'{EC661E99-6315-4974-99F8-7018045C351F}' : 'DWGAcadSupportedProxiesEnumerator',
	'{E1FDDE0A-AAFB-4069-8266-D6389559A1A3}' : 'DWGAcadSupportedProxy',
	'{B1EECF0D-991E-44FD-8244-61AB5E826B35}' : 'ImportedDWGComponentProxy',
	'{7A458570-4422-40E6-B40E-008C2183AF1C}' : 'DWGEntityProxy',
	'{93545775-90CE-4E69-B0A5-4E3F23C30677}' : 'DWGBlockReferenceProxy',
	'{518CD473-78CC-4B12-A831-AE93812A2774}' : 'DWGBlockDefinitionProxy',
	'{E5CFA472-5D23-4486-8D2C-A4D8D564C196}' : 'DWGArcProxy',
	'{5EE74326-54FB-4C26-97AD-B78830B6E0C0}' : 'DWGEllipticalArcProxy',
	'{7EB60BBC-FF1C-428E-BB89-5F69BD727E83}' : 'DWGLineProxy',
	'{BA9FAF37-B4D2-45C1-BBBE-78E7B8ECB219}' : 'DWGPointProxy',
	'{6755F53A-DF74-4D7A-AB08-340C5AAD6F5C}' : 'DWGPolylineProxy',
	'{EF97259E-0689-42D1-AFAC-1FFD9F6A1980}' : 'DWGSplineProxy',
	'{C5A7AC9D-A15D-46B9-8582-31BD4E8D05CD}' : 'DWGPolyline2DProxy',
	'{078D1300-9A94-4644-BB80-BFD3B4600F3A}' : 'DWGPolyline3DProxy',
	'{A3DF761A-289E-4DBA-9BBE-4FC0A9665559}' : 'DWGACMStandardPartProxy',
	'{3E8A1835-A481-4153-A44C-8B75A94A5C05}' : 'DWGAcadSupportedProxyProxy',
	'{3CDDC905-E3FD-4255-890B-028E2523B0BF}' : 'DWGEntitySegmentProxy',
	'{143A4592-E2D5-47BD-9161-9CD37E6948F9}' : 'DWGEntityArcSegment',
	'{6DB61529-F8A8-46C6-988A-3E37306EAEC7}' : 'DWGEntityArcSegmentProxy',
	'{D27C87CF-D6D4-4B7C-BE3F-04623C44910D}' : 'DWGEntityEllipticalArcSegment',
	'{6DEC7317-ECC4-4007-9FAF-E1F7A570A2D2}' : 'DWGEntityEllipticalArcSegmentProxy',
	'{5B34AC50-EB91-4C51-AD13-6D9994BF1C62}' : 'DWGEntityLineSegment',
	'{E66320B8-E8EC-499F-AB2D-ACC633020A1C}' : 'DWGEntityLineSegmentProxy',
	'{B19DEB3B-9A69-4BAC-AEBB-20B92FD93B16}' : 'DWGEntitySplineSegment',
	'{66345F07-0F3F-4480-9D7F-80493F361595}' : 'DWGEntitySplineSegmentProxy',
	'{C2F5F99E-12F8-4AC2-9DC8-74F076FE9036}' : 'MeshFeatureProxy',
	'{873C598A-4E73-4BC1-BFF2-8370A1CDC935}' : 'MeshFeatureSetProxy',
	'{8D2C37E8-0C75-4B02-A09D-93F648E72CE7}' : 'MeshFeatureEntityProxy',
	'{FEA9A836-D065-45BD-9898-564E67B5F11A}' : 'MeshFace',
	'{EDE2434F-2FED-4902-82B0-8112FD7079C1}' : 'MeshFaceProxy',
	'{46BC8F99-10AF-4045-AADB-79A062E6508A}' : 'MeshEdge',
	'{AAE3F8BA-A09D-4788-B4E3-F637183206DA}' : 'MeshEdgeProxy',
	'{3C6AA9D5-971C-4753-9293-4E806CA49074}' : 'MeshVertex',
	'{D94E7C45-598A-4EA3-AD99-F4562C267BA3}' : 'MeshVertexProxy',
	'{A697A765-A9A9-4ACC-842D-4071034B9BCB}' : 'PublicationMeshEdge',
	'{4B3E3AD0-F07C-4CD0-A184-EA58A11EB9B3}' : 'PublicationMeshFace',
	'{A8B09AA7-B712-47AC-B188-00B659E84903}' : 'PublisherServer',
	'{F08B385C-86E0-4A1A-9E06-5A30BBE96ACB}' : 'PresentationTrailSegmentsEnumerator',
	'{E06DD476-868C-43C7-A3F5-3D624ADD40AF}' : 'DerivedFuturePartComponentProxy',
	'{27802D7B-DD17-4A6E-9889-99BB57A833E2}' : 'DerivedFutureAssemblyComponentProxy',
	'{7BF80981-BF32-101A-8BBB-00AA00300CAB}' : 'IPictureDisp',
}
VTablesToClassMap = {}
VTablesToPackageMap = {
	'{70109AA7-63C1-11D2-B78B-0060B0EC020B}' : 'IRxDocumentEvents',
	'{70109AA8-63C1-11D2-B78B-0060B0EC020B}' : 'IRxApplicationEvents',
	'{9235396C-0350-11D3-B787-0060B0F159EF}' : 'IRxUserInputEvents',
	'{32E4A318-C5E8-11D2-B77F-0060B0F159EF}' : 'IRxFileAccessEvents',
	'{AE277671-2FDC-11D3-B78F-0060B0F159EF}' : 'IRxTransactionEvents',
	'{70109AA6-63C1-11D2-B78B-0060B0EC020B}' : 'IRxFileUIEvents',
	'{5DF86067-6B16-11D3-B794-0060B0F159EF}' : 'IRxSurfaceBody',
	'{5DF86071-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumFaceShells',
	'{5DF86068-6B16-11D3-B794-0060B0F159EF}' : 'IRxFaceShell',
	'{5DF86072-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumFaces',
	'{5DF86069-6B16-11D3-B794-0060B0F159EF}' : 'IRxFace',
	'{5DF86073-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumEdgeLoops',
	'{5DF8606A-6B16-11D3-B794-0060B0F159EF}' : 'IRxEdgeLoop',
	'{5DF86074-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumEdgeUses',
	'{5DF8606B-6B16-11D3-B794-0060B0F159EF}' : 'IRxEdgeUse',
	'{5DF8606C-6B16-11D3-B794-0060B0F159EF}' : 'IRxEdge',
	'{5DF8606D-6B16-11D3-B794-0060B0F159EF}' : 'IRxVertex',
	'{5DF86075-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumEdges',
	'{5DF8603C-6B16-11D3-B794-0060B0F159EF}' : 'IRxCurveEvaluator',
	'{5DF8602A-6B16-11D3-B794-0060B0F159EF}' : 'IRxBox',
	'{CB69F15D-558E-11D3-B793-0060B0F159EF}' : 'IRxPoint',
	'{5DF8603D-6B16-11D3-B794-0060B0F159EF}' : 'IRxCurve2dEvaluator',
	'{5DF8602B-6B16-11D3-B794-0060B0F159EF}' : 'IRxBox2d',
	'{CB69F15E-558E-11D3-B793-0060B0F159EF}' : 'IRxPoint2d',
	'{5DF86076-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumVertices',
	'{5DF8606E-6B16-11D3-B794-0060B0F159EF}' : 'IRxSurfaceEvaluator',
	'{5DF8600D-6B16-11D3-B794-0060B0F159EF}' : 'IRxComponentDefinition',
	'{5DF86070-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumSurfaceBodies',
	'{5DF86012-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumComponentOccurrences',
	'{9D7CECDD-2CF1-11D4-B7A8-0060B0F159EF}' : 'IRxComponentOccurrence',
	'{5DF8600F-6B16-11D3-B794-0060B0F159EF}' : 'IRxComponentOccurrenceOld',
	'{CB69F15B-558E-11D3-B793-0060B0F159EF}' : 'IRxMatrix',
	'{5DF86026-6B16-11D3-B794-0060B0F159EF}' : 'IRxReferenceKey',
	'{5DF86010-6B16-11D3-B794-0060B0F159EF}' : 'IRxGeometryProxy',
	'{5DF86013-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumComponentDefinitionReferences',
	'{5DF8600E-6B16-11D3-B794-0060B0F159EF}' : 'IRxComponentDefinitionReference',
	'{5DF8600C-6B16-11D3-B794-0060B0F159EF}' : 'IRxComponentDocument',
	'{5DF86011-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumComponentDefinitions',
	'{5DF8606F-6B16-11D3-B794-0060B0F159EF}' : 'IRxAlternateSurfaceBody',
	'{E3571291-DB40-11D2-B783-0060B0F159EF}' : 'IRxApplicationAddIn',
	'{E3571290-DB40-11D2-B783-0060B0F159EF}' : 'IRxEnumApplicationAddIns',
	'{5DF86032-6B16-11D3-B794-0060B0F159EF}' : 'IRxBSplineCurve',
	'{5DF86033-6B16-11D3-B794-0060B0F159EF}' : 'IRxBSplineCurve2d',
	'{5DF8609C-6B16-11D3-B794-0060B0F159EF}' : 'IRxBSplineSurface',
	'{CB69F161-558E-11D3-B793-0060B0F159EF}' : 'IRxUnitVector',
	'{5DF8602E-6B16-11D3-B794-0060B0F159EF}' : 'IRxCircle',
	'{5DF8602F-6B16-11D3-B794-0060B0F159EF}' : 'IRxCircle2d',
	'{5DF86099-6B16-11D3-B794-0060B0F159EF}' : 'IRxCone',
	'{5DF86098-6B16-11D3-B794-0060B0F159EF}' : 'IRxCylinder',
	'{CB69F15F-558E-11D3-B793-0060B0F159EF}' : 'IRxVector',
	'{5DF86030-6B16-11D3-B794-0060B0F159EF}' : 'IRxEllipseFull',
	'{CB69F160-558E-11D3-B793-0060B0F159EF}' : 'IRxVector2d',
	'{5DF86031-6B16-11D3-B794-0060B0F159EF}' : 'IRxEllipseFull2d',
	'{97ED8AED-EF9D-11D3-B7A2-0060B0F159EF}' : 'IRxEllipticalCone',
	'{FA34A3FE-F063-11D3-B7A2-0060B0F159EF}' : 'IRxEllipticalCylinder',
	'{59D3FA3B-ACE0-11D3-B79A-0060B0F159EF}' : 'IRxEnumComponentDocuments',
	'{00C8476D-E79F-11D2-B785-0060B0F159EF}' : 'IRxReferencedFileDescriptor',
	'{D4606260-75D8-48EA-A3C3-A971E2384118}' : 'IRxFileAndReferences',
	'{C0E7110B-2136-11D4-8DD0-0010B541CAA8}' : 'IRxFileAndReferencesOld2',
	'{023BEB56-898C-11D2-86B1-080009DB6864}' : 'IRxFileAndReferencesOld',
	'{2C9F9B60-8967-11D2-86B1-080009DB6864}' : 'IRxEnumFileAndReferences',
	'{00C8476F-E79F-11D2-B785-0060B0F159EF}' : 'IRxEnumReferencedFileDescriptors',
	'{9CAF9897-33EA-11D3-B78F-0060B0F159EF}' : 'IRxEnumReferencedOLEFileDescriptors',
	'{9CAF9896-33EA-11D3-B78F-0060B0F159EF}' : 'IRxReferencedOLEFileDescriptor',
	'{73F35CCB-ED6E-11D2-B785-0060B0F159EF}' : 'IRxPropertySets',
	'{73F35CCD-ED6E-11D2-B785-0060B0F159EF}' : 'IRxPropertySet',
	'{73F35CCF-ED6E-11D2-B785-0060B0F159EF}' : 'IRxProperty',
	'{5DF86027-6B16-11D3-B794-0060B0F159EF}' : 'IRxEnumReferenceKeys',
	'{CB69F159-558E-11D3-B793-0060B0F159EF}' : 'IRxFacetsOld',
	'{2894395B-1E28-4516-8308-6AD0911B83D5}' : 'IRxFacets',
	'{42C7E0BF-FDCF-11D2-B785-0060B0F159EF}' : 'IRxFileLocations',
	'{5DF86015-6B16-11D3-B794-0060B0F159EF}' : 'IRxGeometricLocate',
	'{CB69F163-558E-11D3-B793-0060B0F159EF}' : 'IRxLine',
	'{CB69F162-558E-11D3-B793-0060B0F159EF}' : 'IRxUnitVector2d',
	'{CB69F164-558E-11D3-B793-0060B0F159EF}' : 'IRxLine2d',
	'{CB69F15C-558E-11D3-B793-0060B0F159EF}' : 'IRxMatrix2d',
	'{5DF86097-6B16-11D3-B794-0060B0F159EF}' : 'IRxPlane',
	'{5DF86028-6B16-11D3-B794-0060B0F159EF}' : 'IRxReferenceKeyManager',
	'{0000000C-0000-0000-C000-000000000046}' : 'IStream',
	'{0C733A30-2A1C-11CE-ADE5-00AA0044773D}' : 'ISequentialStream',
	'{00000100-0000-0000-C000-000000000046}' : 'IEnumUnknown',
	'{5DF8609A-6B16-11D3-B794-0060B0F159EF}' : 'IRxSphere',
	'{CB69F15A-558E-11D3-B793-0060B0F159EF}' : 'IRxStrokesOld',
	'{DAEA25A5-513E-41CA-BB8F-8E88B507C52E}' : 'IRxStrokes',
	'{5DF8609B-6B16-11D3-B794-0060B0F159EF}' : 'IRxTorus',
	'{C1B42715-92E9-4278-BD5F-6DCE4B25FEBE}' : 'IRxTransientGeometry',
	'{95105315-340B-4406-AAB1-2039EAA23E7D}' : 'IRxApprenticeServer',
	'{0A5CE3AB-073D-11D4-B7A4-0060B0F159EF}' : 'IRxApprenticeServerOld',
	'{42C7E0BE-FDCF-11D2-B785-0060B0F159EF}' : 'IRxFileSaveAs',
	'{0000010B-0000-0000-C000-000000000046}' : 'IPersistFile',
	'{0000010C-0000-0000-C000-000000000046}' : 'IPersist',
	'{E3571297-DB40-11D2-B783-0060B0F159EF}' : 'IRxApplicationAddInSiteOld',
	'{6A2718FD-4CCB-46D8-857A-CB83113FD4B9}' : 'IRxApplicationAddInSite',
	'{E3571292-DB40-11D2-B783-0060B0F159EF}' : 'IRxApplicationAddInServer',
	'{6ECCBC7B-A50D-11D4-8DE4-0010B541CAA8}' : 'IRxTranslatorAddInServer',
	'{863741CF-1A34-11D5-8DEC-0010B541CAA8}' : 'IRxTranslatorAddInServer2',
}


NamesToIIDMap = {
	'ComponentDefinition' : '{5DF8601E-6B16-11D3-B794-0060B0F159EF}',
	'SurfaceBodies' : '{5DF860AE-6B16-11D3-B794-0060B0F159EF}',
	'SurfaceBody' : '{5DF86089-6B16-11D3-B794-0060B0F159EF}',
	'FaceShells' : '{5DF86091-6B16-11D3-B794-0060B0F159EF}',
	'FaceShell' : '{5DF8608A-6B16-11D3-B794-0060B0F159EF}',
	'Faces' : '{5DF86092-6B16-11D3-B794-0060B0F159EF}',
	'Face' : '{5DF8608B-6B16-11D3-B794-0060B0F159EF}',
	'PartFeature' : '{DA33F1A4-7C3F-11D3-B794-0060B0F159EF}',
	'AttributeSets' : '{790B4EB3-7947-4D08-9510-372E93A24CF1}',
	'AttributeSet' : '{EFA08B24-F116-4751-90FA-46ADE09BF0B3}',
	'Attribute' : '{BC3487BB-F349-4A6C-9F72-D8C62CBADE6B}',
	'DataIO' : '{FBCADB33-9CBE-11D3-B799-0060B0F159EF}',
	'AttributesEnumerator' : '{1734EB04-2921-11D5-A4C1-00C04F6B9531}',
	'Box' : '{5DF86062-6B16-11D3-B794-0060B0F159EF}',
	'Point' : '{CB69F172-558E-11D3-B793-0060B0F159EF}',
	'Matrix' : '{CB69F171-558E-11D3-B793-0060B0F159EF}',
	'Vector' : '{CB69F174-558E-11D3-B793-0060B0F159EF}',
	'UnitVector' : '{CB69F176-558E-11D3-B793-0060B0F159EF}',
	'RenderStyle' : '{D480B516-E785-4CEE-B43C-FD4E3B6055F4}',
	'ComponentOccurrencesEnumerator' : '{EF562DD1-92FA-11D4-8DE0-0010B541CAA8}',
	'ComponentOccurrence' : '{5DF86020-6B16-11D3-B794-0060B0F159EF}',
	'AssemblyComponentDefinition' : '{AA044AA1-D685-11D3-B7A0-0060B0F159EF}',
	'ComponentOccurrences' : '{5DF86024-6B16-11D3-B794-0060B0F159EF}',
	'NameValueMap' : '{6BA435DD-BBD6-11D4-8DE6-0010B541CAA8}',
	'ClientGraphicsCollection' : '{66829BB6-656B-431C-BF5C-0BF53DBA225D}',
	'ClientGraphics' : '{2B0F6166-711D-47E0-B9B1-54ED9E3F160B}',
	'GraphicsNode' : '{58614F83-BD65-4B95-9C8B-92280B06D2F1}',
	'GraphicsPrimitive' : '{EBDAEE90-2DE0-42E5-8AA0-823A643DB4B3}',
	'Point2d' : '{CB69F173-558E-11D3-B793-0060B0F159EF}',
	'Matrix2d' : '{DA33F19F-7C3F-11D3-B794-0060B0F159EF}',
	'Vector2d' : '{CB69F175-558E-11D3-B793-0060B0F159EF}',
	'UnitVector2d' : '{CB69F177-558E-11D3-B793-0060B0F159EF}',
	'LineGraphics' : '{6C312B38-95D8-47B3-A6A8-78942F77A1C7}',
	'GraphicsCoordinateSet' : '{956DA506-F82D-4924-A000-C1A66CDB3B49}',
	'GraphicsIndexSet' : '{9D2A8D7D-D599-4D54-BDE0-586E5E18880D}',
	'GraphicsColorSet' : '{E54B3528-EB27-4A1A-8403-48A9846C93BB}',
	'Color' : '{0D084DAB-C766-4595-A449-7625772E88D2}',
	'LineStripGraphics' : '{D2666468-C11D-42F3-AB1E-6E590C5AA182}',
	'PointGraphics' : '{114E3531-FE3B-4042-A454-372A6B98F26F}',
	'GraphicsImageSet' : '{FC23373B-FA59-43C7-BD1B-2618DFA1C8C0}',
	'TextGraphics' : '{F3D4C961-7227-4E32-90A3-C60A9EEFA90D}',
	'TriangleFanGraphics' : '{99CBF031-2FFA-440F-B947-8470CD64E79C}',
	'GraphicsNormalSet' : '{D8297E9E-DD8B-4C8D-9271-186CAE8E00C1}',
	'GraphicsColorMapper' : '{AFA9F4D2-A1D8-42C3-8BFA-994FFAB1BEA4}',
	'GraphicsTextureCoordinateSet' : '{FFA15510-CD22-4C40-8DEE-4F846C3D5470}',
	'TriangleGraphics' : '{B5E1C129-EE0E-4C45-9AC3-FE79794F1EB0}',
	'TriangleStripGraphics' : '{907F6639-A091-4B19-B1B4-E677D960934C}',
	'FeatureGraphics' : '{6757C085-699B-474B-9566-61221A64A09F}',
	'CurveGraphics' : '{9AB0A7C1-DDEE-400D-B526-287FB2EB6DDD}',
	'ViewList' : '{807562AB-40E2-47D3-9FDC-E74E2D1E5724}',
	'View' : '{70109AA3-63C1-11D2-B78B-0060B0EC020B}',
	'Document' : '{70109AA1-63C1-11D2-B78B-0060B0EC020B}',
	'File' : '{6E5CDAB2-6BA5-4EAD-B357-78646BE0A813}',
	'FileDescriptorsEnumerator' : '{C64DD969-DCB0-4FA9-AD0A-E09744466D61}',
	'FileDescriptor' : '{67CF708B-CA38-419D-8016-19CEAA5FBB7D}',
	'FilesEnumerator' : '{4771DB69-A789-4BA4-A35C-56BFCC6AECFA}',
	'DocumentDescriptorsEnumerator' : '{DBD3CBEE-DBBC-4A71-B122-33A8D1786D20}',
	'DocumentDescriptor' : '{D755CFCA-9E02-4A08-AFE8-7178E818C763}',
	'DocumentsEnumerator' : '{ACE59077-7778-11D4-8DD8-0010B541CAA8}',
	'Views' : '{70109AA4-63C1-11D2-B78B-0060B0EC020B}',
	'ClientViews' : '{3D218008-FA54-48CB-89BC-8EFBF3D0B6CC}',
	'ClientView' : '{BCD3EFAF-0FEF-4AC1-8303-2A4BF18E96FC}',
	'Camera' : '{9C88D3AD-C3EB-11D3-B79E-0060B0F159EF}',
	'DocumentEventsObject' : '{1F6B29F0-6C04-4D11-8ACE-9D41C2904FCD}',
	'DocumentEventsSink' : '{851B66FA-B31A-453D-8628-2DE2A5768C59}',
	'ReferencedOLEFileDescriptors' : '{9CAF98A0-33EA-11D3-B78F-0060B0F159EF}',
	'ReferencedOLEFileDescriptor' : '{9CAF989F-33EA-11D3-B78F-0060B0F159EF}',
	'ObjectsEnumerator' : '{A94DCF5E-90E9-4F60-BB55-F65B4618ECD5}',
	'ReferencedOpaqueFileDescriptors' : '{5076EA3C-FC27-499D-BEC8-B57BD219F0A7}',
	'ReferencedOpaqueFileDescriptor' : '{5076EA3B-FC27-499D-BEC8-B57BD219F0A7}',
	'SoftwareVersion' : '{076C16D1-4994-11D4-9E0F-0010A4C72F07}',
	'PropertySets' : '{73F35CC8-ED6E-11D2-B785-0060B0F159EF}',
	'PropertySet' : '{73F35CC7-ED6E-11D2-B785-0060B0F159EF}',
	'Property' : '{73F35CC9-ED6E-11D2-B785-0060B0F159EF}',
	'AttributeManager' : '{46D51BD4-B58D-4C94-BA7A-124B184AC687}',
	'AttributeSetsEnumerator' : '{1734EB03-2921-11D5-A4C1-00C04F6B9531}',
	'ObjectCollection' : '{6939FFDD-BA10-11D2-B779-0060B0F159EF}',
	'UnitsOfMeasure' : '{D007B6F9-71BB-48FF-B14C-EE5D633CB0C3}',
	'ParametersEnumerator' : '{C52EE54D-B18E-4CB3-AEE3-7D0375F92948}',
	'Parameter' : '{44E517BC-D882-4AFE-A300-B3DAC6B8DB58}',
	'ExpressionList' : '{C13EA1C0-2DD0-4B64-9938-0E4804316912}',
	'Tolerance' : '{77B88412-A66B-43BE-BEE2-06CFE38B0C70}',
	'CustomPropertyFormat' : '{B2EC7987-2BDE-47F6-8EE7-534C7B854B2B}',
	'PrintManager' : '{69190E26-316F-47BD-AE75-8B64641C18C8}',
	'GraphicsDataSetsCollection' : '{8C2CC3CF-A455-40D6-8505-56A702F6FB77}',
	'GraphicsDataSets' : '{400A64D5-7150-42F6-943E-F190518265CA}',
	'GraphicsDataSet' : '{D4BF045D-8DFB-44B5-9FFC-FE6ACADF2B23}',
	'RenderStyles' : '{1F76C4FA-DB71-4D87-8390-1529297ED5A9}',
	'BrowserPanes' : '{1EBEC999-3A4D-4A4C-A35A-3F2E773DD56D}',
	'BrowserPaneObject' : '{21F02BD0-F849-49E1-A1EC-A04A8F49AE05}',
	'BrowserPaneSink' : '{619680F8-EB9A-4F13-8D23-721FE776C955}',
	'BrowserNode' : '{5D21C290-CB28-4861-9367-C3F1B9F0BCCB}',
	'BrowserNodeDefinition' : '{E9E1E669-7C31-486B-A5A6-FD0825ABCB28}',
	'BrowserNodesEnumerator' : '{76B0EC66-F962-4D22-9E96-3D02F49AD363}',
	'Application' : '{70109AA0-63C1-11D2-B78B-0060B0EC020B}',
	'Documents' : '{70109AA2-63C1-11D2-B78B-0060B0EC020B}',
	'ApplicationEventsObject' : '{6ED45F3A-BAF4-41FE-8907-970BB3CA48DF}',
	'ApplicationEventsSink' : '{CD4C47ED-C403-4F42-B3BF-0A90F3E89D81}',
	'WebView' : '{CCEBC8A5-7171-47B6-B9DC-067DAC0C79E7}',
	'DesignProject' : '{9A14B139-7101-40B1-BD92-B3F9870DC7F0}',
	'ContentCenterConfiguration' : '{0B13DE4E-2371-408F-AF1A-F884A9061ED9}',
	'IntentConfiguration' : '{CF66D521-D40D-477C-A686-D2D5A614D323}',
	'ProjectPaths' : '{7B4F757F-55D3-4078-9AED-61AD15AC9AD5}',
	'ProjectPath' : '{F8D97A2E-CC4D-49EF-8FFF-F16F2FB13929}',
	'DesignProjectManager' : '{4A60CB5E-1EE8-4180-A801-194704F3021E}',
	'DesignProjects' : '{131DB1C8-39A0-41F6-B881-9B49050D08DC}',
	'ProjectOptionsButtonObject' : '{4F599909-D43A-4090-BC23-3616A075A02D}',
	'ProjectOptionsButtonSink' : '{0C946530-B275-481A-9573-6CA7D4F93611}',
	'ProjectAssetLibrary' : '{C6EEC114-BE48-4323-B58C-9DF90ED92996}',
	'ProjectAssetLibraries' : '{EC5AD11E-A3AB-4C86-85BD-61DEBF623987}',
	'ModelingEventsObject' : '{A50B89A5-B9C9-449C-AD62-813F12D80A5D}',
	'ModelingEventsSink' : '{124B76C3-CB79-4414-9CB9-DDA2F8C5C90A}',
	'ClientFeature' : '{BB91C845-BD7E-4470-948F-C5A069B21BBC}',
	'FeatureDimensions' : '{44A143D3-13C8-4B0A-AE53-CCC6169C44DB}',
	'FeatureDimension' : '{6C0C1E47-E731-4ECF-8EDD-EF8CE58E395E}',
	'Asset' : '{766A9447-A604-43C8-9393-2D2709837D1E}',
	'AssetValue' : '{C6E1E6AB-897D-4CDD-A486-4ABAA04FC9B9}',
	'AssetCategory' : '{25E59F53-ADFB-4B1B-8CF4-C8EAE80CA85F}',
	'AssetLibrary' : '{BE5F1900-C9E6-49B4-BA3A-1BC7FF49DCD0}',
	'AssetCategories' : '{047360BD-1872-4C10-8538-01518FD7F750}',
	'AssetsEnumerator' : '{505BB0CA-670E-4D54-AB26-F66A64DBB72C}',
	'ClientFeatureDefinition' : '{0A1F6F03-BA19-49CD-8376-93A85FB08A2A}',
	'ClientFeatureElements' : '{112F95FB-41E9-466C-9ACC-1074F5512831}',
	'ClientFeatureElement' : '{BA8A81FD-71F7-4BE4-A009-1CC6731723FD}',
	'ModelAnnotations' : '{9789E1AC-1767-4225-96DD-FD06F614AD59}',
	'ModelAnnotation' : '{089C1D07-A3A6-4649-B1C4-CE9DAB1D8BBE}',
	'ModelCompositeAnnotation' : '{6E94434B-5CEC-4CC5-AB2E-B37904E7264E}',
	'ModelToleranceFeature' : '{CEBC9A45-2058-4537-9D52-5E11419267DE}',
	'ModelToleranceFeatureDefinition' : '{A342F0A8-2B29-44B8-BB55-C6A89EC0A977}',
	'ModelAnnotationsEnumerator' : '{8F656C43-9BFD-4BAE-AF23-A21067DDED8E}',
	'FaceCollection' : '{24B7B991-46D9-45F8-82CD-05212ECFC6DD}',
	'ModelToleranceFeaturesEnumerator' : '{E0AE1A27-0BDD-442C-8A74-92F5E6F1E839}',
	'ModelCompositeAnnotationDefinition' : '{F874F2B3-E7C0-434A-BC00-DE5E1B687452}',
	'ModelFeatureControlFrames' : '{01711A84-0018-4452-A736-D9292E754D38}',
	'ModelFeatureControlFrame' : '{F2948971-943D-4CBB-88B0-20E0B48B8573}',
	'ModelFeatureControlFrameDefinition' : '{CD675FA9-2F1B-4574-B287-C0C601CCC1B1}',
	'AnnotationPlane' : '{FAF83927-A3E9-4ABC-BBCF-AA1D983010F8}',
	'AnnotationPlaneDefinition' : '{740E1B50-7EC5-4C4E-B94B-CCEB4FB5C489}',
	'Line' : '{CB69F178-558E-11D3-B793-0060B0F159EF}',
	'CurveEvaluator' : '{5DF860B0-6B16-11D3-B794-0060B0F159EF}',
	'Plane' : '{CB69F17A-558E-11D3-B793-0060B0F159EF}',
	'SurfaceEvaluator' : '{5DF860B2-6B16-11D3-B794-0060B0F159EF}',
	'Box2d' : '{5DF86063-6B16-11D3-B794-0060B0F159EF}',
	'ModelFeatureControlFrameRows' : '{181A614B-8F7D-4E15-BCF9-08ECC5F225E2}',
	'ModelFeatureControlFrameRow' : '{D0F606AE-494C-4810-8280-071F5A56824F}',
	'ModelDatumIdentifier' : '{EB143431-FB4F-4B4B-BDDA-C21026571456}',
	'ModelDatumIdentifierDefinition' : '{0B87CDBE-3271-46A7-9C95-259667C9FFCF}',
	'GeometryIntent' : '{56B990B9-D25A-436F-A652-1D21EC739C57}',
	'ModelLeader' : '{F2E7C272-A777-41B1-B217-C31B8CFAEF77}',
	'ModelLeaderNode' : '{7430CE13-37A3-4A67-A645-2AAD0BB71038}',
	'ModelLeaderNodesEnumerator' : '{76A8F762-B6B5-4B18-916C-EC7C17B22618}',
	'ModelSurfaceTextureSymbols' : '{5FCCBA74-9BA4-49C7-95D3-FC9E7D76EFB3}',
	'ModelSurfaceTextureSymbol' : '{E083158B-C56B-4CB0-B637-C56896BDAF1C}',
	'ModelSurfaceTextureSymbolDefinition' : '{85B493F3-342B-4D54-83A1-4EF9C50378D0}',
	'ModelDimensions' : '{7AD96A84-A539-4220-B9AD-7A2854D518B8}',
	'AngularModelDimensions' : '{29C4F94E-2656-4727-8510-2B0DAF6FCEFE}',
	'AngularModelDimension' : '{1BFD9261-5C05-4BF4-9A9F-F5323F3C8E69}',
	'ModelDimensionDefinition' : '{4062D31A-F8CE-4D38-B50A-6D8B1FB50D94}',
	'ModelDimension' : '{C66A1C65-43C3-4F1C-A22C-089F3F03349A}',
	'ModelAnnotationText' : '{B513304D-05B5-4DD7-AA23-E4BF2F120406}',
	'LineSegment' : '{607CC753-5796-4409-85F4-9EA576EAA417}',
	'AngularModelDimensionDefinition' : '{A765255E-0264-4316-9F81-F5B051281001}',
	'DiameterModelDimensions' : '{17BE1D0D-0A2B-4A92-9CB2-A9725D391143}',
	'DiameterModelDimension' : '{098FDC37-8060-4944-AD0E-B55FEC55CA8C}',
	'DiameterModelDimensionDefinition' : '{5FCEA8CE-F9AE-4216-8AAD-2530EC41B619}',
	'LinearModelDimensions' : '{D60D7065-70F2-4E41-AE17-17E36EE573DF}',
	'LinearModelDimension' : '{7D6FF00B-9613-4E95-AA2F-484E089AAEA3}',
	'LinearModelDimensionDefinition' : '{84385A0E-4B73-48FE-B948-CB83894F2E61}',
	'RadiusModelDimensions' : '{7C6BCC40-95D1-4B47-AE7F-A5EBFEF95851}',
	'RadiusModelDimension' : '{672C4DAF-1B67-4131-8F53-9274F42E44E9}',
	'RadiusModelDimensionDefinition' : '{62D66B29-1EA9-48CA-A6C6-6D6FF7785213}',
	'ModelHoleThreadNotes' : '{C5BF9314-D319-44A4-BDFF-16142CE92D58}',
	'ModelHoleThreadNote' : '{2BAE3F08-F0AE-4B03-A432-E3A3C22408F6}',
	'ModelHoleThreadNoteDefinition' : '{90ED1343-7C9E-4042-9664-93D821AF88CC}',
	'HoleClearanceInfo' : '{59B2196B-616D-41FC-A7B9-FFAD0334B48D}',
	'ModelLeaderNotes' : '{B97AC4F4-708A-431E-90BA-AFDCC6623A84}',
	'ModelLeaderNote' : '{5194100D-435F-4C85-A922-6BD3E4CC9C36}',
	'ModelLeaderNoteDefinition' : '{3614BB38-60E8-42E0-84E1-A0045BFB25D4}',
	'ModelDatumIdentifiers' : '{498E2A5A-76DD-4059-BB54-300D026EC79D}',
	'AnnotationPlaneDefinitionsEnumerator' : '{FA169DD0-A365-49D9-9572-F0F23F2B634E}',
	'ModelCompositeAnnotations' : '{45EEBC4D-5D77-4D15-A138-4522B26F1631}',
	'ModelGeneralNotes' : '{0C71D10A-6A99-42EB-8563-6D7F2DD934EF}',
	'ModelGeneralNote' : '{88C68B3A-B9B0-45DD-873C-FA0187B80E62}',
	'ModelGeneralNoteDefinition' : '{6EE0926D-4482-4469-8AE3-C90231C60713}',
	'GeneralNoteSymbolDefinitions' : '{828F3709-2B6A-4CCE-942D-DC8A3FD92D44}',
	'GeneralNoteSymbolDefinition' : '{949C0CAF-E83D-4AEB-B734-7DA77D913967}',
	'SketchEventsObject' : '{0CB0F042-1627-49BF-B430-619A3AD6FADC}',
	'SketchEventsSink' : '{3B71CB69-62FB-40D1-BEF9-3B0C255C8DD4}',
	'Sketch' : '{5FDB5E25-C96F-11D5-8DF9-0010B541CAA8}',
	'GeometricConstraints' : '{8006A072-ECC4-11D4-8DE9-0010B541CAA8}',
	'GeometricConstraint' : '{B5461257-09AA-11D5-8DEC-0010B541CAA8}',
	'CoincidentConstraint' : '{8006A074-ECC4-11D4-8DE9-0010B541CAA8}',
	'SketchEntity' : '{B546124D-09AA-11D5-8DEC-0010B541CAA8}',
	'SketchConstraintsEnumerator' : '{8006A026-ECC4-11D4-8DE9-0010B541CAA8}',
	'ReferenceComponent' : '{DD8AB7FC-77D4-4EA8-83A9-A0C868DABFC0}',
	'ReferencedFileDescriptor' : '{9E0BA9CA-E916-11D2-B785-0060B0F159EF}',
	'Layer' : '{9FEBA8BF-6BB5-421E-82DE-F1C4A1639C70}',
	'DrawingStylesManager' : '{1A58DFEF-0B8C-44DF-97AF-4DAC85734B04}',
	'DrawingStandardStylesEnumerator' : '{415A6C89-2B25-4884-B2E3-78BC8CAB9AC2}',
	'DrawingStandardStyle' : '{55DBDB4E-BC61-4D53-84F6-86CF24267DD8}',
	'Style' : '{A5AFB9DC-4066-4800-A459-E4A7E4E433B6}',
	'ObjectDefaultsStyle' : '{E8528224-258B-471F-81E3-1F276425BC39}',
	'DimensionStyle' : '{3697D2E9-C4C2-4FF5-A60D-F5EC68EACD27}',
	'TextStyle' : '{A907AEC1-A78F-11D5-8DF8-0010B541CAA8}',
	'LeaderStyle' : '{7E4D60AD-496E-4336-96AA-5A2C6178C836}',
	'BalloonStyle' : '{04B1FC27-4477-491B-A640-3C313E9AC402}',
	'FeatureControlFrameStyle' : '{9CB10C50-7F27-4E55-BADE-15A308DB8820}',
	'HoleTableStyle' : '{97B2D2E2-78EA-4838-B140-2BBAB4D8E7A9}',
	'SurfaceTextureStyle' : '{F329734C-AAC4-40B9-A1A0-A051679C1EC7}',
	'CentermarkStyle' : '{AD4D6527-A103-4FF5-8433-FB90C52B9473}',
	'TableStyle' : '{A957DFC5-7AC5-497F-A7AF-5438FAFAD6B4}',
	'PartsListStyle' : '{6C65399A-B4E9-42DB-8659-6E13E4B07050}',
	'RevisionTableStyle' : '{4758367B-5DAF-4CE3-BDF1-189FAD8D6BD2}',
	'DimensionStylesEnumerator' : '{0134748C-7F24-467B-9DF2-6647677B125F}',
	'DrawingDocument' : '{29F0D467-C114-11D2-B77F-0060B0F159EF}',
	'ReferenceKeyManager' : '{1405C19D-F8AC-41AD-AAB2-D0923BD45C15}',
	'SelectSet' : '{189559A8-0C9B-4F77-93E9-8330AAAD7943}',
	'SelectionPreferences' : '{1907E11C-C275-4008-95FA-9AC7539E1A7C}',
	'InventorVBAProject' : '{95C6C576-FC7A-4B16-B565-BFABEF69B013}',
	'InventorVBAComponents' : '{24FAC734-1A3D-404E-A28B-7CC1AD47DCA1}',
	'InventorVBAComponent' : '{611EDF7B-009C-4871-B3F9-69E1B4A61C1E}',
	'InventorVBAMembers' : '{E83434B4-B12D-4A6F-A2DC-BFA52D3C5FA7}',
	'InventorVBAMember' : '{FBC2D851-EC7F-4D70-B13C-98B57B785E97}',
	'InventorVBAArguments' : '{BAB06F80-7165-484C-88DF-7D8A0004A76D}',
	'InventorVBAArgument' : '{25944748-FC4C-4214-A0AC-627BDF178793}',
	'DocumentSubType' : '{D3EDB5BC-7B47-42B9-9D77-F3A2676EC15B}',
	'HighlightSet' : '{545F2567-592E-45DA-A262-77BD7E546F7A}',
	'DocumentInterests' : '{B1DA2E33-F616-41D4-917A-CEB1138058D0}',
	'DocumentInterest' : '{36DB2A89-F970-4C03-AA8A-7864122D553B}',
	'_DocPerformanceMonitorObject' : '{AAF23B5F-E2FE-471C-85AA-E37FCE6DE651}',
	'_DocPerformanceMonitorSink' : '{C2083475-A259-414A-BED9-FC43291F4455}',
	'_SegPerformanceMonitor' : '{AE621339-6CA8-486C-BF06-E683D2EE3A8E}',
	'ReferencedFileDescriptors' : '{9E0BA9CB-E916-11D2-B785-0060B0F159EF}',
	'HighlightSets' : '{DD60CA37-AB7B-491F-AD9E-C9DF3B4B5BBB}',
	'Sheet' : '{206B59AE-22A6-11D4-B7A8-0060B0F159EF}',
	'DrawingViews' : '{206B59B2-22A6-11D4-B7A8-0060B0F159EF}',
	'DrawingView' : '{206B59B1-22A6-11D4-B7A8-0060B0F159EF}',
	'DrawingSketches' : '{1644E1D7-9BD5-11D5-8DF7-0010B541CAA8}',
	'DrawingSketch' : '{1644E1D5-9BD5-11D5-8DF7-0010B541CAA8}',
	'DimensionConstraints' : '{C173A075-012F-11D5-8DEA-0010B541CAA8}',
	'DimensionConstraint' : '{B5461259-09AA-11D5-8DEC-0010B541CAA8}',
	'OffsetDimConstraint' : '{C173A077-012F-11D5-8DEA-0010B541CAA8}',
	'SketchLine' : '{8006A016-ECC4-11D4-8DE9-0010B541CAA8}',
	'SketchEntitiesEnumerator' : '{B546124B-09AA-11D5-8DEC-0010B541CAA8}',
	'SketchBlock' : '{08A3AC40-A684-4F8B-8033-7D0FE23AFBE3}',
	'SketchBlocksEnumerator' : '{2C9F06C7-9124-43FE-B6D9-703620D53DA7}',
	'SketchBlockDefinition' : '{F393AB2C-8A8B-4B69-9F0D-91FFA842A53F}',
	'SketchArcs' : '{8006A032-ECC4-11D4-8DE9-0010B541CAA8}',
	'SketchArc' : '{8006A046-ECC4-11D4-8DE9-0010B541CAA8}',
	'SketchPoint' : '{8006A022-ECC4-11D4-8DE9-0010B541CAA8}',
	'Arc2d' : '{C173A091-012F-11D5-8DEA-0010B541CAA8}',
	'Curve2dEvaluator' : '{5DF860B1-6B16-11D3-B794-0060B0F159EF}',
	'Arc3d' : '{744FFECE-189A-4ACC-8BCF-8F959D5E4EAE}',
	'SketchLines' : '{8006A018-ECC4-11D4-8DE9-0010B541CAA8}',
	'SketchPoints' : '{8006A024-ECC4-11D4-8DE9-0010B541CAA8}',
	'SketchSplines' : '{8006A034-ECC4-11D4-8DE9-0010B541CAA8}',
	'SketchSpline' : '{8006A048-ECC4-11D4-8DE9-0010B541CAA8}',
	'BSplineCurve2d' : '{49CB4BBA-872A-11D3-8524-0060B0F0B5B7}',
	'SketchSplineHandle' : '{1236D237-9BAC-4399-8CFB-66CB6B7FD5CA}',
	'LineSegment2d' : '{C173A08D-012F-11D5-8DEA-0010B541CAA8}',
	'BSplineCurve' : '{49CB4BB9-872A-11D3-8524-0060B0F0B5B7}',
	'SketchOffsetSplines' : '{16372AAE-1133-4C4C-9A48-D9305D8358F3}',
	'SketchOffsetSpline' : '{063D7617-E630-4D35-B809-64D6695F57C0}',
	'SketchEllipses' : '{8006A036-ECC4-11D4-8DE9-0010B541CAA8}',
	'SketchEllipse' : '{8006A04A-ECC4-11D4-8DE9-0010B541CAA8}',
	'EllipseFull2d' : '{49CB4BB8-872A-11D3-8524-0060B0F0B5B7}',
	'EllipseFull' : '{49CB4BB7-872A-11D3-8524-0060B0F0B5B7}',
	'SketchEllipticalArcs' : '{C173A089-012F-11D5-8DEA-0010B541CAA8}',
	'SketchEllipticalArc' : '{C173A087-012F-11D5-8DEA-0010B541CAA8}',
	'EllipticalArc2d' : '{C173A095-012F-11D5-8DEA-0010B541CAA8}',
	'EllipticalArc' : '{C1066E40-4E2F-45C2-A5AB-E2B4D1B84A1E}',
	'SketchCircles' : '{8006A038-ECC4-11D4-8DE9-0010B541CAA8}',
	'SketchCircle' : '{8006A04C-ECC4-11D4-8DE9-0010B541CAA8}',
	'Circle2d' : '{49CB4BB6-872A-11D3-8524-0060B0F0B5B7}',
	'Circle' : '{49CB4BB5-872A-11D3-8524-0060B0F0B5B7}',
	'TextBoxes' : '{A907AE97-A78F-11D5-8DF8-0010B541CAA8}',
	'TextBox' : '{A907AE99-A78F-11D5-8DF8-0010B541CAA8}',
	'SketchFixedSplines' : '{6359FE67-0814-4847-9F33-72E0BB9EB688}',
	'SketchFixedSpline' : '{DCEF44A1-7A80-4A0A-937C-A349AF8A9233}',
	'SketchImages' : '{64D6BFDF-5B47-48C1-AC74-1BE2C24757B2}',
	'SketchImage' : '{C00FE3F4-2D75-4409-93FB-9B72913C073C}',
	'SketchControlPointSplines' : '{135F0952-BF41-444D-A962-8A7805AB2E78}',
	'SketchControlPointSpline' : '{D5F8CF99-AF1F-4089-A638-F6889762C1D6}',
	'SketchEquationCurves' : '{C38DE680-2374-487B-86F8-E3DA8012DE66}',
	'SketchEquationCurve' : '{6D7C3BDC-9CE1-4F23-82CC-2F001A326F89}',
	'Profiles' : '{523EF757-245A-11D5-8DEC-0010B541CAA8}',
	'Profile' : '{8006A03A-ECC4-11D4-8DE9-0010B541CAA8}',
	'ProfilePath' : '{B5461253-09AA-11D5-8DEC-0010B541CAA8}',
	'ProfileEntity' : '{B5461255-09AA-11D5-8DEC-0010B541CAA8}',
	'RegionProperties' : '{4735D53B-FEF2-4671-9430-3D60964D850B}',
	'Wires' : '{31B11F76-0E31-45DF-8BE6-409EE5416DC5}',
	'Wire' : '{A267D26D-EA7D-444F-8D54-7316BF10DD96}',
	'EdgeUses' : '{5DF86094-6B16-11D3-B794-0060B0F159EF}',
	'EdgeUse' : '{5DF8608D-6B16-11D3-B794-0060B0F159EF}',
	'Edge' : '{5DF8608E-6B16-11D3-B794-0060B0F159EF}',
	'Vertex' : '{5DF8608F-6B16-11D3-B794-0060B0F159EF}',
	'Edges' : '{5DF86095-6B16-11D3-B794-0060B0F159EF}',
	'EdgeCollection' : '{8DC730F1-A15F-4547-A279-69B7A9FAE657}',
	'EdgeLoop' : '{5DF8608C-6B16-11D3-B794-0060B0F159EF}',
	'PlanarSketch' : '{2C16787F-83FF-11D4-8DDB-0010B541CAA8}',
	'ProjectedCuts' : '{3C83A20C-1648-40C3-9A28-FFDE72124D2C}',
	'ProjectedCut' : '{21E8F0AC-DFCD-4800-B07A-6E0C492CC447}',
	'SketchBlocks' : '{A9C5B884-2122-4DBB-A94E-EB75ED78A160}',
	'TwoPointDistanceDimConstraint' : '{C173A079-012F-11D5-8DEA-0010B541CAA8}',
	'TwoLineAngleDimConstraint' : '{C173A07B-012F-11D5-8DEA-0010B541CAA8}',
	'ThreePointAngleDimConstraint' : '{C173A07D-012F-11D5-8DEA-0010B541CAA8}',
	'DiameterDimConstraint' : '{C173A07F-012F-11D5-8DEA-0010B541CAA8}',
	'RadiusDimConstraint' : '{C173A081-012F-11D5-8DEA-0010B541CAA8}',
	'ArcLengthDimConstraint' : '{FD350F5E-E3C9-4268-BCF4-0DEA91B6F8EF}',
	'TangentDistanceDimConstraint' : '{C173A085-012F-11D5-8DEA-0010B541CAA8}',
	'EllipseRadiusDimConstraint' : '{6ABB821F-4962-11D5-8DEE-0010B541CAA8}',
	'OffsetSplineDimConstraint' : '{BBCEA345-055B-4625-ABCA-582C6BF7E440}',
	'SketchFillRegions' : '{A7993C2A-CFCA-4455-BC79-B15952DBF102}',
	'SketchFillRegion' : '{920C0497-59BF-4F6C-A45C-8C8AA72750CF}',
	'AutomatedCenterlineSettings' : '{E72E9ED9-8A10-4292-9792-96FA51ECD810}',
	'DrawingCurvesEnumerator' : '{E49C9290-6D71-4C14-8B15-3595306A49D6}',
	'DrawingCurve' : '{1C98EA42-27FC-4BFA-84E4-D29C7A11F889}',
	'DrawingCurveSegments' : '{D05367DD-3A18-47DC-A618-7550582CEEDA}',
	'DrawingCurveSegment' : '{EEE9F58F-FD0B-4862-AE21-BAE203DFE23E}',
	'DrawingViewEventsObject' : '{1DA08DFE-88EB-4ABE-8FA8-34FD098D65AA}',
	'DrawingViewEventsSink' : '{F777456B-314C-4F8E-87E0-196CB7FC8D32}',
	'DrawingViewLabel' : '{C9216F3D-E886-4E75-89AB-D7665FA14AB1}',
	'OriginIndicator' : '{96E36D73-DFEC-4CF8-9DB3-F97F01A41A23}',
	'BreakOperations' : '{1880ABD8-B826-4258-A2F1-31B5E5740FA6}',
	'BreakOperation' : '{ABCACDBB-5EAF-4AF5-86A0-FB2DB0502D5D}',
	'BreakOutOperations' : '{600D4AE6-12FB-47E9-86E6-46C8C2A9161E}',
	'BreakOutOperation' : '{5D175430-8A8D-47F7-AABE-50C2E9B65D89}',
	'SectionDrawingView' : '{9CF770DE-2A15-4069-A057-AB247ACCFAFC}',
	'DetailDrawingView' : '{3B39A185-9BED-4494-993C-26762D8A2D5F}',
	'PartsLists' : '{A907AE85-A78F-11D5-8DF8-0010B541CAA8}',
	'PartsList' : '{A907AE87-A78F-11D5-8DF8-0010B541CAA8}',
	'PartsListColumns' : '{A907AE89-A78F-11D5-8DF8-0010B541CAA8}',
	'PartsListColumn' : '{A907AE8B-A78F-11D5-8DF8-0010B541CAA8}',
	'PartsListRows' : '{A907AE8D-A78F-11D5-8DF8-0010B541CAA8}',
	'PartsListRow' : '{A907AE8F-A78F-11D5-8DF8-0010B541CAA8}',
	'PartsListCell' : '{A907AE91-A78F-11D5-8DF8-0010B541CAA8}',
	'Balloons' : '{3DFE3282-5B67-431A-A890-040098957C1C}',
	'Balloon' : '{A5F6343C-7FE9-431E-BF12-A7308A57CE91}',
	'BalloonValueSets' : '{B3721DAB-0BAD-4296-8C1E-6608FC0F6049}',
	'BalloonValueSet' : '{380ED49C-ADD8-47EC-B99E-10D00CE618D7}',
	'DrawingBOMRow' : '{3538A9B3-0A9F-4B3E-9FC9-3272AB0D7C2B}',
	'BOMRow' : '{148682B7-6B44-4FF0-8C10-AB21D276602E}',
	'ComponentDefinitionsEnumerator' : '{C5AC2A12-6439-4CB5-BA1E-45765296285E}',
	'BOMRowsEnumerator' : '{BCDD5058-E7D5-4E88-8EF8-8D6370E0CBA3}',
	'DrawingBOMCell' : '{2FBF7141-4414-423B-9F95-3C6489DC47B9}',
	'DrawingBOM' : '{1290504E-696F-4480-8126-04A65C7DA45E}',
	'DrawingBOMColumns' : '{F78F8237-3CAA-467D-AB38-6998DF84B3BE}',
	'DrawingBOMColumn' : '{A36A7AD1-DDBD-4858-B025-D3F6C2042BC8}',
	'DrawingBOMRows' : '{6ADEEB5C-21C6-4995-91AA-7FD0CE1D0073}',
	'Leader' : '{77D4A0A3-255E-42A8-B0F5-41FE5007BCCE}',
	'LeaderNode' : '{48F6DB32-6623-4944-BBF1-12A26E47107A}',
	'LeaderNodesEnumerator' : '{26C1C5B1-44AE-4180-8118-EDF2B8CB220B}',
	'TitleBlock' : '{A907AEB9-A78F-11D5-8DF8-0010B541CAA8}',
	'TitleBlockDefinition' : '{A907AEB7-A78F-11D5-8DF8-0010B541CAA8}',
	'Border' : '{A907AEAF-A78F-11D5-8DF8-0010B541CAA8}',
	'BorderDefinition' : '{A907AEB3-A78F-11D5-8DF8-0010B541CAA8}',
	'CustomTables' : '{2A6C1D0D-FAF8-4A31-A9FB-39761F36F814}',
	'CustomTable' : '{88F528C1-AE9A-457B-8A19-A6224F473A62}',
	'Columns' : '{151E96E1-59DA-4732-B025-4AA7A1C9AF27}',
	'Column' : '{70984603-E322-4AC8-B6DE-2F5A31AF0910}',
	'Rows' : '{2022FEE8-01DA-481F-A515-D2D89C787EA8}',
	'Row' : '{8AF87EC1-B613-43DB-9FF6-E0D489B68DAE}',
	'Cell' : '{CE3FEA37-5793-4814-B9E4-88C84DC0BEEE}',
	'TableFormat' : '{A2F174A9-9D82-4AF1-B80C-67FB45B59923}',
	'RevisionTables' : '{DB2B25D3-66F3-47CC-9DBF-D6B7468EE76E}',
	'RevisionTable' : '{644AE247-EFBA-49FA-9F55-384CA82DB549}',
	'RevisionTableColumns' : '{CBC02A91-4346-4459-8A47-C845B0A4051F}',
	'RevisionTableColumn' : '{C802F139-6C51-4A73-ABAE-BF5E88687E00}',
	'RevisionTableRows' : '{C5EDE080-C83A-4D7F-9560-B867FD29DFD6}',
	'RevisionTableRow' : '{FB83111D-DED9-462D-9BC5-95A6933ADF4C}',
	'RevisionTableCell' : '{63C5D5FD-8348-4246-BE53-619E8C48EC6F}',
	'HoleTables' : '{8C0B72C6-CFC6-4B2D-8A89-1DE890D9F65B}',
	'HoleTable' : '{13A31354-BFF7-45CC-B749-2CE174780E77}',
	'HoleTableColumns' : '{A80294E5-6638-47F4-948A-A31A9F9CBC36}',
	'HoleTableColumn' : '{A2E47B01-25D6-4047-BC17-FA7F71B18599}',
	'HoleTableRows' : '{73886374-D415-4797-8E3A-A2CA9115D924}',
	'HoleTableRow' : '{E41AB38F-1708-4CAB-AA12-A29E5B3CE6FA}',
	'HoleTableCell' : '{E232F1FF-D6C3-421F-B650-AFAC768279D5}',
	'HoleTag' : '{CA779A92-76AD-4CD4-ACDB-7F06D73A089E}',
	'DrawingNotes' : '{3A4B5B27-8B78-4584-83B5-6A088C6B87FF}',
	'DrawingNote' : '{33A71A9E-0E21-4B70-A688-604C897D3A5A}',
	'GeneralNotes' : '{395CFC80-16C4-4289-A9F3-06E09E329D95}',
	'GeneralNote' : '{5C204B1E-BE7E-489A-A842-7A800A7CE348}',
	'UnitAttributes' : '{4B5F98A9-D670-4DDF-A7CE-8AFCEE0990CA}',
	'LeaderNotes' : '{08DCE0A8-28F0-4513-A655-010AD06BC874}',
	'LeaderNote' : '{04AAEAB9-6EAD-412C-B69A-D8EE4D924798}',
	'ChamferNotes' : '{E521F56F-13D5-4D80-95BA-10CB3B2F5918}',
	'ChamferNote' : '{C71B52F5-89E4-486C-B80E-8AC74650EB34}',
	'BendNotes' : '{206AFE1A-FAFA-4DAF-A569-1AF60672D63B}',
	'BendNote' : '{F5DA8C39-2BD7-4E77-BE94-81743E81ACC9}',
	'PunchNotes' : '{46D8F255-F1A2-4C52-8D4B-29C02C8198FF}',
	'PunchNote' : '{D23F0671-F983-4D09-8E5A-2BAB64BFB549}',
	'HoleThreadNotes' : '{DDB3F084-C3BC-4A46-8B6A-A169466514BF}',
	'HoleThreadNote' : '{C1516EB6-AEA2-412F-B1D0-9C609D152E21}',
	'DimensionText' : '{AEFA0FB8-139F-469C-8765-26AEA8C0A175}',
	'DrawingDimension' : '{63E2B412-8EDA-496C-BAF6-A28928F74091}',
	'DefaultBorder' : '{A907AEE3-A78F-11D5-8DF8-0010B541CAA8}',
	'SketchedSymbols' : '{A907AED9-A78F-11D5-8DF8-0010B541CAA8}',
	'SketchedSymbol' : '{A907AED5-A78F-11D5-8DF8-0010B541CAA8}',
	'SketchedSymbolDefinition' : '{A907AED3-A78F-11D5-8DF8-0010B541CAA8}',
	'AutoCADBlocks' : '{50DE4356-9814-490A-8932-18E72420930E}',
	'AutoCADBlock' : '{C7A9F576-7180-4DEE-BCC7-8E9DEABECEC4}',
	'AutoCADBlockDefinition' : '{C7131135-82E7-45EA-BB86-15DA083F6A04}',
	'FeatureControlFrames' : '{682CEB3B-365E-4863-B103-BCC368FBA896}',
	'FeatureControlFrame' : '{F3E768AB-B2BC-42B4-B95F-ED49BE550257}',
	'FeatureControlFrameRows' : '{4A558EB0-274A-4EF6-90A0-222A720A778E}',
	'FeatureControlFrameRow' : '{7CD6C780-663E-4187-8D35-D132C99F6918}',
	'SurfaceTextureSymbols' : '{F828B7C4-4B02-4B69-8D22-8BC7BA9D6243}',
	'SurfaceTextureSymbol' : '{7FF4B4DA-DF87-4E58-8727-ADEBA3B6452B}',
	'SurfaceTextureSymbolDefinition' : '{70E4E4A0-D090-41AF-8B0A-FFDB9F97B58B}',
	'DrawingDimensions' : '{FD30DCC9-A6E8-44B1-85B0-D7D8AE1580E5}',
	'GeneralDimensions' : '{A0F72CD2-B7A3-4EBA-9CDB-47F42BC74777}',
	'GeneralDimension' : '{EE21CD75-39FD-4683-BE24-BFBB9CA66EB4}',
	'GeneralDimensionsEnumerator' : '{294E366C-86B9-4CF7-9CF9-10D83787D2A6}',
	'LinearGeneralDimension' : '{B0E8CB6F-9451-4AFC-B8D3-A157ACDCBB0F}',
	'BaselineDimensionSet' : '{6FD094BA-90C4-4C9D-A3B9-DF3A398ECE26}',
	'ChainDimensionSet' : '{5BC0F92E-9C6A-4887-9B29-E1831F845DB2}',
	'AngularGeneralDimension' : '{5D81FF33-0E80-4FC7-A02B-D955952B2EC9}',
	'RadiusGeneralDimension' : '{8C1619BB-08F8-458D-B1B9-DEE4B63A3D07}',
	'DiameterGeneralDimension' : '{98D51E77-8775-4472-8AB0-50BCA8F56023}',
	'OrdinateDimensions' : '{EEB73D62-BB10-4FDA-84B2-B27521C833A1}',
	'OrdinateDimension' : '{3DA40E6A-7ED7-4B2C-A2E5-3FCE98B44077}',
	'OrdinateDimensionSet' : '{71BA345E-F3F9-49C9-917C-D7DFC284A07F}',
	'OrdinateDimensionsEnumerator' : '{A3788117-9A81-4D70-A8C8-C3FF3895E3D2}',
	'BaselineDimensionSets' : '{F2930064-7C6A-4FF7-8B87-D98EAC520AA1}',
	'OrdinateDimensionSets' : '{ACC86380-BE3B-48F1-A3D0-91E6ED2E2A82}',
	'ChainDimensionSets' : '{C9D63CDD-B82A-4CD9-82EB-CE937569197E}',
	'Centermarks' : '{0945D4EC-0E81-4062-8AC1-E4DE4BB8CBF9}',
	'Centermark' : '{37697A9E-01B1-4581-B52D-B8758FBA364E}',
	'Centerlines' : '{3DC9DC2A-8A78-43BE-BDB5-E6F1162980BB}',
	'Centerline' : '{05EC93C4-CC47-450C-A826-FEC6692AD526}',
	'Sheets' : '{206B59AF-22A6-11D4-B7A8-0060B0F159EF}',
	'SheetFormat' : '{1DF75C0E-591B-45B3-8233-37924B5019DB}',
	'AutoCADBlockDefinitionsEnumerator' : '{892AF496-C31A-431A-9B15-39FA10940A86}',
	'TextStyles' : '{A907AEBF-A78F-11D5-8DF8-0010B541CAA8}',
	'BorderDefinitions' : '{A907AEB1-A78F-11D5-8DF8-0010B541CAA8}',
	'TitleBlockDefinitions' : '{A907AEB5-A78F-11D5-8DF8-0010B541CAA8}',
	'SketchedSymbolDefinitions' : '{A907AED1-A78F-11D5-8DF8-0010B541CAA8}',
	'SketchedSymbolDefinitionLibraries' : '{A86A47DC-AAFE-4565-9E26-CBEEB2C1C8E5}',
	'SketchedSymbolDefinitionLibrary' : '{A4AE6207-A45C-4454-9CF6-867D56403BD1}',
	'LibraryFolders' : '{3E1A7894-35A3-41C3-9AF9-1E501AD1D747}',
	'LibraryFolder' : '{90602DB0-0BE4-48E2-864E-D853D3542959}',
	'LibrarySketchedSymbolDefinitions' : '{98E6F703-DF38-4C29-85A2-A8266869668E}',
	'LibrarySketchedSymbolDefinition' : '{3B1375EE-4B13-48AA-8A03-EDFDAEA85651}',
	'DrawingSettings' : '{E493FF48-3A9A-4A71-9C0D-27D79B3138C2}',
	'SketchSettings' : '{02BCE85C-478B-4A66-8668-6579602A0EB6}',
	'DrawingEventsObject' : '{27716230-E826-46E8-90FB-923D38D6F6F8}',
	'DrawingEventsSink' : '{FA561B14-D9E1-4ABD-B6E6-CC8A6A88B268}',
	'DisabledCommandList' : '{81710E0C-B8F1-4D04-BDDF-AC92C274CC81}',
	'ControlDefinition' : '{1ABBBF4A-8946-4A44-BFAE-F3200B41AA40}',
	'CommandManager' : '{9C88D3A9-C3EB-11D3-B79E-0060B0F159EF}',
	'InteractionEventsObject' : '{68D1E13F-F6A4-47FD-AAC0-5545A57B712B}',
	'InteractionEventsSink' : '{F1C0EFF2-5035-4DDD-8086-060590676024}',
	'SelectEventsObject' : '{21F3FEA8-2DF7-47B5-9C4C-33BB28E97D1C}',
	'SelectEventsSink' : '{2E19A8EE-1E70-4AE4-8C1E-06DAE3BBABB2}',
	'MouseEventsObject' : '{70B77812-4E3A-4499-8F8D-6AB6C6BDC5A5}',
	'MouseEventsSink' : '{C18BB14E-4FEF-478B-BF34-4690DE9BFC6C}',
	'PointInferenceEnumerator' : '{6886F155-F98E-4287-BF33-F63CB776B6B2}',
	'PointInference' : '{6886F154-F98E-4287-BF33-F63CB776B6B2}',
	'KeyboardEventsObject' : '{BD32F579-5C70-453E-BD6F-41D11EF640FD}',
	'KeyboardEventsSink' : '{AB510BBF-B893-47F7-ACC6-8F22836C5D8C}',
	'TriadEventsObject' : '{0466D05C-72BF-45E4-A1C6-3FA76AF8812C}',
	'TriadEventsSink' : '{5401A856-D03A-4418-AAA2-F1B677FA410D}',
	'ManipulatorEventsObject' : '{05E71BA9-6F04-4325-A3EA-1E2BEA94E4C2}',
	'ManipulatorEventsSink' : '{4DF6BEBE-5642-49CC-B365-BCC424F9C2F6}',
	'InteractionGraphics' : '{691AF5CB-83DC-4AF2-B689-F70AFB0D5020}',
	'MeasureEventsObject' : '{6AAD65B4-5F61-42C1-830A-A45C60809D76}',
	'MeasureEventsSink' : '{3C75ADFE-18C0-42BF-A83D-D0E539BD1F7D}',
	'MiniToolbarObject' : '{DBC99CB5-8EB0-4D45-BAC7-DE9D532FDD04}',
	'MiniToolbarSink' : '{B6B0211A-D77D-4D79-A529-7D8612C9A7A3}',
	'MiniToolbarControls' : '{79093216-BF48-46A2-9BFA-2D15CCB8BADD}',
	'MiniToolbarControl' : '{F4D9FAC9-D5F7-4FB5-8324-16CA73F349FF}',
	'MiniToolbarButtonObject' : '{F6A7B996-5EB9-4DC4-99D9-3919C36FB802}',
	'MiniToolbarButtonSink' : '{54D7BD09-6FA0-46F5-B427-F2432560A8C3}',
	'MiniToolbarCheckBoxObject' : '{3D7599FE-1A8A-47D8-A353-5C48B819A55D}',
	'MiniToolbarCheckBoxSink' : '{7DDF539F-7AFE-44BD-BAF9-BBAE51A93721}',
	'MiniToolbarDropdownObject' : '{7DF3C716-A1C7-4D3F-83C0-5D06A3D7F05C}',
	'MiniToolbarDropdownSink' : '{8AAC5924-81F8-4760-9BA0-3BD408FA7BA5}',
	'MiniToolbarListItem' : '{F22EBF2F-9F55-45FD-96DB-AABFBD40C177}',
	'MiniToolbarComboBoxObject' : '{F7844415-30E0-4507-8BC0-F8AF990B3B38}',
	'MiniToolbarComboBoxSink' : '{5A213EAD-8C62-4EE8-B99A-61A09F2F56E3}',
	'MiniToolbarValueEditorObject' : '{4E97BC3C-1235-44DE-8B31-571FA40955B5}',
	'MiniToolbarValueEditorSink' : '{334FE9E9-7C63-4924-8ADC-42DB57B7B688}',
	'MiniToolbarSliderObject' : '{6299A1B5-4F87-4209-B024-B002D3438E61}',
	'MiniToolbarSliderSink' : '{2F9E3271-4E14-4B76-9581-602AED994066}',
	'MiniToolbarTextEditorObject' : '{AAC6E2B5-64B0-440C-A5A2-2AED0D4D7191}',
	'MiniToolbarTextEditorSink' : '{32F5072E-8F1B-4889-898F-A512619D7D74}',
	'MiniToolbarTextBoxObject' : '{7E765E87-446D-451C-9B54-F9714B157BE9}',
	'MiniToolbarTextBoxSink' : '{C3DB869D-CA34-4269-BAEC-BB08F8FD7CB3}',
	'UserInputEventsObject' : '{2772058F-17D8-4969-8D46-51860F09AC9B}',
	'UserInputEventsSink' : '{711F30CD-A00B-4015-93A8-397EC8F5A284}',
	'CommandBar' : '{EF0F253F-6AF9-40A8-BD13-B136E00B6588}',
	'CommandBarControls' : '{67B1BC45-4518-4DB9-A5D3-C0364374BB80}',
	'CommandBarControl' : '{4BF433DE-1B2F-4ADE-B71C-0C826CF2CC88}',
	'ButtonDefinitionObject' : '{DBADC913-8652-4B4E-B13E-B356CC4E9BEE}',
	'ButtonDefinitionSink' : '{9B5D2EC6-A4BD-4B3A-8A34-069EE52B009D}',
	'ControlDefinitionEventsObject' : '{4CF7D720-1E41-4049-8C1A-70C980D11667}',
	'ControlDefinitionEventsSink' : '{AB5EF2D1-EAEB-4A4A-A86B-24BF0F2111BD}',
	'ProgressiveToolTip' : '{5189E676-CC1A-4901-98E7-EC85130FDB63}',
	'MacroControlDefinition' : '{2F800161-0E4D-4953-A0B7-E55EE05E039B}',
	'ComboBoxDefinitionObject' : '{91B9E6B9-B526-45A8-A7FD-0D2FFD1D6EF5}',
	'ComboBoxDefinitionSink' : '{ACC63CB3-EBF2-48E3-A0F4-48E3FC13ECED}',
	'RadialMarkingMenu' : '{828DB6DB-AE56-4DB4-A765-216D9159A18C}',
	'CommandControls' : '{DE07F599-C9C0-4843-8EFE-D5083EBEFB1D}',
	'CommandControl' : '{E0519C23-A426-4FA3-BB30-AC5FBEAD137E}',
	'CommandCategories' : '{AE2CB260-129A-494C-9F8C-AD8140271E8A}',
	'CommandCategory' : '{6B821DA7-B56B-44FC-859F-4DABA658C6E2}',
	'ControlDefinitions' : '{B9D982C4-3FFF-4796-AD6D-C6D1F16D7BA9}',
	'DragContext' : '{FA403DAE-32E0-4C17-BB7C-CD3626A9BFA9}',
	'EnvironmentManager' : '{2F5EC0C5-5335-4677-BB14-5621C1140D1B}',
	'Environment' : '{4E27C06E-4D6A-4E53-9F84-32A0643623CF}',
	'CommandBarList' : '{16EF0082-3213-4E37-AF75-5CB2BF738741}',
	'PanelBarObject' : '{C2FEB1BC-115B-443B-A18C-F88B2FCBB7BA}',
	'PanelBarEventsSink' : '{30A44C19-C3F4-483B-8835-A0A13B849AC0}',
	'Ribbon' : '{3AB23287-16A5-4B3B-964B-00C27869CD23}',
	'UserInterfaceManager' : '{3AF77BAF-EECD-4301-823D-9B604FE5C176}',
	'CommandBars' : '{6364B6D5-2994-46A5-8F53-03F63958B056}',
	'EnvironmentList' : '{A1C8AD17-F4C3-4424-982C-9D628A5A4ECA}',
	'Environments' : '{D23D422B-C248-4EA4-98AF-9E6390C99964}',
	'UserInterfaceEventsObject' : '{4B01DD28-A1AF-4387-9F24-2B87442C1E94}',
	'UserInterfaceEventsSink' : '{9BC9A7EC-A0AD-433B-BB3C-9AC30C9030E4}',
	'Ribbons' : '{4AA83B95-08F8-4415-9397-4BB5E8103290}',
	'CommandControlsEnumerator' : '{B32BC09F-4DC6-4655-A457-8B7E8934CAAA}',
	'DockableWindows' : '{FE97EF73-E784-47FB-AA0B-D1891A8F1DF4}',
	'DockableWindow' : '{3A32960B-A64E-4257-B24F-240C7E68C065}',
	'DockableWindowsEventsObject' : '{32958A3F-CEA1-4390-946D-3D2F2E92675B}',
	'DockableWindowsEventsSink' : '{863F993F-413C-4965-B391-CE4CF47616DB}',
	'WebBrowserDockableWindow' : '{1A88CE14-0590-4C13-B58A-C9B7FA1458C5}',
	'BalloonTips' : '{176AA199-DDEA-4CA9-B7EC-0437918DF800}',
	'BalloonTipObject' : '{BDAFC08A-5CAC-4E5A-B715-F2BCAFFD5282}',
	'BalloonTipSink' : '{321398AC-E78C-43DF-B1A6-5BE90C133680}',
	'RibbonTabs' : '{1CE97D79-6535-4D0F-9A51-57734766BEDC}',
	'RibbonTab' : '{734FDACC-45FD-487A-AC60-02CE0522FF00}',
	'RibbonPanels' : '{7693ED6C-807E-443A-A3C0-A63010E5625A}',
	'RibbonPanel' : '{916EFE1C-6493-4712-92D7-CD789914321A}',
	'RadialMarkingMenus' : '{228EA2B9-974A-48DF-8E17-7EAE50A79AFD}',
	'GenericObject' : '{32E4A31B-C5E8-11D2-B77F-0060B0F159EF}',
	'SheetSettings' : '{EF8803D3-9ADF-4B81-9097-6529ED782861}',
	'SheetFormats' : '{6AC3D773-1202-450D-9CD2-3557B1395C64}',
	'DrawingBOMs' : '{68517DF3-9E1D-44AA-B12D-08880086D61A}',
	'AutoCADBlockDefinitions' : '{FC290B65-544A-4F65-B812-092CB93AA421}',
	'Parameters' : '{528C9A32-4173-420A-AD05-B6FBF8382212}',
	'ModelParameters' : '{652F6A52-8B8A-4CEF-B1DC-C78751914993}',
	'ModelParameter' : '{916D7FDB-CFE6-4FB1-8921-694DC9CD2793}',
	'ReferenceParameter' : '{12959B9F-4EF1-4834-83C1-7950F2321878}',
	'UserParameter' : '{8510D6EA-9A97-4CC9-A2A8-221FFC610AB4}',
	'ReferenceParameters' : '{1304BB1D-95AE-4738-80F8-CCCA1ABCFF6B}',
	'UserParameters' : '{2FF370FA-BB1C-4C92-BB10-06D94CC8F8F3}',
	'ParameterTables' : '{53D15C9C-4920-4B58-8804-8567A94D1643}',
	'ParameterTable' : '{5250C13F-196F-442E-86E8-68C87B75CABE}',
	'TableParameters' : '{0E4C2356-1844-43F1-BAFA-45AA948EDAD8}',
	'TableParameter' : '{B1F0562A-BC71-44E3-89B6-5583BB50CD09}',
	'CustomParameterGroups' : '{ADE1D7A7-3CF2-49E7-8476-79677765D850}',
	'CustomParameterGroup' : '{81342C4A-E898-4566-AA9B-735E88874E56}',
	'DerivedParameterTables' : '{321D3FD9-A57F-4CDE-AD39-FD1EEE22543C}',
	'DerivedParameterTable' : '{B9831DEF-A198-48C1-8023-F5F05E55B092}',
	'DerivedParameters' : '{D4C98D93-FA6C-4602-8EB8-2709938BFE74}',
	'DerivedParameter' : '{0BDE54D4-8527-46BE-B2DC-7E9A5AED8AB9}',
	'TextStylesEnumerator' : '{D4AAD36D-D0D1-4BFC-9C3A-C4718D3D9209}',
	'ObjectDefaultsStylesEnumerator' : '{062F6086-60DC-4550-93C5-A9B8CEA89ADB}',
	'LayersEnumerator' : '{1010554D-5E7D-4D43-A381-89B57B51A708}',
	'Styles' : '{3CF51EB9-B426-482F-98B0-8CE17BDCDEED}',
	'LeaderStylesEnumerator' : '{9BAC756F-6695-4C8B-A25C-16D29002F114}',
	'BalloonStylesEnumerator' : '{7D85BA17-75C5-4EBE-AA18-F7E60AE25733}',
	'FeatureControlFrameStylesEnumerator' : '{852C83B9-26EC-4FDA-89D5-E031523AEE01}',
	'SurfaceTextureStylesEnumerator' : '{1DCB7001-C7CD-4637-AC67-296CEB47A86B}',
	'HoleTableStylesEnumerator' : '{1FA42157-89A8-4DA0-A943-888BF014E072}',
	'CentermarkStylesEnumerator' : '{8E9F0865-0AE2-4AAC-8E67-0CED8434114C}',
	'PartsListStylesEnumerator' : '{F829B171-412E-4642-8034-AEC013FCFDC5}',
	'RevisionTableStylesEnumerator' : '{50C3C4B3-5029-44E8-BF12-C1D09530CCF5}',
	'TableStylesEnumerator' : '{E0B90B3E-0907-49B2-8E51-438C950F3A4B}',
	'CollinearConstraint' : '{8006A076-ECC4-11D4-8DE9-0010B541CAA8}',
	'ConcentricConstraint' : '{8006A078-ECC4-11D4-8DE9-0010B541CAA8}',
	'EqualLengthConstraint' : '{8006A07E-ECC4-11D4-8DE9-0010B541CAA8}',
	'EqualRadiusConstraint' : '{8006A080-ECC4-11D4-8DE9-0010B541CAA8}',
	'GroundConstraint' : '{8006A082-ECC4-11D4-8DE9-0010B541CAA8}',
	'HorizontalConstraint' : '{8006A084-ECC4-11D4-8DE9-0010B541CAA8}',
	'HorizontalAlignConstraint' : '{8006A086-ECC4-11D4-8DE9-0010B541CAA8}',
	'MidpointConstraint' : '{8006A088-ECC4-11D4-8DE9-0010B541CAA8}',
	'ParallelConstraint' : '{8006A08A-ECC4-11D4-8DE9-0010B541CAA8}',
	'PerpendicularConstraint' : '{8006A08C-ECC4-11D4-8DE9-0010B541CAA8}',
	'SymmetryConstraint' : '{8006A08E-ECC4-11D4-8DE9-0010B541CAA8}',
	'TangentSketchConstraint' : '{8006A090-ECC4-11D4-8DE9-0010B541CAA8}',
	'VerticalConstraint' : '{8006A092-ECC4-11D4-8DE9-0010B541CAA8}',
	'VerticalAlignConstraint' : '{8006A094-ECC4-11D4-8DE9-0010B541CAA8}',
	'SmoothConstraint' : '{8FFF6DFE-F659-4C77-81E5-DD9B70A37D90}',
	'Sketch3D' : '{E4C09561-E779-4A00-A835-E8D43E08A290}',
	'SketchEntity3D' : '{FD1878BB-56AD-44CD-9186-11BC84E584A4}',
	'SketchConstraints3DEnumerator' : '{85C83167-947D-46E2-A802-92D529B48E37}',
	'SketchEntities3DEnumerator' : '{6CBA9E79-C13B-46ED-BB14-6541A63B1A16}',
	'Profiles3D' : '{B1340A33-EB0D-4609-BA1E-B98A3D173794}',
	'Profile3D' : '{2A8678EA-A024-469A-80DC-D1EAD67847A3}',
	'ProfilePath3D' : '{D7347916-69D8-4972-AEBE-95BE5672BED2}',
	'ProfileEntity3D' : '{142C71BE-1254-4947-9192-382BCC511F46}',
	'SketchPoint3D' : '{2307500B-D075-4F5D-815D-7A1B8E90B20C}',
	'SketchArcs3D' : '{4AF3870E-AB8B-4567-94B5-C1850D292111}',
	'SketchArc3D' : '{6129AB00-E4D1-45AD-B3AE-A873BDF452BF}',
	'SketchLine3D' : '{87056D9A-B0B2-4BD0-A6EC-51E9D893A502}',
	'SketchLines3D' : '{3A62D311-C21A-4DD3-83C0-A23507CA385E}',
	'SketchPoints3D' : '{3BCDEC54-2F73-4114-A7CB-ACF5E823B67D}',
	'SketchCircles3D' : '{FA48B024-CC3B-458F-B0EB-6FE4CBEC35DD}',
	'SketchCircle3D' : '{8D562D7A-4F0B-4EC8-8737-47DD28FB7323}',
	'SketchEllipses3D' : '{7A7BD889-E944-41FC-A34F-474465F0894E}',
	'SketchEllipse3D' : '{8F014D19-4B2F-4DD1-9010-FE75815C297C}',
	'SketchEllipticalArcs3D' : '{08C74C78-5F8D-40B3-9D57-4507D5CEA79C}',
	'SketchEllipticalArc3D' : '{C3CB1896-B26C-4862-8652-5208013D95A7}',
	'SketchSplines3D' : '{611271CA-48EE-4EBF-9ACD-CCD081142400}',
	'SketchSpline3D' : '{61FC7221-543B-4885-9546-B700267C98D1}',
	'SketchSplineHandle3D' : '{5DBD70FD-AB80-4074-B105-EB28F2CB397A}',
	'GeometricConstraints3D' : '{85A24FF2-F0E9-4BC4-9A69-34F8C683B41A}',
	'GeometricConstraint3D' : '{0DE9D15F-7E51-4861-BD72-050A86BA17AD}',
	'TangentConstraint3D' : '{0456FF0D-196E-4C72-989D-D86E3DD32955}',
	'CollinearConstraint3D' : '{E8BE2118-716C-40FD-8BC0-2517B253E4F9}',
	'GroundConstraint3D' : '{38876920-588A-4F80-A4B1-1F2E3562FB19}',
	'ParallelConstraint3D' : '{73919DC1-220E-4EC9-B716-072D6046A3AD}',
	'PerpendicularConstraint3D' : '{2035E584-09E7-4B18-9698-014DEF44B10E}',
	'CustomConstraint3D' : '{8E02BFEC-2C95-4685-83B8-E215F98BA844}',
	'SmoothConstraint3D' : '{281176E3-4EDC-4F4E-9804-6716B7B9059D}',
	'CoincidentConstraint3D' : '{843FEEB5-A0EF-4C5B-8939-4F9B574119D8}',
	'WorkPoint' : '{28DD48C9-8D70-11D4-8DDE-0010B541CAA8}',
	'MidpointConstraint3D' : '{4FAB4F91-4998-4B1C-9717-8CDF1BD7377E}',
	'ParallelToXAxisConstraint3D' : '{8675C60E-CE43-4722-AB95-C41479862B66}',
	'ParallelToYAxisConstraint3D' : '{76FE6138-9B22-40E6-AE41-98AE40609A45}',
	'ParallelToZAxisConstraint3D' : '{50FB8693-BA00-47C5-BD0B-D03F1B545354}',
	'ParallelToXYPlaneConstraint3D' : '{879211BF-E1DA-4EC6-BB14-35A030C132E7}',
	'ParallelToYZPlaneConstraint3D' : '{35BB39D2-FBCF-4780-BC9C-6CF50B268EED}',
	'ParallelToXZPlaneConstraint3D' : '{005E9B5E-B6E5-4670-97C6-0A6EA4B6CE2D}',
	'EqualConstraint3D' : '{0C797F20-90F4-42F3-89B2-786880D1883A}',
	'OnFaceConstraint3D' : '{93E69636-D11D-4044-BAC8-CD1DE3E6BC1E}',
	'SketchFixedSplines3D' : '{80DBF4D7-FEC3-454C-BF1C-65BCDB27188C}',
	'SketchFixedSpline3D' : '{7A5B2F53-5756-4261-B6F1-4B5C3CDE1226}',
	'SilhouetteCurves' : '{B4F71C8B-BC8D-47F1-A327-9275F5FB443D}',
	'SilhouetteCurve' : '{F9CB0F15-28B0-4D98-A658-F906D8B0D965}',
	'DimensionConstraints3D' : '{3C934EFD-E26A-4940-BA5A-66908C16AA92}',
	'DimensionConstraint3D' : '{460D3833-0485-4B61-8A1A-C9E8008FAFCC}',
	'TwoLineAngleDimConstraint3D' : '{1EA98FE3-C2EA-4025-8B42-7F91BD2E8DFC}',
	'PointAndPlaneDistanceDimConstraint3D' : '{39930637-A840-4819-AB86-EFE9CCB21BD1}',
	'TwoPointDistanceDimConstraint3D' : '{C124F1E0-1B29-481D-A0CB-BA8A8AB69764}',
	'LineLengthDimConstraint3D' : '{04A196FD-3FBB-43EF-9A79-2735B3B99214}',
	'RadiusDimConstraint3D' : '{90943B1A-D344-4227-8219-D1C6090697BB}',
	'SplineLengthDimConstraint3D' : '{E045F7F0-7E93-4212-AA63-5F77EECB5625}',
	'SketchControlPointSplines3D' : '{745A04C4-8445-412A-AFA7-33E778DA3059}',
	'SketchControlPointSpline3D' : '{A4126F98-E952-4997-BD2D-209D4788F70F}',
	'SketchEquationCurves3D' : '{01BAC9F1-F900-4E57-9FDB-F12232AEC9D2}',
	'SketchEquationCurve3D' : '{67863AC3-95B7-4386-8A51-449E44AC2FBC}',
	'IntersectionCurves' : '{9F672C49-E28B-4239-8F7B-BF3FA7FD5071}',
	'IntersectionCurve' : '{25FF655F-9C78-4C55-9166-51E299DB6565}',
	'OnFaceCurves' : '{A5620F8C-EEF1-4BD5-8C45-2C2327EFD42F}',
	'OnFaceCurve' : '{173A0AA0-589E-4DC0-BDA9-8F5F10F8AF72}',
	'HelicalCurves' : '{B88938D1-2BE1-42D5-BD17-B4A7498C1B60}',
	'HelicalCurve' : '{314DEB20-A0E9-4F72-8C44-D9B28D2CA3E7}',
	'HelicalCurveDefinition' : '{C726DA3F-7695-4786-BB9E-EFF55388C855}',
	'HelicalCurveConstantShapeDefinition' : '{111D8480-B19C-449F-84A8-3541A6B62253}',
	'HelicalCurveVariableShapeDefinition' : '{597DC0FA-350A-418D-B183-450AB1FB041E}',
	'HelicalCurveShapeDefinitionRows' : '{40AA25E1-641B-4765-9904-65F26FA457FF}',
	'HelicalCurveShapeDefinitionRow' : '{2E61B5D9-3348-452C-8444-593CFD702693}',
	'StyleEventsObject' : '{221D9E13-D105-485A-B538-1E3FB7250A71}',
	'StyleEventsSink' : '{A52071CF-BF9F-45BA-A7D5-E5AAA2682B4D}',
	'RepresentationEventsObject' : '{FB4D47B9-777E-49C5-99CB-9CE5C345D66E}',
	'RepresentationEventsSink' : '{AFD8E323-2B44-4657-89F2-4C50233D287A}',
	'AssemblyDocument' : '{29F0D465-C114-11D2-B77F-0060B0F159EF}',
	'ModelingSettings' : '{81F414A9-1062-46BB-A5EE-26575E90DCF0}',
	'UserCoordinateSystemSettings' : '{42E1EF4D-7D8F-49EA-95A4-B4661D4983AA}',
	'Materials' : '{C45BCCBE-2E53-4C8F-B76A-E6B7815E87E4}',
	'Material' : '{57CFD4EC-1776-48D3-B5C4-7B6E015D0541}',
	'LightingStyle' : '{9DACF05E-4734-4D7E-986A-EE320F8A85C7}',
	'Lights' : '{9F512CF6-D755-4539-A0A5-E346F4B89AE1}',
	'Light' : '{755B3C6B-3A92-4702-96AC-686382A91278}',
	'LightingStyles' : '{A5B827BD-83C7-4CCA-8DCA-06CD10C2237E}',
	'ObjectVisibility' : '{1B73EA84-1B63-4F24-B295-B50EA9215C26}',
	'AssemblyComponentDefinitions' : '{575F2831-2B6A-11D4-B7A8-0060B0F159EF}',
	'DisplaySettings' : '{F2780C41-65D5-43E1-A259-E05D08ED1659}',
	'GroundPlaneSettings' : '{A12C6DFA-6381-41A2-9037-13AFE5B1EFBD}',
	'Assets' : '{7289A75E-C37E-468C-904F-B2BADC61F272}',
	'OGSSceneNode' : '{BED3CF92-D335-4DC0-BA98-76F2E8A6A963}',
	'OGSRenderItemsEnumerator' : '{1915251D-AC20-4EFC-A0EE-43FBEF266925}',
	'OGSRenderItem' : '{429D036C-4F9D-4F72-9F77-AB5789FCC6E9}',
	'OGSSceneNodesEnumerator' : '{E8DC5B4C-F562-4911-AFBC-41961F55C140}',
	'DesignViewRepresentation' : '{4E1C27BA-D992-411F-9DE2-BD630285E4B3}',
	'RepresentationsManager' : '{B25D15A6-B823-42FF-9ABB-781A3043ECB0}',
	'PositionalRepresentations' : '{1154D44F-DED2-4457-B862-8631D4D69FC6}',
	'PositionalRepresentation' : '{DD22F707-6FC9-481B-A3FD-44FDA2D695A2}',
	'AssemblyConstraint' : '{AA044AA2-D685-11D3-B7A0-0060B0F159EF}',
	'iMateResult' : '{6D634B29-2066-44CA-AA97-D87A2C95A172}',
	'AssemblyConstraintsEnumerator' : '{56C3574C-13A4-46AB-B981-4B45784B2156}',
	'iMateResultsEnumerator' : '{359AC6D9-E239-4825-BA81-DD8E433FBD1E}',
	'iMateDefinition' : '{928894AE-2111-43EB-B77C-4E1A7388CD75}',
	'LayoutConstraint' : '{EB7E9B67-F77A-4ACE-A3CB-1D5C93F7EE9D}',
	'FlushConstraint' : '{AC581AF3-E3C8-4011-9140-3B64D555FA05}',
	'AngleConstraint' : '{9048CE40-F6A5-422D-A816-CBE5E03B28D6}',
	'CustomConstraint' : '{929723D9-517D-4405-A5B5-263E3B02C6C4}',
	'InsertConstraint' : '{0AEBFB16-385B-4663-B17C-D07F576F2C70}',
	'MateConstraint' : '{CEFDC141-B989-4BF3-BDD7-8308D8089FFE}',
	'RotateRotateConstraint' : '{F8F30CD3-A44B-4C8A-B9D2-287361B0BD26}',
	'RotateTranslateConstraint' : '{31737D0F-56F3-40B8-8649-C8A5AB945D80}',
	'TangentConstraint' : '{0A73D068-AC6B-4B51-8B6D-913B90A77741}',
	'TransitionalConstraint' : '{3CBE8AAD-3D92-11D5-8DEE-0010B541CAA8}',
	'DriveConstraintSettingsObject' : '{C3F06C8B-B0EA-4EC3-9922-1657009774D3}',
	'DriveConstraintSettingsSink' : '{ED68898D-4062-47D4-AC28-9B8A1F38CE90}',
	'DriveSettingsObject' : '{F8FEB6D6-1D1A-4472-9429-1FF06A76DB9E}',
	'DriveSettingsSink' : '{0F13E8B9-A4C2-4477-93CA-FC2CD0D2C1B1}',
	'AssemblySymmetryConstraint' : '{BA9EC28C-765B-4481-8A8C-20489290B35E}',
	'ConstraintLimits' : '{8112A2AA-0017-4029-81A5-9C18F5E37E92}',
	'RectangularOccurrencePattern' : '{A8E2C150-78E9-4E97-A4A0-BF43936B2A45}',
	'OccurrencePatternElements' : '{CDF65ADD-9C11-4AB9-8F2E-AB6F83FED7C2}',
	'OccurrencePattern' : '{09A5CE88-D529-499E-82EF-246D8DC4F5B3}',
	'OccurrencePatternElement' : '{6ABB8219-4962-11D5-8DEE-0010B541CAA8}',
	'CircularOccurrencePattern' : '{6F9AAB22-31DC-4F5A-98ED-8A8693D5BD1C}',
	'LevelOfDetailRepresentations' : '{B7B652AD-7411-429D-92AC-663F9183F7F6}',
	'LevelOfDetailRepresentation' : '{F24F9821-0EE5-4157-A555-45B97DE14D6D}',
	'DesignViewRepresentations' : '{C6A2B48C-DBBC-4BA9-A98B-6EB63FB78AE4}',
	'AssemblyEventsObject' : '{5F08DCB5-FE15-4511-9A2E-A3FB10968F2A}',
	'AssemblyEventsSink' : '{BABF5BBF-9878-11D4-8DE2-0010B541CAA8}',
	'_AssemblySolver' : '{92E914D0-9FEA-11D6-8E0B-0010B541CAA8}',
	'_AssemblySolverNodeObject' : '{92E91440-9FEA-11D6-8E0B-0010B541CAA8}',
	'_AssemblySolverNodeSink' : '{92E914A0-9FEA-11D6-8E0B-0010B541CAA8}',
	'PublicationEventsObject' : '{560F650A-7084-466C-8308-F14F854D677F}',
	'PublicationEventsSink' : '{B1DC30D1-7C5F-41F2-A1D9-5D7D4C76C9CA}',
	'PresentationDocument' : '{29F0D46C-C114-11D2-B77F-0060B0F159EF}',
	'PresentationExplodedViews' : '{941D7D22-4C65-4E96-B446-086CD1B94572}',
	'PresentationExplodedView' : '{1F917159-C90E-4746-A4E3-E543894ADFD3}',
	'TrailsEnumerator' : '{F30319D0-9C9E-40BC-96AC-62D2E9302E5B}',
	'Trail' : '{0AD2B1BB-3410-4A43-9926-C3849F69FD2F}',
	'TrailSegment' : '{8D039683-92D8-4F9E-995C-1FDF01AA16D0}',
	'PresentationTasks' : '{32705861-0597-4BAA-A445-5846AF71C3B7}',
	'PresentationTask' : '{AED640A3-73BD-4F63-B15D-FD6D71529BAB}',
	'PresentationSequences' : '{67C4F7E6-7B96-4837-8DD1-B4A6A78FF810}',
	'PresentationSequence' : '{51CBB633-D1B6-4575-A028-085C4A270C27}',
	'PublicationComponentsEnumerator' : '{0C8FA54F-425F-4F29-8DD8-4EA0D1CBF23E}',
	'PublicationComponent' : '{D7EF5F2C-9214-426A-BC93-3DCE96FC6573}',
	'Publication' : '{B70FB526-7ED8-4345-B5BE-B7DFB062394C}',
	'PublicationComponents' : '{9FC0A05F-E541-4E76-ADD5-AD36E875A620}',
	'Storyboard' : '{539C3AFE-A915-4086-B2B6-1133E4DC4E51}',
	'PublicationTweaks' : '{31B59E93-AB77-4236-9F8B-781B150CD754}',
	'PublicationTweak' : '{87A90F35-C48D-4BBB-A865-5EBBC267CBC3}',
	'PublicationTweakDefinition' : '{0AA9C1C0-0182-4E85-9A61-B5410F35EA4C}',
	'PublicationTrailSegmentsEnumerator' : '{91CF45CD-E5CD-47DF-B7AA-ECCA91DC4FA0}',
	'PublicationTrailSegment' : '{98BDC540-5F67-4A23-87E8-EC2072999157}',
	'PublicationTrail' : '{0D1F1D70-2997-462D-90A0-61C5D5E97C85}',
	'PublicationTrailSegments' : '{86128260-22B9-4841-92C2-977F78B39A96}',
	'PublicationTweakPath' : '{A13F8CA8-B7C1-4459-9E89-E5D890336737}',
	'PublicationTweakPaths' : '{7EDBE5DA-6A04-4AF6-B891-6A6139147197}',
	'PublicationTrails' : '{8EB31EAC-43A6-429E-A06C-7CDC128B4996}',
	'Storyboards' : '{3DD94016-2767-47B0-A331-117EA621C088}',
	'PublicationMarkedViews' : '{66C9BA8B-1A75-4A21-BF84-EA4D26E89010}',
	'PublicationMarkedView' : '{35D84E9C-ABB8-49CE-831D-62BBC8B0594A}',
	'PublicationBodiesEnumerator' : '{4762B21E-A04D-4479-BCF3-1B105A126455}',
	'PublicationBody' : '{54167F8A-A119-41FD-8B5C-895257D45E2C}',
	'PublicationEdgesEnumerator' : '{A8EAF4E3-FD98-4E26-9B99-D7B9D97961FD}',
	'PublicationEdge' : '{A093F915-6F3B-41C5-A3A6-7943A498DF78}',
	'PublicationFacesEnumerator' : '{0EF5B3D1-E19B-423A-BFD8-102D7C0F4A0C}',
	'PublicationFace' : '{87C8148C-FB68-4E5C-B79A-7648BAC75886}',
	'PublicationFaceShell' : '{41BECC60-689A-455E-8637-991E384C1C96}',
	'PublicationVerticesEnumerator' : '{D88680AD-1C6E-4C6B-B946-CB1FC8849DDF}',
	'PublicationVertex' : '{F9F9CB96-EF02-45D5-A8D1-62EDFE3C9F99}',
	'PublicationFaceShellsEnumerator' : '{7DB211BE-6367-4245-97F2-4B30F4A79E13}',
	'MeshFeatureSets' : '{D6DB0745-4B18-4A22-8F03-DD12B0D444E0}',
	'MeshFeatureSet' : '{8728FC5B-20DF-43CC-A845-F2BFA49163A1}',
	'MeshFeature' : '{D2EB4CB2-4FC9-4E83-A9BE-71D86E1D5752}',
	'MeshFeatureEntitiesEnumerator' : '{5F093D38-605F-42A2-B2D3-38E4A16353F1}',
	'MeshFeatureEntity' : '{0466F7FE-1603-4F35-882C-B0B27E17E976}',
	'PresentationTweaks' : '{EB674FEC-0328-44DB-A763-E58F97EDD8DC}',
	'PresentationTweak' : '{354F622F-BDFB-4010-A276-46F0EA99AD16}',
	'TrailSegmentsEnumerator' : '{9F579B5F-27B6-4F2A-A08B-40231EB645D3}',
	'Publications' : '{965DB171-5349-455E-8C19-3789DD189792}',
	'PresentationEventsObject' : '{EF6287D1-E4BF-4978-A5AF-CBCA47EB56E6}',
	'PresentationEventsSink' : '{4C1CBCCC-487C-48ED-9AB6-7411B020A58E}',
	'PresentationScenes' : '{B59644DA-CE64-4FAF-BAC6-A064AD00AE41}',
	'PresentationScene' : '{C9C41EF2-150B-4B55-8949-0A860D91245C}',
	'PresentationSnapshotView' : '{3851834F-2FC9-4D4A-8739-0C2DB105C795}',
	'PresentationTrails' : '{B2EFCD07-8F2C-47FB-93D1-22645ECD280C}',
	'PresentationTrail' : '{C56AC462-1A94-41D4-90C6-AD796A778986}',
	'PresentationComponent' : '{431E59F3-872A-4293-891B-9B637BB454A0}',
	'PresentationMeshFeatureSetsEnumerator' : '{00BC5CE8-F355-421B-82AD-B6DFA428156B}',
	'PresentationMeshFeatureSet' : '{121AEDEB-A983-4AA9-9F88-81DEC638DCFB}',
	'PresentationMeshFeature' : '{29302798-B225-447C-B37B-300DC28B888C}',
	'PresentationMeshFeatureEntitiesEnumerator' : '{AC89451E-1B5B-4E2F-9E94-0050F94041A4}',
	'PresentationMeshFeatureEntity' : '{B7635E1F-FF33-424A-B121-4CAC9EBDA9E2}',
	'PresentationBodiesEnumerator' : '{6F61D701-A0B1-4E74-97A5-9B3F7ABA36BC}',
	'PresentationBody' : '{297560D3-0E33-4208-B903-96C1C5FE181E}',
	'PresentationEdgesEnumerator' : '{C1C31BE3-445F-403A-927B-54840EA62012}',
	'PresentationEdge' : '{59EE8744-CA2F-4E38-B19A-D99EAACE0219}',
	'PresentationFacesEnumerator' : '{05C7DEC5-9B50-4AA8-9263-7A8AA35F1834}',
	'PresentationFace' : '{BF527E81-1757-417B-BAA1-F50ED7F40A8F}',
	'PresentationVerticesEnumerator' : '{6A2E6CA4-4138-4FD7-9843-7EBCEC07126D}',
	'PresentationVertex' : '{DBC6E00A-9233-4A04-BA1E-EFD6C476F9FB}',
	'PresentationComponentsEnumerator' : '{1AD88D7E-9F07-4657-9410-9AF1E0A734F6}',
	'PresentationTrailSegments' : '{88666A4B-DC8F-48A2-8748-CB345ABC0B0D}',
	'PresentationTrailSegment' : '{B35A4214-030A-44C2-8618-E94A05543B23}',
	'PresentationSnapshotViews' : '{12162DC0-9513-405B-8882-8CEDE4CC78C2}',
	'FileAccessEventsObject' : '{3D67DF18-9BC6-4470-A9E3-C820CB4E821C}',
	'FileAccessEventsSink' : '{E51041E7-5DB6-4951-9F76-3ACA9B2E2A66}',
	'ObjectsEnumeratorByVariant' : '{9235396B-0350-11D3-B787-0060B0F159EF}',
	'ApplicationAddIns' : '{A0481EEA-2031-11D3-B78D-0060B0F159EF}',
	'ApplicationAddIn' : '{A0481EEB-2031-11D3-B78D-0060B0F159EF}',
	'FileLocations' : '{0BF73FD9-1253-11D3-B789-0060B0F159EF}',
	'TransactionManager' : '{AE277672-2FDC-11D3-B78F-0060B0F159EF}',
	'TransactionsEnumerator' : '{AE277673-2FDC-11D3-B78F-0060B0F159EF}',
	'Transaction' : '{AE277674-2FDC-11D3-B78F-0060B0F159EF}',
	'CheckPointsEnumerator' : '{68E4EA6F-3BEA-4F89-9335-F46CDF1AB005}',
	'CheckPoint' : '{B0955199-1373-4868-9B86-4ABB2DC2A684}',
	'TransactionEventsObject' : '{ABD216FA-7559-4883-93D7-C0A9ECFF19C4}',
	'TransactionEventsSink' : '{BA8CE4E1-3FC3-414C-A73A-26BDB38ECE70}',
	'ChangeManager' : '{D70C53E3-58A6-48CA-95D2-AF6F4AAD04EA}',
	'ChangeDefinitions' : '{9ACB775D-8E1E-4A38-9121-7E1467526860}',
	'ChangeDefinitionObject' : '{4F8D5D47-63F7-4690-A06D-54D7311A2566}',
	'ChangeDefinitionSink' : '{48DDBD08-5630-4D9A-A71F-8F623A3ABB47}',
	'ChangeProcessorObject' : '{62246192-FF8D-4715-997D-09E760061B5C}',
	'ChangeProcessorSink' : '{5BAB1E1A-F66B-4021-A008-A16E939CA863}',
	'TransientGeometry' : '{97ECB3AE-6C6E-4D8A-A91E-564314494EB8}',
	'Line2d' : '{CB69F179-558E-11D3-B793-0060B0F159EF}',
	'Cylinder' : '{5DF860A2-6B16-11D3-B794-0060B0F159EF}',
	'EllipticalCylinder' : '{FA34A401-F063-11D3-B7A2-0060B0F159EF}',
	'Cone' : '{5DF860A3-6B16-11D3-B794-0060B0F159EF}',
	'EllipticalCone' : '{FA34A402-F063-11D3-B7A2-0060B0F159EF}',
	'Sphere' : '{5DF860A5-6B16-11D3-B794-0060B0F159EF}',
	'Torus' : '{5DF860A4-6B16-11D3-B794-0060B0F159EF}',
	'BSplineSurface' : '{5DF860A6-6B16-11D3-B794-0060B0F159EF}',
	'BSplineCurve2dDefinition' : '{E3B2EB5A-FE46-4DA6-8DDD-6135E2120CB2}',
	'BSplineCurveDefinition' : '{30630D32-6807-4D69-8E77-224FD90A21BF}',
	'Polyline3d' : '{C9EBE756-798A-4E78-8CC4-DA91D7737321}',
	'Polyline2d' : '{2A1047EF-0B48-413B-92FD-6CA45A488DA6}',
	'OrientedBox' : '{556DCFA3-BD63-4B13-9C12-D99113AEAEFB}',
	'TransientObjects' : '{6BA435D7-BBD6-11D4-8DE6-0010B541CAA8}',
	'TranslationContext' : '{6BA435D9-BBD6-11D4-8DE6-0010B541CAA8}',
	'DataMedium' : '{6BA435DB-BBD6-11D4-8DE6-0010B541CAA8}',
	'ObjectCollectionByVariant' : '{FD9487E1-57A9-419B-A365-14323D1B1CD9}',
	'FileMetadata' : '{BEE271DA-318F-471D-AF24-296B6F59B392}',
	'InventorVBAProjects' : '{EEB0116A-7B74-4A9C-B2FF-96BC31812249}',
	'FileManager' : '{B00506C6-BEB7-47F6-8B1B-A5CB5DCD09B3}',
	'FileManagerEventsObject' : '{C029F46A-865A-4466-BE55-DF72750C8865}',
	'FileManagerEventsSink' : '{CA8E18AF-5EA2-4A45-BA43-FF3914C5C200}',
	'AssemblyOptions' : '{C6345819-0FAA-45A0-BF96-3C946F130076}',
	'GeneralOptions' : '{DBB345F5-06CB-4B20-96B8-C47EF589ECBE}',
	'ThreadTableQuery' : '{5A0B6FAA-1405-4AB1-AFE9-786462FADF33}',
	'ThreadInfo' : '{1470BE5E-D0B2-4177-A484-3528D6B0FC37}',
	'GripSnapOptions' : '{C032137F-6434-40C1-8DEC-763A191D1EE0}',
	'SpellCheckOptions' : '{2389822D-0890-4A2F-8CE3-B5F65E162E96}',
	'CustomDictionary' : '{88032CAE-3F85-4B0E-A4C0-9F76F490DDDC}',
	'CustomDictionaries' : '{D80190AB-F025-4F75-9363-D3522E429A56}',
	'SketchOptions' : '{8B657FE9-BF0A-4AED-B1FB-166229D406B3}',
	'HeadsUpDisplayOptions' : '{F440685C-03F8-49FF-8B68-79E575AF5A5E}',
	'SketchConstraintSettings' : '{541E7231-CD23-4986-B26D-4C2B4F1E2DBE}',
	'PartOptions' : '{986FCF92-8A47-4DEC-9007-DD852292DE71}',
	'Sketch3DOptions' : '{D39AB98F-45E0-4CAE-A0F2-4490804F2AD3}',
	'DrawingOptions' : '{221277C1-7963-4539-B2E5-E7E16D3C75AA}',
	'SaveOptions' : '{A6EC8B79-931A-409E-90CE-3EE28CB9F9F4}',
	'FileOptions' : '{EB213A42-0727-48F0-9BCF-C55F6CB4CD78}',
	'FileOpenOptions' : '{F7EDD327-75BC-4976-A0AE-7696B54D461D}',
	'HardwareOptions' : '{9A19AF07-A6BF-43AA-ABF3-870CA1CF329F}',
	'ContentCenter' : '{8AC1686D-0646-41D5-A28F-05353181AEBA}',
	'ContentQueryObject' : '{2BF92C40-9E07-4F12-B6A3-C5DAA12D3A61}',
	'ContentQuerySink' : '{6F10D9EC-E95C-489C-A398-5B530FD1D820}',
	'CategoryManager' : '{2B4C4468-F71B-44EE-BAC6-C68CD4F8DDA1}',
	'FamilyManager' : '{BFB40FAA-DEC6-4C84-BBA2-8FD424F3C564}',
	'MemberManager' : '{2B24FE45-C9E2-4590-BA7E-F7DB0E5A683F}',
	'QueryManager' : '{FC6C5BEB-A2CE-4249-8C31-6B0E1E8030A9}',
	'LibraryManager' : '{C3E0CCFC-A6F5-4C54-83E4-3A2CBF11D5D7}',
	'ContentCenterEventsObject' : '{069D986F-6DED-4D48-900F-B53674E46499}',
	'ContentCenterEventsSink' : '{6C6BEFAC-FECC-47A9-8A4C-68210FE441C3}',
	'ContentCenterDialog' : '{52223C79-EAAC-45CB-B000-35DBB1494A3D}',
	'ContentCenterDialogEventsObject' : '{F55C4A2E-FEBB-4EEA-872D-C54B481B0948}',
	'ContentCenterDialogEventsSink' : '{26F03E86-7DA4-4789-AACC-DE231C4C35E5}',
	'ContentTreeViewNode' : '{3DD6B742-71A1-438D-BB71-5CACFA2AACBE}',
	'ContentTreeViewNodesEnumerator' : '{2CB6EA8B-44E3-4C93-BB2A-531D62EBD934}',
	'ContentFamiliesEnumerator' : '{239A8027-E757-4A2E-B8DC-9203A644401F}',
	'ContentFamily' : '{30E22548-6DE0-43B7-A8EE-E379A9C86F7D}',
	'ContentTableColumns' : '{E06998C3-E510-47D3-BE8D-2CD348F24456}',
	'ContentTableColumn' : '{20C36669-DC84-413C-84A7-4D0983BAD319}',
	'ExpressionLimits' : '{F8CA1F67-2904-4C91-88F3-F79683227118}',
	'ContentTableRows' : '{8BEE2F07-0ACD-4A3C-A5BC-E064C8C0DBA8}',
	'ContentTableRow' : '{1C310044-05CF-4B79-9829-FE41BD1EB1A6}',
	'ContentTableCell' : '{2F27448C-CB52-4D34-87AE-6D75E01F5623}',
	'iFeatureOptions' : '{2B03891E-1B59-4576-8160-C61EA6E6D0DC}',
	'NotebookOptions' : '{CEF827E8-5A0A-452D-83BB-1A88815C1601}',
	'DisplayOptions' : '{48694BB1-0E75-4A39-94E0-C7C133C23305}',
	'ShadedDisplayOptions' : '{DA7E3A1C-5473-4CC3-8E19-25F8DE00C0A6}',
	'WireframeDisplayOptions' : '{75091477-A808-4B93-AF11-14C0CD466611}',
	'MeasureTools' : '{78B3596A-176A-43F5-A65C-4BDFFC042236}',
	'LanguageTools' : '{0420658E-CCD1-4100-BFA1-AD78AA655551}',
	'TransientBRep' : '{2BFE4397-C369-4CEF-90C9-D5C8AE90BC9F}',
	'SurfaceBodyDefinition' : '{4D662CE2-D29B-42E0-BA74-715C311E5630}',
	'EdgeDefinitions' : '{7F842490-A580-4A3A-AF94-DF8E5D292A42}',
	'EdgeDefinition' : '{F8B3014D-CA2D-40F4-B2A3-FA00E23105A1}',
	'FaceDefinition' : '{F3ACEE71-EC98-43F5-AC33-D0BDE47609EE}',
	'EdgeLoopDefinitions' : '{9A9B007B-18C5-4C27-BBA5-1D8F7E9B9A30}',
	'EdgeLoopDefinition' : '{F1779764-61F6-4C25-8B5D-6A6F41B57709}',
	'EdgeUseDefinitions' : '{ECEA0373-8BE9-4970-A696-C967A9718017}',
	'EdgeUseDefinition' : '{6307798C-50E3-4E9E-B502-038DA82B7C74}',
	'VertexDefinition' : '{40E01FF0-E437-4C55-83A4-8E3FA8B19225}',
	'LumpDefinitions' : '{41473886-B1F1-4E65-9BEB-36F729B6A9F1}',
	'LumpDefinition' : '{27AAE3A7-29EC-4C49-9845-97318E4C6905}',
	'FaceShellDefinitions' : '{1B28061F-6494-47D6-B8A4-3F6EF0DF0642}',
	'FaceShellDefinition' : '{BB41DDFD-351A-4AC7-9294-0FF1D2710C07}',
	'FaceDefinitions' : '{34EE0736-EB0C-47F4-A4DA-D28AE8D91BFF}',
	'WireDefinitions' : '{29440031-7A2B-4713-907C-DCCE79375669}',
	'WireDefinition' : '{9F5047CD-939F-4F15-930C-5C77CEB50BAA}',
	'WireEdgeDefinitions' : '{4B427038-81A6-4E75-A633-CF7CCBDD8160}',
	'WireEdgeDefinition' : '{D29F9AF1-3383-40AC-94BA-69057A213AAD}',
	'VertexDefinitions' : '{F5BB5A51-A89B-425E-A747-23CD25D3C186}',
	'ApplicationUtilities' : '{DB93184E-4A45-4C38-96B4-42051502413D}',
	'MoldDefinition' : '{E8D1DB25-5BBF-4635-B2A9-2ECC3A150373}',
	'MoldSplitResult' : '{CB5F8603-7F21-4B44-A5C1-CD471AB5EA08}',
	'RunoffSurfaceDefinition' : '{6D78B55D-0148-442F-9EF5-E00611FCD8FF}',
	'ErrorManager' : '{7B550B22-4519-43D2-9A9E-5EC0D9FFCCD6}',
	'MessageSection' : '{C7CECA91-B8BD-4C0E-A998-FBFD9BE85416}',
	'ContentCenterOptions' : '{650A171B-40E1-4C3B-B55E-DFB3D31C2CB8}',
	'StylesManager' : '{D93EE206-0CA6-401E-B74E-0D9E4F924751}',
	'MaterialsEnumerator' : '{DDD3ADB9-30D8-4E01-8E88-42ABF8645AD4}',
	'DebugInstrumentationObject' : '{F6F33557-6984-11D5-8DF3-0010B541CAA8}',
	'DebugInstrumentationSink' : '{F6F3355B-6984-11D5-8DF3-0010B541CAA8}',
	'_AppPerformanceMonitor' : '{DDC2F383-3824-49E3-837C-7387D4775893}',
	'TestManager' : '{369933DF-0F63-46AA-919B-17C91F385C9E}',
	'TestCases' : '{A4555442-8328-402E-BBF5-EDC7D808E522}',
	'TestCase' : '{3588F0A6-950E-402A-BFB1-C0ECB1B2EE44}',
	'TestProgram' : '{52D6C08A-B387-4F4C-A2E3-4F3CFFF276CE}',
	'TestInputOutput' : '{2190DB7B-9EAB-45D5-B9E0-B7FE50E1F50B}',
	'TestResult' : '{D88ABC2A-BA2E-4E03-AABE-E052F004A177}',
	'TestResults' : '{8378680D-EA06-405D-986A-8406E0E874B0}',
	'TestPrograms' : '{ED859179-A285-41B4-A736-55215294134D}',
	'TestConfiguration' : '{66B08E3B-4411-44C0-9A17-2C818A5BB08F}',
	'EnumType' : '{127400A4-792F-4C40-892E-1AEEA1BBF1E2}',
	'PresentationOptions' : '{6E68C1F1-A6AF-4235-8E86-AB031F7813E3}',
	'AssetLibraries' : '{DF8C6267-186F-4A45-8BD4-2545484B102E}',
	'ReferenceKeyEventsObject' : '{B4A5B240-ED5B-4F0F-B5C7-A1D21FB85939}',
	'ReferenceKeyEventsSink' : '{4DA70A52-6AE0-4674-95A6-6D7E563CD589}',
	'CustomDataEventsObject' : '{60C6DD49-AE1F-4937-A6EF-844A85C7D052}',
	'CustomDataEventsSink' : '{C59649BA-7BE5-42DD-8839-625556A813F0}',
	'PluginLicenseManager' : '{BC3FDF84-449A-4C14-A825-473FDB60C433}',
	'PluginLicenseManagerEventsObject' : '{FA98595D-E7A6-4C19-810D-AC891DA24402}',
	'PluginLicenseManagerEventsSink' : '{80334E55-A73F-45EC-A1D9-EE2A8F5BDD5C}',
	'ViewsEnumerator' : '{2C16787B-83FF-11D4-8DDB-0010B541CAA8}',
	'HelpManager' : '{9C88D3AA-C3EB-11D3-B79E-0060B0F159EF}',
	'HelpEventsObject' : '{2A922EEA-AE03-4C69-9986-D79D5A5A24DA}',
	'HelpEventsSink' : '{39E63B3F-3A40-4735-9C8F-012AFB75F087}',
	'EnvironmentBaseCollection' : '{BC985A7D-4B44-4089-870D-0AEE95D5E86A}',
	'EnvironmentBase' : '{09E02BBB-8953-4E69-8686-B0AADCFF8D02}',
	'CommandBarBase' : '{582865AB-F113-4939-8796-336EA266F8B2}',
	'CommandBarBaseCollection' : '{51BAA695-F419-4D00-B6C5-7C32F4114562}',
	'ColorScheme' : '{917CE8E7-741A-48A3-8E15-89A6DA053C40}',
	'ColorSchemes' : '{817C825E-2D55-4E09-A69E-789E9753959D}',
	'FileDialog' : '{BA80AE34-5BB2-4C90-BFDE-64DA56286813}',
	'FileDialogEventsObject' : '{5993FFB7-877A-4AFA-9BAA-73D627DE0D39}',
	'FileDialogEventsSink' : '{BF078925-9AC1-485E-9638-4DE87CABBCB7}',
	'ThemeManager' : '{388C8482-AC37-4E41-8B59-DC4A2F6BFE45}',
	'ProgressBarObject' : '{3D157428-294A-4446-A33D-6BEA664F61D7}',
	'ProgressBarSink' : '{6322C608-F92C-4CBB-9C17-B1661DA641AB}',
	'FileUIEventsObject' : '{C4F1B40A-B7A7-4F92-A9A4-CF8B1DDDE124}',
	'FileUIEventsSink' : '{63AD687A-3898-44E2-B857-C9DAD84FC9EC}',
	'CameraEventsObject' : '{F2BD70CA-061C-45C4-B057-88526074C390}',
	'CameraEventsSink' : '{839AA92C-F073-4BB6-9657-51061150E17C}',
	'TutorialsManager' : '{0169EC1F-0694-4353-B28D-3D74B59402D0}',
	'WebViews' : '{B894B815-AEF1-4FAA-938A-2131E2E5190F}',
	'WebBrowserDialogs' : '{077CE0DB-81E9-4A4C-B0D3-C5C33B3128A4}',
	'WebBrowserDialog' : '{42ACC897-4782-4BB7-9F3F-1C3167372D3D}',
	'WebBrowserDialogEventsObject' : '{97040303-12F3-4AE3-952E-FA2C15EB5665}',
	'WebBrowserDialogEventsSink' : '{0D5E3454-9140-4731-96D3-F86A47C1678F}',
	'FactoryTableDialog' : '{1052B04A-487B-446C-AAAD-90CD3BCCAC9E}',
	'BrowserFoldersEnumerator' : '{A9427B73-D39C-4DA3-9330-3CEB71ECA2B9}',
	'BrowserFolder' : '{9D063FDB-B597-49B0-8DBC-7EB3D5F715B8}',
	'SearchBox' : '{9BD8EE46-BA95-4CDF-BC13-8C912B4582AE}',
	'SearchBoxEventsObject' : '{2E7E650F-4051-46F0-96AD-E42CC1C5F980}',
	'SearchBoxEventsSink' : '{E35E9F66-6F21-467A-A44B-D3CBD0920E8B}',
	'ClientNodeResources' : '{9C8B2909-8C33-481E-8CF5-9C269B4E54DC}',
	'ClientNodeResource' : '{9ACFBDEF-B81B-4B4D-8EA6-8453F1DD6285}',
	'ClientBrowserNodeDefinitionObject' : '{CABA7470-1B47-492D-A62E-EE7213257C05}',
	'ClientBrowserNodeDefinitionSink' : '{B142CBF7-AE52-4AC4-ADAB-7A36A2A9A834}',
	'BrowserPanesEventsObject' : '{EF126FC8-7582-4E15-B5DC-194EEE2CEEDA}',
	'BrowserPanesSink' : '{B159D948-7FC9-4D48-B482-FC7FD152AFCA}',
	'NativeBrowserNodeDefinitionObject' : '{FAD47DA5-3A14-4A2C-9A70-7BCDD992D8A7}',
	'BrowserNodeDefinitionSink' : '{11D880AF-2B60-4816-A74A-73526CFE6FDD}',
	'SurfaceGraphics' : '{5F24EB5E-169E-47C1-9C3D-401A01F4415B}',
	'SurfaceGraphicsFaceList' : '{0B8D52D2-8147-4407-B2E3-D982ED775F0C}',
	'SurfaceGraphicsFace' : '{18757DD9-20E4-4DF9-9585-1AC6D0B941FB}',
	'SurfaceGraphicsEdgeList' : '{977D767F-C958-44E8-AB59-8F7267DEBBA1}',
	'SurfaceGraphicsEdge' : '{834BFEF4-D052-4139-93F2-D4F08F3A3121}',
	'SurfaceGraphicsVertexList' : '{C11F6667-E5D4-4A7E-8C47-70AA423E7758}',
	'SurfaceGraphicsVertex' : '{7C9B84A9-127C-42B6-A0A7-6CDC39B98CDE}',
	'ComponentGraphics' : '{C958801B-73D0-4031-B9F6-5CDBCE975ABC}',
	'BOMQuantity' : '{07F8CD55-9194-4CDB-8403-6BFC4F99D1EE}',
	'ComponentDefinitionReferences' : '{5DF86023-6B16-11D3-B794-0060B0F159EF}',
	'ComponentDefinitionReference' : '{5DF8601F-6B16-11D3-B794-0060B0F159EF}',
	'AssemblyConstraints' : '{AA044AA3-D685-11D3-B7A0-0060B0F159EF}',
	'MassProperties' : '{2FA1D3CF-EAFF-4D47-9E13-E5B074C1565C}',
	'InterferenceResults' : '{F2286BBF-D48E-4F85-A613-A48AF46893BC}',
	'InterferenceResult' : '{FA452CED-C585-4568-BACD-C3DBFAC85D97}',
	'OccurrencePatterns' : '{1112CDE3-CD39-4004-8E74-0C019C73F380}',
	'FeatureBasedOccurrencePattern' : '{773C0E8F-2C4C-4871-93F7-AF9483171461}',
	'WorkAxes' : '{28DD48B5-8D70-11D4-8DDE-0010B541CAA8}',
	'WorkAxis' : '{28DD48B7-8D70-11D4-8DDE-0010B541CAA8}',
	'WorkPlanes' : '{46785C3B-7F4A-11D4-8DDB-0010B541CAA8}',
	'WorkPlane' : '{46785C3D-7F4A-11D4-8DDB-0010B541CAA8}',
	'WorkPoints' : '{28DD48C7-8D70-11D4-8DDE-0010B541CAA8}',
	'iMateDefinitions' : '{AE309209-288A-4083-BEAB-7DFB7EC9947D}',
	'AngleiMateDefinition' : '{F5C82F4B-9B32-488E-920A-31F065B1AD77}',
	'CompositeiMateDefinition' : '{BAC6577B-6985-4B55-BADC-8113EFF69A3C}',
	'FlushiMateDefinition' : '{4A943DD0-592A-4E36-8E2C-D2E9DD54B2F5}',
	'MateiMateDefinition' : '{425EAA71-D590-4893-AFAB-012380A7CEBA}',
	'InsertiMateDefinition' : '{4FE10280-6679-4500-B7CE-411995D157E7}',
	'RotateRotateiMateDefinition' : '{6025C779-5DFB-4B1D-B2C9-E7CDD5D18B5F}',
	'RotateTranslateiMateDefinition' : '{06460F0C-B76C-49E4-B24A-3C60142219B9}',
	'TangentiMateDefinition' : '{C78E43C1-DB92-414A-9B45-352DFAC434E4}',
	'iMateResults' : '{9788ECD5-7355-4AFC-8784-B139CAC98DF3}',
	'BOM' : '{8AF6DB71-B75D-4D21-A837-4A6699E972BC}',
	'BOMViews' : '{12A24FCF-4CBD-403D-9E32-ECE5DC3297E9}',
	'BOMView' : '{5538440B-E168-4C38-B817-56F50B538C96}',
	'Features' : '{89B5C2F2-A577-41F7-953A-916CF31BC7D5}',
	'ChamferFeatures' : '{2D38284B-DEAD-48C3-905D-02D1B7432699}',
	'ChamferFeature' : '{539ACB89-A1F6-43E4-BC0A-BDCE1B127584}',
	'ChamferDefinition' : '{8415AC9D-CA60-4AD8-8F79-CE03F00F573D}',
	'PartialChamferEdges' : '{5042E6DE-5FE2-49E6-9371-75554E6A1046}',
	'PartialChamferEdge' : '{FAD37762-2B83-491D-AB61-CD746D1EBE65}',
	'ExtrudeFeatures' : '{F05DFBBD-F824-48A1-8272-A62F1A524F42}',
	'ExtrudeFeature' : '{2FD8A7F5-B548-4E12-9D65-FF47FD063F8C}',
	'PartFeatureExtent' : '{8B6FA30B-DC7A-4603-8793-445D70FF073E}',
	'ExtrudeDefinition' : '{3098A39F-CCD6-4163-8ADC-2E9504F3E00C}',
	'FilletFeatures' : '{94ABF5D8-E979-494E-84D3-883672074BD4}',
	'FilletFeature' : '{7DE603B3-DAA7-4364-BC8B-77295B53D1DB}',
	'FilletDefinition' : '{448C7AED-838C-44DB-87FC-2D18E74AA05A}',
	'FilletRadiusEdgeSet' : '{A40068C9-5681-4B3D-961A-1C6360B20BFE}',
	'FilletSetbackVertex' : '{C6C1652F-6D5B-495D-B7E5-F4DEB205BA25}',
	'FilletSetback' : '{325CFE17-8D9E-4977-A3B3-97AC9D827CD9}',
	'FilletConstantRadiusEdgeSet' : '{9374403D-49B0-4DA3-A4CA-55DDAB40D8E1}',
	'FilletVariableRadiusEdgeSet' : '{A335F5F6-7194-409E-94A7-45B617264920}',
	'FilletIntermediateRadius' : '{3C16D9FD-5F89-4669-B637-B356887583D1}',
	'FilletConstantRadiusFaceSet' : '{237CB3F2-314E-4211-92DC-D69C15BF1B64}',
	'FilletFullRoundSet' : '{FDBEDE20-57AB-44CC-9A84-31E4D730E85D}',
	'HoleFeatures' : '{A0DB05CD-57E9-47C9-9D33-E648BB57226A}',
	'HoleFeature' : '{ABA7FFC5-E604-498E-B1B1-B829D4E059EC}',
	'HolePlacementDefinition' : '{8924897F-3F00-4220-BF8A-76CADC5A10DD}',
	'HoleTapInfo' : '{F5BFBDBA-35EE-424D-A3AD-8D87B22484CF}',
	'TaperedThreadInfo' : '{D4D0315D-6874-4E69-9BBB-6E3D28B9122A}',
	'SketchHolePlacementDefinition' : '{2BC16E62-07F5-4106-B5BD-58C7C660DA2C}',
	'LinearHolePlacementDefinition' : '{06AC6A50-B820-406B-995A-DDA0CCE3E2F5}',
	'ConcentricHolePlacementDefinition' : '{71F90E58-8C83-4C68-9B75-2E14F8BF3A23}',
	'PointHolePlacementDefinition' : '{1993ABC5-7080-4CB1-9CE3-406B4B70B951}',
	'RevolveFeatures' : '{8EB2E33C-2CF3-41E6-9B08-C0C0D15DF5EE}',
	'RevolveFeature' : '{87F4CA2E-5700-4FC7-A283-8E2D90FE5F61}',
	'SweepFeatures' : '{CADFFDB1-11E6-4684-A35E-7EE2064AA46C}',
	'SweepFeature' : '{773586BE-A5CE-422F-9036-FAFC8451F011}',
	'Path' : '{86338055-4538-47A0-BD9B-06A8C4BD8D93}',
	'PathEntity' : '{6B9C5A03-557E-477A-A6E4-D2E00FB5B812}',
	'_SweepDefinition' : '{3D70E84F-AC86-4734-8A36-1672FE750893}',
	'SweepDefinition' : '{938C8A20-C60B-47C8-A9F4-CDAA7CE06095}',
	'SolidSweepDefinition' : '{1DD4A980-A4A8-4BEA-8691-FA05F1BAAC95}',
	'RectangularPatternFeatures' : '{ADA699FB-D9E7-4879-A1A3-86D9F2C6F57F}',
	'RectangularPatternFeature' : '{58B0C13D-27CC-4F06-93FD-0524B69E6578}',
	'FeaturePatternElements' : '{82B32371-11B8-467E-B57E-0112DDD4BB65}',
	'FeaturePatternElement' : '{1A60195B-72BF-4714-9392-1212EC6260CB}',
	'RectangularPatternFeatureDefinition' : '{07291B94-27DD-4EAD-BC9A-9123FF5EF420}',
	'CircularPatternFeatures' : '{E2E51C17-C894-45AF-9827-988D38C283C7}',
	'CircularPatternFeature' : '{7BB0E824-4852-4F1B-B43C-7F729A3D7EB8}',
	'CircularPatternFeatureDefinition' : '{311AF9CD-27E4-48F9-8117-955692A98376}',
	'MirrorFeatures' : '{26C57F9F-A6AC-4FCD-BE7C-DAE2F0940E8E}',
	'MirrorFeature' : '{12BF1F8A-5679-468F-A820-DA5532624CEA}',
	'MirrorFeatureDefinition' : '{3026FC98-A183-45C8-84BF-D4EF802A5629}',
	'SketchDrivenPatternFeatures' : '{DC6DA623-B4F1-4185-B954-92F92F3C8E21}',
	'SketchDrivenPatternFeature' : '{CD9F482B-1EE9-4F16-AEFD-2C5934AC17CC}',
	'SketchDrivenPatternDefinition' : '{B2B45853-725F-4E73-86D1-8B550B5CACD7}',
	'MoveFaceFeatures' : '{04370FAD-4F3A-4589-A7F8-6DFA839522D3}',
	'MoveFaceFeature' : '{837D8FB2-848D-4A3B-8F83-ECCFDCAC2766}',
	'MoveFaceDefinition' : '{B0A76319-7649-4B77-9159-0975E700253B}',
	'ClientFeatures' : '{68AF2955-0901-433D-B7C3-D91D637DD21C}',
	'FaceOffsetFeatures' : '{3FD23B6F-222D-485D-A9E8-164C497B17F8}',
	'FaceOffsetFeature' : '{31C63BA8-7EB4-4816-A367-F99A12691690}',
	'FaceOffsetDefinition' : '{20C6159F-9ACD-4AA6-B616-1CC57A6F91CA}',
	'FaceOffsetPreview' : '{FD93BF70-B8C9-4CEE-8AEB-AAC34B534803}',
	'MidSurfaceFeatures' : '{B148630A-2ECA-4159-8FF2-77CD1B7A79A5}',
	'MidSurfaceFeature' : '{247E2AC0-3948-4DD9-88A1-0AC87A794BC7}',
	'MidSurfaceThicknesses' : '{6E9FA739-9CD7-49D3-85B9-72F260BFBF52}',
	'MidSurfaceThickness' : '{08389E18-6E84-499B-8F1F-09AC53003178}',
	'ThreadFeatures' : '{D0786DD9-AD8A-431B-B2A9-388211ABD7DD}',
	'ThreadFeature' : '{F8957621-7E89-4CB8-AFCA-CE11A556E7A2}',
	'StandardThreadInfo' : '{B2CB30BD-4B68-4D6C-8A07-3122FE52E6B9}',
	'iAssemblyFactory' : '{B76D6529-D84D-4A66-8215-58B6A32D56A9}',
	'iAssemblyTableRow' : '{18517A46-ABB7-4285-94B4-35B3277880F1}',
	'iAssemblyTableCell' : '{290EC1FE-2BB5-46E8-AB41-919D7455740D}',
	'iAssemblyTableColumns' : '{C7AF47E6-3FDE-469F-B258-85FE0390E7DA}',
	'iAssemblyTableColumn' : '{90821476-EE63-4328-BC9F-164D0BBF6F9C}',
	'iAssemblyTableRows' : '{CE99120C-2AEC-4916-AB66-C14F780325A7}',
	'FactoryOptions' : '{1DC369B0-C6C9-42B7-BA0F-5A2AB9CA79AE}',
	'iAssemblyMember' : '{29049E48-996E-4799-8DA6-778A0B82AB54}',
	'PlanarSketches' : '{A03B2CAF-A5F8-4522-BF79-CF4D497DCF4E}',
	'RigidBodyResults' : '{E09DAF1C-7738-4CDB-B26B-5DE6A2B37573}',
	'RigidBodyGroups' : '{CBE24DE3-529E-4039-BFDF-D014844691F0}',
	'RigidBodyGroup' : '{611952AC-F765-4950-8863-36C465FA2370}',
	'RigidBodyJoints' : '{1C4A4777-E52F-405F-BABA-7ED0931E81C0}',
	'RigidBodyJoint' : '{1C0E39F2-15F3-41EA-94C1-62AD59AD25D9}',
	'AssemblyJointsEnumerator' : '{15AD2867-FEE2-4A5B-9F07-FDC0A4FF5C72}',
	'AssemblyJoint' : '{9C7891F4-F438-445A-AD22-8FB29E343231}',
	'AssemblyJointDefinition' : '{AB9D8E26-4BEC-4E22-84B0-B1ECDED332D8}',
	'UserCoordinateSystems' : '{D0BD7B89-04B5-4165-8E8D-1DB705A02E47}',
	'UserCoordinateSystem' : '{F0854465-652D-4375-98A4-7C875BFE7A9C}',
	'UserCoordinateSystemDefinition' : '{598714D9-653D-4D2B-B7BB-139C3E9E38B1}',
	'BIMComponent' : '{47005682-42D1-4831-A4BC-63AD38B98D6E}',
	'BIMComponentDescription' : '{03B09E04-FA49-40EA-AE2D-FF7972025350}',
	'BIMComponentPropertySets' : '{34ACFD9F-B9B0-4D81-B44C-55AEEAEE16BC}',
	'BIMComponentPropertySet' : '{5F89369C-998C-4AD6-B59D-FBA9AFDCFB65}',
	'BIMComponentProperty' : '{A145B58E-E928-4180-951B-D7E652298E2A}',
	'BIMConnectors' : '{7C1BEFD9-4296-4794-B3A2-8025809570D8}',
	'BIMConnector' : '{12DA4D02-DCE6-4F08-ADEB-9EE13C559C52}',
	'BIMConnectorDefinition' : '{E41CA526-545A-4782-A383-C44FC7523552}',
	'BIMCableTrayConnectorDefinition' : '{2D6BA5C4-3929-44A3-8D59-5A173034BBF1}',
	'BIMConduitConnectorDefinition' : '{744F35C4-CD6F-46C3-87B8-80425AB4AFA2}',
	'BIMDuctConnectorDefinition' : '{1FE852AA-E1B7-4160-8F8D-302E0B46BC52}',
	'BIMElectricalConnectorDefinition' : '{1F222D21-CBB5-4FC4-A6CF-0387224A7F2C}',
	'BIMPipeConnectorDefinition' : '{E52803C6-7F1E-4D7B-9C0E-D4FA6BFFA00D}',
	'BIMConnectorLinks' : '{99C8344C-60E3-46CA-A32D-1EF2010EB01D}',
	'BIMConnectorLink' : '{8E05BCC6-20B2-477A-A318-CB7116D8D0A7}',
	'SimulationManager' : '{7771DA50-AFDF-4E9A-9055-1CAA9B9CFFE5}',
	'DynamicSimulations' : '{7771DA51-AFDF-4E9A-9055-1CAA9B9CFFE5}',
	'DynamicSimulation' : '{7771DA52-AFDF-4E9A-9055-1CAA9B9CFFE5}',
	'DSJoints' : '{7771DA58-AFDF-4E9A-9055-1CAA9B9CFFE5}',
	'DSJoint' : '{055EC022-CD9B-4983-97E2-2EC073939046}',
	'DSJointDefinition' : '{055EC023-CD9B-4983-97E2-2EC073939046}',
	'DSDegreesOfFreedom' : '{055EC024-CD9B-4983-97E2-2EC073939046}',
	'DSDegreeOfFreedom' : '{055EC025-CD9B-4983-97E2-2EC073939046}',
	'DSValue' : '{7771DA56-AFDF-4E9A-9055-1CAA9B9CFFE5}',
	'DSValueGraph' : '{7771DA57-AFDF-4E9A-9055-1CAA9B9CFFE5}',
	'DSResults' : '{055EC026-CD9B-4983-97E2-2EC073939046}',
	'DSResult' : '{055EC027-CD9B-4983-97E2-2EC073939046}',
	'DSLoads' : '{7771DA53-AFDF-4E9A-9055-1CAA9B9CFFE5}',
	'DSLoad' : '{7771DA54-AFDF-4E9A-9055-1CAA9B9CFFE5}',
	'DSLoadDefinition' : '{7771DA55-AFDF-4E9A-9055-1CAA9B9CFFE5}',
	'DSSettings' : '{7771DA59-AFDF-4E9A-9055-1CAA9B9CFFE5}',
	'VisibleOccurrenceFinder' : '{B4D0EB63-4D3B-42A6-BE38-855EB5DA68E3}',
	'AssemblyJoints' : '{EF706A55-28C3-41A6-8D99-EE900BDBCD9D}',
	'PointClouds' : '{715899F9-C5E6-4A31-96C7-151D74A852B8}',
	'PointCloud' : '{6E45ED1A-92ED-469A-9CE0-79C26C9CB5E5}',
	'PointCloudRegions' : '{10DE860A-67D1-47ED-A23A-291BD48E25E9}',
	'PointCloudRegion' : '{E34C07F3-B8FF-4181-ADC4-DEE3D6550961}',
	'PointCloudScans' : '{F20B72F3-D856-45E8-A71A-0753F12D7A10}',
	'PointCloudScan' : '{A962939B-0A11-490F-AC66-DC0FDAA3DD75}',
	'PointCloudCrops' : '{AADD24A8-0094-41C6-BF61-C79E700AA1E2}',
	'PointCloudCrop' : '{2D5EB497-6E4D-4B66-B185-EB6C7C188F2F}',
	'ImportedComponents' : '{D2F65CFD-A8D7-44D1-8262-9FD5BCA8FECA}',
	'ImportedComponent' : '{239475B6-6DCA-4683-B410-A5788BF2077B}',
	'ImportedComponentDefinition' : '{903F1E1B-1A0E-4344-820B-CDD9619C0FDC}',
	'iMateDefinitionsEnumerator' : '{22D71B5C-2F5E-4A1B-9328-ABE89F78ABC6}',
	'EdgeLoops' : '{5DF86093-6B16-11D3-B794-0060B0F159EF}',
	'Vertices' : '{5DF86096-6B16-11D3-B794-0060B0F159EF}',
	'TextureMaps' : '{8BC9C1AA-4238-4112-A5FC-15F3765E5336}',
	'TextureMap' : '{AF6AFE3F-4249-410E-A4F8-9399EE807D30}',
	'TextureCoordinateSet' : '{D96060F8-0E08-4E73-8D5E-37F506A1A738}',
	'PartFeaturesEnumerator' : '{AD3341ED-F50C-46F3-AB93-601CA37413E6}',
	'DraftAnalyses' : '{5C93A2CD-ECCA-4998-9DC4-D439BD9FE3DB}',
	'DraftAnalysis' : '{9C9D6F69-F26B-4311-A688-17C04EC292BE}',
	'AnalysisManager' : '{BB075EDC-49B3-4F03-8737-5E20737B1AEB}',
	'ComponentDefinitions' : '{5DF86022-6B16-11D3-B794-0060B0F159EF}',
	'ComponentOccurrenceProxy' : '{46AEA719-4302-11D4-B7AB-0060B0F159EF}',
	'DraftingStandard' : '{206B59B0-22A6-11D4-B7A8-0060B0F159EF}',
	'EdgeProxy' : '{46AEA72F-4302-11D4-B7AB-0060B0F159EF}',
	'EdgeLoopProxy' : '{46AEA72C-4302-11D4-B7AB-0060B0F159EF}',
	'EdgeUseProxy' : '{46AEA72D-4302-11D4-B7AB-0060B0F159EF}',
	'FaceProxy' : '{46AEA72B-4302-11D4-B7AB-0060B0F159EF}',
	'FaceShellProxy' : '{46AEA72E-4302-11D4-B7AB-0060B0F159EF}',
	'SweepGraphics' : '{1435773B-06FC-46E8-B965-5845697D2A6B}',
	'GraphicsNodeProxy' : '{C6DE930F-09D7-487F-A4C9-401AA8B19879}',
	'OccurrencePatternElementProxy' : '{5B94A1C2-5FA9-4093-87DD-11B7115B9F02}',
	'SurfaceBodyProxy' : '{46AEA729-4302-11D4-B7AB-0060B0F159EF}',
	'VertexProxy' : '{46AEA730-4302-11D4-B7AB-0060B0F159EF}',
	'AssetTexture' : '{3E0ED07A-F5ED-46BF-8903-EBC1B409A270}',
	'ChoiceAssetValue' : '{CC1FB682-EF98-4FE5-9934-143CFB8C65B1}',
	'FloatAssetValue' : '{5F0359BB-A074-4CD1-98EF-F66DAE4649E9}',
	'IntegerAssetValue' : '{48D3D9AD-F3F0-41E8-B4D8-6DA2533CCFC9}',
	'BooleanAssetValue' : '{4479E5B2-48BF-4760-BA24-0A0CE854DF24}',
	'ColorAssetValue' : '{9D7514D7-EA00-4F2D-8F66-0E395B21C284}',
	'TextureAssetValue' : '{AD623DC3-5354-483D-99A1-C7ADDB0C06CF}',
	'StringAssetValue' : '{9ADC4649-06DC-449E-ABE8-5DCA6F4C7788}',
	'FilenameAssetValue' : '{0FC5FA72-0397-4522-9E58-764385FA9B69}',
	'ReferenceAssetValue' : '{186F6C0F-C3A2-4798-9685-C773181074C1}',
	'MaterialAsset' : '{A095B86B-84EF-4364-888E-1F6F03EAA73F}',
	'ApprenticePrintManager' : '{8530B3FF-DBD2-4C75-A6EC-0755B8229AE7}',
	'ApprenticeDrawingPrintManager' : '{F90311E1-7249-40AF-A597-8AFF681BFA93}',
	'ApprenticeServerDocument' : '{C343ED83-A129-11D3-B799-0060B0F159EF}',
	'ApprenticeServerDocuments' : '{59D3FA3A-ACE0-11D3-B79A-0060B0F159EF}',
	'FileSaveAs' : '{9CAF98A3-33EA-11D3-B78F-0060B0F159EF}',
	'ApprenticeServer' : '{C343ED82-A129-11D3-B799-0060B0F159EF}',
	'ApprenticeServerDrawingDocument' : '{4F589652-207C-11D4-B7A5-0060B0F159EF}',
	'InventorServerObject' : '{EF42229B-CAC3-488D-BCC4-C992FC7795AE}',
	'VbaApplication' : '{71A0E8AF-8F3E-485D-BB40-7C98163F9C14}',
	'_VbaImplementationEvents' : '{F8841598-132A-4A18-BE1F-EBDD2067C648}',
	'AliasFreeformFeature' : '{49A9C1BC-D718-4DCB-AAD8-8FB4285EFA45}',
	'AliasFreeformFeatureProxy' : '{8DE224FA-1DA2-4B05-BE2B-3E7FB6361FC2}',
	'AliasFreeformFeatures' : '{3C007201-8D66-47BD-AD94-2012FF75C4C5}',
	'AnalyticEdgeWorkAxisDef' : '{AF22C0E0-AEBC-4009-BD3E-85EBF9C9ED58}',
	'AngleConstraintProxy' : '{076FFE46-6694-42EE-9F7F-E61F71434845}',
	'AngleExtent' : '{312EFE2A-648A-4715-85F4-B7A1EF02CCB9}',
	'AngleiMateDefinitionProxy' : '{CFA8AC15-B4C1-4703-A672-DAED79017FF3}',
	'AngularModelDimensionProxy' : '{95137870-2785-4E40-BE13-1D23D6CDF348}',
	'AnnotationPlaneProxy' : '{6A979CE4-093B-4D91-9C67-CFE4D38C27E3}',
	'LinearModelDimensionProxy' : '{E8057590-7265-4294-9D82-1A93BF64178F}',
	'RadiusModelDimensionProxy' : '{744023BD-507E-43EA-B378-60D2F553C51E}',
	'DiameterModelDimensionProxy' : '{68E038B4-ED9F-4FE9-A4E0-8ABE96A474CB}',
	'AnnotationPlanes' : '{02F3D9FA-F750-4C1B-8A2E-A2C5BB99C76C}',
	'ApplicationAddInSite' : '{E3571299-DB40-11D2-B783-0060B0F159EF}',
	'Command' : '{C343ED7B-A129-11D3-B799-0060B0F159EF}',
	'ButtonDefinitionHandlerObject' : '{93224595-EAF4-4AE2-9604-16A2854AFF4B}',
	'ButtonDefinitionHandlerEventsSink' : '{96750E11-92EA-457A-BF5E-6FA15C44B8EE}',
	'EnvironmentBaseHandlerObject' : '{EBB974BD-2A69-4125-899A-5752878B7E55}',
	'EnvironmentBaseHandlerEventsSink' : '{165776AC-95DC-4BD0-8288-BE844390282F}',
	'DocumentSubTypeHandlerObject' : '{CAEB520A-F52E-4F2B-AE02-CE0BF9944814}',
	'DocumentSubTypeHandlerEventsSink' : '{94F1E029-984C-4DDC-9B12-003982C02E06}',
	'ApplicationAddInServer' : '{E3571293-DB40-11D2-B783-0060B0F159EF}',
	'SheetMetalComponentDefinition' : '{0562B816-F05F-4293-AF39-D2F640E42740}',
	'PartFeatures' : '{DA33F1A5-7C3F-11D3-B794-0060B0F159EF}',
	'NonParametricBaseFeature' : '{1D09051E-D674-4ABE-BEC9-5A58016455B1}',
	'CoilFeatures' : '{2C30965F-FD0D-4D6E-AC98-797F2F0E2DEB}',
	'CoilFeature' : '{B9036BF2-EBE0-4593-92B6-DBCD421C6BDF}',
	'DecalFeatures' : '{0218B59B-0CE5-4CA1-9A3B-F7D266C4E75F}',
	'DecalFeature' : '{9C693BB0-7C99-4D06-961E-99936273C492}',
	'DeleteFaceFeatures' : '{91BDBCAB-AC12-4216-ACE4-4F561D7DD4BD}',
	'DeleteFaceFeature' : '{4CDC6B45-25DB-442E-BF8B-12C87365788E}',
	'EmbossFeatures' : '{730B9714-80D2-4009-8904-1AEF4EAF3F23}',
	'EmbossFeature' : '{6A0A9BAD-53F2-4254-A34E-9262F980B5CE}',
	'FaceDraftFeatures' : '{C77D9639-C58A-4E5A-BAE0-14966E37DDEE}',
	'FaceDraftFeature' : '{EA1D0D38-93AD-48BB-84AC-7707FAC29BAF}',
	'FaceDraftDefinition' : '{8A551127-A520-46FD-A9C4-5ECD271576FC}',
	'FreeformFeatures' : '{E15EF363-30C7-420B-91DE-B76BE5F6007F}',
	'FreeformFeature' : '{88C36A1E-2212-4E9C-BBDB-3155DC8C06E9}',
	'DirectEditFeatures' : '{69F95DF7-6F84-4FF8-8060-AB921DF1E4F1}',
	'DirectEditFeature' : '{602389D5-6C6A-4368-A6F2-47D54FA1FBA4}',
	'DirectEditOperations' : '{DE936728-E326-4EE4-A671-9AC25F43868C}',
	'DirectEditOperation' : '{86EF3B55-8CEB-45E8-9C9C-5F4430679B7C}',
	'KnitFeatures' : '{1426BDF8-DD91-4FF0-AD8D-BB0EC8797B24}',
	'KnitFeature' : '{E408524C-B7A1-4F17-921E-160774F4DE5D}',
	'BoundaryPatchFeatures' : '{97D6B280-1D62-48E6-B4B9-007F25F7A3A5}',
	'BoundaryPatchFeature' : '{16B36EBE-2DFA-4474-B11B-DF3D57C109B0}',
	'BoundaryPatchDefinition' : '{4FF4C556-DB2C-4FD7-A7E5-06C171C18D7B}',
	'BoundaryPatchLoops' : '{4CD53A13-201C-402A-A729-EFEB24A1417C}',
	'BoundaryPatchLoop' : '{4DF199B9-D7C8-4770-9954-2EFF94867CEC}',
	'LoftFeatures' : '{24A0170B-C253-4A3C-9639-5DE9818A8F31}',
	'LoftFeature' : '{F7DDBE1D-2C8E-48B9-9E52-FC0BFB7D59A6}',
	'MapPointCurves' : '{E405BACE-0EE8-4427-B6BE-82CC11F9CC35}',
	'MapPointCurve' : '{52909F65-AE2E-4997-B3F5-527FE09BF5BE}',
	'LoftRails' : '{3E43E559-0053-402D-BE5F-4AC170C11A04}',
	'LoftRail' : '{02466B5A-9C4B-48C4-BFA0-5590DB014745}',
	'LoftDefinition' : '{FBEBA281-9346-4AC6-B324-6CEB7318BEBE}',
	'LoftSectionDimensions' : '{F8FBACE4-75A7-4493-B2D8-492AC937F3E5}',
	'LoftSectionDimension' : '{3138A370-A692-42B1-8C91-7981A9A0F12C}',
	'NonParametricBaseFeatures' : '{59E208A8-BB82-4322-92D6-DA364F8B9AB0}',
	'NonParametricBaseFeatureDefinition' : '{559C5073-6378-47FD-AA38-DE0BB46A9268}',
	'ReplaceFaceFeatures' : '{3CBD2849-0258-4583-9CE0-578A71CB7483}',
	'ReplaceFaceFeature' : '{5D8B9732-07F2-4E90-A4AB-C98FB56944A1}',
	'RibFeatures' : '{436A627D-919B-4B92-B242-268F7266D8A1}',
	'RibFeature' : '{D65B8777-CF40-4542-9A0F-28F2F6EF0678}',
	'RibDefinition' : '{5B078EF2-5839-4B6A-97D1-BB8F5D9CFD78}',
	'BossSets' : '{85672B0C-EA86-4DF1-B223-51DD72F29566}',
	'BossSet' : '{FB1FDFB0-239C-4040-9B22-7ACACCFFE82E}',
	'RuledSurfaceFeatures' : '{721CC25E-D96C-4E25-BED5-04EF710574B4}',
	'RuledSurfaceFeature' : '{E58169E1-CCA4-432A-9626-A37ABF5F287E}',
	'RuledSurfaceDefinition' : '{148406BE-AC67-4E05-B5E9-A427269D3A28}',
	'RuledSurfaceEdgeFacePairs' : '{89A80CCD-6F08-462F-98CB-BD062E77E8D4}',
	'RuledSurfaceEdgeFacePair' : '{7E763E3B-84CB-4D77-B4F1-C18A1BEF0EA6}',
	'ShellFeatures' : '{3B4B3DE9-7B05-47A7-975A-2C370BBBF974}',
	'ShellFeature' : '{E861980A-A56F-416A-BF52-876C8A06CE4E}',
	'ShellDefinition' : '{C80E7C12-B126-45F2-A228-704248D58530}',
	'ShellThicknessFaceSet' : '{0F8F253B-5ED8-4AE0-9C62-3DEFDCCD0BC4}',
	'SplitFeatures' : '{209DF795-8088-4158-969C-0CC120E0A2A3}',
	'SplitFeature' : '{78D752FD-9090-4AEA-9CF2-247ABA9D1936}',
	'ThickenFeatures' : '{F59CE3B0-44CC-4FB5-9C81-7234A25DD381}',
	'ThickenFeature' : '{97E8752C-E818-41FF-8C13-D10B6FBC522F}',
	'ReferenceFeatures' : '{347FB32C-79ED-4A5B-89B1-7B14FF6A9CA8}',
	'ReferenceFeature' : '{298849A9-ECAB-4234-9675-6FAA66A95E4D}',
	'SculptFeatures' : '{EAADC3AE-D599-495E-A56C-FA79AE3E8848}',
	'SculptFeature' : '{7E2A1EB5-F770-45BD-8DC5-8FEE60664D9F}',
	'SculptSurface' : '{65A5B1BC-9F61-4F5D-A113-66EDC3DAAAC0}',
	'TrimFeatures' : '{109C1DF4-2290-44AC-9E90-A108D090B4E9}',
	'TrimFeature' : '{98588913-EE07-4969-8939-3DFDEE09180E}',
	'ExtendFeatures' : '{4A355C86-508E-4A45-80C3-001139E9FD81}',
	'ExtendFeature' : '{2DADCD08-8ED5-4F71-88BF-481E8B0E9847}',
	'BendPartFeatures' : '{3E39E3B3-FA8E-463D-A191-6D7A7CB8E7AE}',
	'BendPartFeature' : '{2CBE5BA6-3501-4389-AF3F-AD114C0DAB5A}',
	'iFeatures' : '{D50258F5-140B-4AE1-BCC7-3CB2438B04E1}',
	'iFeature' : '{98675AD1-A109-43DE-A7D7-1612BC503E0E}',
	'iFeatureDefinition' : '{358B0B8E-D2C7-4D76-AAC6-33009864424E}',
	'iFeatureInputs' : '{AF669E3B-2FC3-4731-96C4-2CC724B98E60}',
	'iFeatureInput' : '{6A89E379-03FC-440E-A655-6111E86247A1}',
	'iFeatureTable' : '{5F15A208-8871-42B9-8421-D0555100A7D9}',
	'iFeatureTableRow' : '{F0684BBA-73A5-45B8-8D38-E64A53735C9E}',
	'iFeatureTableCell' : '{ABC49BF6-3E83-45A6-AF98-059245620FF4}',
	'iFeatureTableColumn' : '{34295D6D-002B-40DC-B1E9-E0D658532EF0}',
	'iFeatureTableColumns' : '{82B8F63A-474B-4DAC-AE2D-E9F5E9BB2C2E}',
	'iFeatureTableRows' : '{4A66B607-4991-4FA2-A361-CD8424A99A70}',
	'iFeatureTemplateDescriptor' : '{3C69FF6F-6ADD-4CF5-8E9B-32CBD2B6BBF7}',
	'SketchesEnumerator' : '{41E90FED-639B-468D-A09E-30363D40DE7F}',
	'CombineFeatures' : '{010971C0-0359-4820-A5EA-5EB9E6FFDA76}',
	'CombineFeature' : '{2D0B10A8-711C-4352-AEE1-C8465CBDC36B}',
	'MoveFeatures' : '{972006AB-5037-4850-AF98-8D3B5A55C1F4}',
	'MoveFeature' : '{F0AF7CF3-7F4E-4A34-B384-7C98CE2843B2}',
	'MoveDefinition' : '{61899B80-0F4D-49F5-A3FF-E727155139FD}',
	'FreeDragMoveOperation' : '{279EB42E-C733-4AA9-BFA8-2A8FCF2B2A4D}',
	'MoveAlongRayMoveOperation' : '{8A11BC6C-E0A4-4954-851A-A5E43144046C}',
	'RotateAboutLineMoveOperation' : '{1E4085FD-7428-4EA1-B3EF-B2ADDD7F8F5C}',
	'MoveOperation' : '{BC1B0D6F-086B-43CC-91CC-6BEF7D7E35C1}',
	'BossFeatures' : '{A110C93B-A3B5-4717-A697-87EA0126216F}',
	'BossFeature' : '{16DC54D8-5357-4ECC-9EB5-E4BDD7DB287C}',
	'GrillFeatures' : '{6AC23513-A004-4DC5-B77D-6D18BCB5E43E}',
	'GrillFeature' : '{5EC2AE01-F47C-4E11-B8CD-67A017E07132}',
	'LipFeatures' : '{2AD0B878-13E1-4BB0-BDFF-BBAA7DA553DD}',
	'LipFeature' : '{5404EF69-8B8C-4CCF-BC9B-D9BC8B4F4A2E}',
	'RestFeatures' : '{0E000A5B-67FD-4B23-A312-E6E5F444C045}',
	'RestFeature' : '{669AFAAA-7F38-44FB-B50A-161D5C713C69}',
	'RuleFilletFeatures' : '{9B108AAB-237A-460D-BC99-40FAF5EABD65}',
	'RuleFilletFeature' : '{A783590A-7480-4A9E-BDA3-D805C2CD7281}',
	'SnapFitFeatures' : '{ED254D15-6E11-409A-83A0-BB085F017204}',
	'SnapFitFeature' : '{BC465119-C96D-4E6C-B5FE-AE114280B6A0}',
	'UnwrapFeatures' : '{FACF4224-09C8-4856-A2B8-6EAA1BFCB5CA}',
	'UnwrapFeature' : '{93392430-44EA-4C19-887F-86717E2EDDF8}',
	'UnwrapDefinition' : '{95E4A10F-0335-4C06-8B61-065A485AE9C8}',
	'CoreCavityFeatures' : '{C44DF7B9-A598-407F-AE04-2594D11B9DC7}',
	'CoreCavityFeature' : '{8C1243A8-F557-4626-A5F1-8B9F988B2EFC}',
	'CoreCavityDefinition' : '{6486F293-4BCF-42EA-91A3-08C82ADBED52}',
	'ReferenceComponents' : '{45D64D2D-8D31-4ABD-BB94-E55F0879A90C}',
	'DerivedPartComponents' : '{CF891949-B3AD-4A38-9254-7CAFE0F3B7F6}',
	'DerivedPartComponent' : '{6D7C8AC8-722D-46C8-B6D9-F6001F1EDD2D}',
	'ReferenceFeaturesEnumerator' : '{BEBB7A1A-2E50-4C62-A4E1-64B2E9A18AE6}',
	'DerivedPartDefinition' : '{79B234B7-D73B-43B2-91BC-75A419703C12}',
	'DerivedPartEntities' : '{90A1D182-6B1E-49C2-9DAF-3A74B31BE6D4}',
	'DerivedPartEntity' : '{FB78F43A-8F10-40F3-8C04-62EEA948C716}',
	'Sketches3DEnumerator' : '{EC6AB9BC-0F8E-49E6-B809-09E5962BA707}',
	'SketchBlockDefinitionsEnumerator' : '{14A842C0-8BD2-431B-B1DA-A487A6E35B18}',
	'DerivedPartUniformScaleDef' : '{F41437F2-9B75-4C35-857C-98646F87B551}',
	'DerivedPartTransformDef' : '{11C8C1C5-74AB-415F-AE6B-F358CE0FDA4C}',
	'DerivedPartCoordinateSystemDef' : '{E9AFE0F2-46D5-4022-B668-F0AE494C48B1}',
	'DerivedAssemblyComponents' : '{A52D98FA-2E72-4170-ABB4-6D10C2BCB095}',
	'DerivedAssemblyComponent' : '{A1D2EAAD-28A1-4692-BC13-883879C68894}',
	'DerivedAssemblyDefinition' : '{18DED264-417F-4B81-828C-B8806397C7C3}',
	'DerivedAssemblyOccurrences' : '{DEB206F5-3467-4860-869E-97479BA38D36}',
	'DerivedAssemblyOccurrence' : '{4DEAC0A5-E998-4958-8344-D866385CECF2}',
	'iFeatureTemplateDescriptors' : '{2520A915-6F04-4248-B5A3-05B15E651FD9}',
	'iFeatureComponents' : '{62F5FBCA-EC38-48F5-9CA7-1D38FED4D443}',
	'iFeatureComponent' : '{2B7A8B03-DD00-4DB8-94F9-9BFF87DB8C06}',
	'DerivedAliasComponents' : '{12EC238A-7178-44C6-BF92-F95F87CD7592}',
	'DerivedAliasComponent' : '{61B9A367-8CCB-4868-A573-CCE62C5C35B6}',
	'DerivedFuturePartComponents' : '{1EAA55EA-9631-4A9F-95BA-752C3924E6EF}',
	'DerivedFuturePartComponent' : '{6F9B064A-7DCD-4AD2-ADFD-05B54952C498}',
	'DerivedFuturePartDefinition' : '{3A6CBA65-5300-4F62-BEB6-4C37C22E10E6}',
	'DerivedFutureAssemblyComponents' : '{846AA6A0-434A-42AD-9529-A4D1755802A8}',
	'DerivedFutureAssemblyComponent' : '{566CDFED-4434-47A8-997A-EAD9265A6B9F}',
	'DerivedFutureAssemblyDefinition' : '{5BA9F691-6325-48B1-A248-4A1E46C315B5}',
	'DerivedFutureAssemblyOccurrences' : '{A4B4E128-2739-4B52-8849-1E19DC7AE4C9}',
	'DerivedFutureAssemblyOccurrence' : '{8A641557-B2B8-4D91-9106-177EEC2B9F2E}',
	'ShrinkwrapComponents' : '{6CFEA047-E49B-4BD9-92F6-F982D7AFBBDA}',
	'ShrinkwrapComponent' : '{82917413-0741-40A5-BAAC-B9E244FFE57A}',
	'ShrinkwrapDefinition' : '{AE5289FB-69D3-4331-BC05-0043FB896B45}',
	'Sketches3D' : '{07FB0B7F-D08F-473F-8EF0-A5E6B4CBA3BC}',
	'WorkSurfaces' : '{5987714B-D55A-4AED-8AE5-97C062EC1F68}',
	'WorkSurface' : '{D136B45B-7B03-4027-9759-AECD06393300}',
	'PartEventsObject' : '{CE45B869-6097-4A49-81B4-0FB7A350079C}',
	'PartEventsSink' : '{BABF5BAF-9878-11D4-8DE2-0010B541CAA8}',
	'iPartFactory' : '{B9F30FBA-DABE-4327-AAB3-65E2160135C1}',
	'iPartMember' : '{2DB692B1-9CA2-40CA-AD6B-D1250C063724}',
	'iPartTableRow' : '{A8DB137E-896E-4B61-8813-E49040BBE99E}',
	'iPartTableCell' : '{901E43F5-403A-45C8-A93C-E9509386BB74}',
	'iPartTableColumns' : '{4C9E5B40-4741-4AD9-AACC-47C2BAD5E903}',
	'iPartTableColumn' : '{8B3FEE20-C49D-495B-AA3E-B90AE49B736B}',
	'iPartTableRows' : '{B01CC9E0-93E8-4482-9321-D8F52A7AB213}',
	'SketchBlockDefinitions' : '{BC450138-0F96-4342-BC2C-239747CD4797}',
	'ModelToleranceFeatures' : '{496CD658-85F0-449A-BA13-9B94962ACBEA}',
	'ModelDatumReferenceFrames' : '{10F5BF67-5FAB-44DD-B1D8-BCE056E71000}',
	'ModelDatumReferenceFrame' : '{8227B88D-4834-487E-8DC1-92DACA5D9E02}',
	'ModelDatumReferenceFrameDefinition' : '{E0DA41A0-C0DA-4BA9-807E-ED6514657F7E}',
	'SheetMetalStyles' : '{5B9228F3-FB28-487E-9EC2-D948901CA89F}',
	'SheetMetalStyle' : '{46A4AA12-70D3-4BEC-B059-D285F084B979}',
	'UnfoldMethod' : '{F69435CA-41FA-4FDC-8E07-2D677A30AB2C}',
	'UnfoldMethods' : '{5D0AB9A7-FCDB-4815-837B-BDCADEE5CEB2}',
	'FlatPattern' : '{A7E07EA5-369D-11D6-8E02-0010B541CAA8}',
	'FlatBendResults' : '{1D32B73F-D1F8-4E1C-80B9-590FA6F008B2}',
	'FlatBendResult' : '{F7EC4513-DB91-4D3D-ABB6-699D301F4387}',
	'Bend' : '{AE99EE3F-A9E9-498C-AE33-C919105745F4}',
	'FlatPunchResults' : '{22A94C59-66DE-4B31-BA10-BCBB774B4AAF}',
	'FlatPunchResult' : '{CFC1C004-270D-4C19-BBE5-5D380A2A7D7E}',
	'FlatPatternFeatures' : '{75A1BC5F-78FC-4E62-99C7-623813E36C43}',
	'CornerChamferFeatures' : '{AB61EB61-7785-4854-9498-8210B3DA80B2}',
	'CornerChamferFeature' : '{8B72B033-1F46-4D07-8B26-6E9A718A1533}',
	'CornerChamferDefinition' : '{E16AEA74-FC21-4762-85D9-A4B20B06A095}',
	'CornerRoundFeatures' : '{5908F091-036B-49E5-9685-3228EB2EE3E2}',
	'CornerRoundFeature' : '{3822A30C-5DAB-449B-8AAA-BDA9DEF3FBF5}',
	'CornerRoundDefinition' : '{21BBAED3-F2FD-4A60-9AE4-7A10A8E2BC2D}',
	'CornerRoundEdgeSet' : '{289220CD-E245-473D-B626-114D97F9EDCB}',
	'CutFeatures' : '{994CF5C9-F097-43AB-8741-76D5DD3DC2BA}',
	'CutFeature' : '{CB8542A0-1559-4E06-BAAE-EFA0BFEF86A7}',
	'CutDefinition' : '{3B809336-2821-4E36-B2A1-31B987537E57}',
	'PunchToolFeatures' : '{C08C777F-2E1B-469D-A1A7-E379ED046444}',
	'PunchToolFeature' : '{0DC3C610-F23D-44AD-B688-A47CAB5B04CB}',
	'CosmeticBendFeatures' : '{B534FD24-88CA-435C-95D5-F0DB0FB0238D}',
	'CosmeticBendFeature' : '{B9694561-1C36-4D14-9930-4B8152E1984F}',
	'ASideDefinition' : '{D092DF11-377A-47AA-92DA-664BE32DDDD4}',
	'FlatPatternOrientations' : '{F98E10EB-6BA5-461D-A3D7-5A90CCE47734}',
	'FlatPatternOrientation' : '{830E9463-F267-4A8E-8CE5-8D417295459D}',
	'FlatPatternPlates' : '{BF8CF130-DAD5-444E-9DED-16AD1178DE2F}',
	'FlatPatternPlate' : '{938A5052-5007-48B1-9629-D00898FD6855}',
	'BendsEnumerator' : '{AA1A04EB-B571-4568-86E6-7732B8330E9C}',
	'ASideDefinitions' : '{6047CD23-889D-458D-9AFF-3CD3EB248BAA}',
	'AssemblyJointProxy' : '{4E19FF37-38A9-494F-AC1E-557D5D01CDB4}',
	'_VbaImplementationAssemblyEvents' : '{E12CF633-9F24-427A-A6F9-D5A7D7BCB314}',
	'AssemblySymmetryConstraintProxy' : '{E4FA0888-2179-4CB4-9277-B103A9C40812}',
	'AssemblyWorkAxisDef' : '{F9885CB4-7B68-45E3-953F-B287BE1C6FAF}',
	'AssemblyWorkPlaneDef' : '{62F1DC23-FB86-4D0C-81B3-05BF2CD775F4}',
	'AssemblyWorkPointDef' : '{8E3A45D9-4432-4408-B261-12E725F97A5D}',
	'BendConstraint' : '{AE27E3D2-63C8-4D39-B2CA-A6387AE5D7B3}',
	'BendConstraintProxy' : '{9533BA5C-A32F-45DA-AE06-32EBE35E8CFF}',
	'BendOptions' : '{CA6A960F-9215-4EF3-AFFC-A90D277BEF4F}',
	'BendDefinition' : '{54E4411A-7349-4591-991E-9F930A01EB83}',
	'BendFeature' : '{BBC883B2-B5E1-44C9-A98F-E7221FC17F3D}',
	'BendFeatureProxy' : '{E6885A36-3C1C-43A1-9206-81706779DA32}',
	'BendFeatures' : '{DAA25411-1CB8-4FE2-8F10-1E98740E0889}',
	'BendPartFeatureProxy' : '{D54EA6F2-9FB4-43A3-A0C6-C93AF9991E28}',
	'BIMExchangeServer' : '{6B73769B-1859-4202-87D4-2E508FC9434C}',
	'BossFeatureProxy' : '{C7EAA071-3EFA-4D2F-87BD-C41ABA98C678}',
	'RibFeatureProxy' : '{1F878EE1-06B7-4C7F-9339-920BEFCFE63D}',
	'BoundaryPatchFeatureProxy' : '{6F18AA5B-56B7-4880-90A5-190322278B8D}',
	'CenteredWidthExtent' : '{FE15F632-2312-46D7-86C9-5EEAAC85F7B3}',
	'CentroidWorkPointDef' : '{4286D377-DC30-4195-9A04-E2C5A29AA72A}',
	'ChamferFeatureProxy' : '{0E1AE204-AD92-497C-A48C-979715C3A035}',
	'CircularOccurrencePatternProxy' : '{E6478D92-2EBD-4363-8C27-A6891E942DBB}',
	'CircularPatternFeatureProxy' : '{1CA68293-D200-42E3-B54E-FEB349B302D3}',
	'ClientApplication' : '{CAD5C3C6-C42C-4F1A-A6E2-5D8746198027}',
	'ClientFeatureProxy' : '{EF375552-9B4F-4384-9775-4D4EE910DA33}',
	'ClientFeatureElementProxy' : '{BDC1CFE2-865D-46A5-83C9-8FDAD55EA7F0}',
	'CoilFeatureProxy' : '{ECD82FDD-5B8F-4515-B3CE-1ED92B94C11F}',
	'CoincidentConstraintProxy' : '{C7A68C71-14FA-11D6-8E01-0010B541CAA8}',
	'CoincidentConstraint3DProxy' : '{BFA33A07-C4CE-4CAD-89BC-AF2C49FD5029}',
	'CollinearConstraintProxy' : '{C7A68CD1-14FA-11D6-8E01-0010B541CAA8}',
	'CollinearConstraint3DProxy' : '{4FDD2BD0-33C6-4EB0-90CE-4EEA2B181738}',
	'CombineFeatureProxy' : '{665564D4-83B4-4B86-A365-CAA6B0EBA6C2}',
	'CommandBarButton' : '{E538F3DF-5386-4537-ABDB-82C476C4274D}',
	'CommandBarPopUp' : '{32429DA6-B712-4638-8C53-B1EEE7C1D18B}',
	'CompositeiMateDefinitionProxy' : '{AE0AA5DD-80A7-4094-B58C-06304422CE34}',
	'ConcentricConstraintProxy' : '{C7A68CD3-14FA-11D6-8E01-0010B541CAA8}',
	'ConcentricConstraint3D' : '{EF118F14-C2D2-4DF4-910A-3438FBEC2817}',
	'ConcentricConstraint3DProxy' : '{6B64AAF5-85DF-4FB5-ACAB-717DBBEE7DA4}',
	'ContourFlangeDefinition' : '{8D389B94-12D9-4150-BC67-B64B560E743F}',
	'CornerOptions' : '{37076B79-AB7A-4E6B-8E9D-8D68D28C272E}',
	'ContourFlangeFeature' : '{2390C0D0-A03F-4526-B4B1-7FBFC3C9A66E}',
	'CornerFeature' : '{7DBA9100-AFA9-407A-A91C-A9CC7A079565}',
	'CornerDefinition' : '{F69024F9-970E-4223-82DD-6B4F0E3AF57F}',
	'ContourFlangeFeatureProxy' : '{159DE5F6-0CF1-48F6-87AA-2865091762D3}',
	'ContourFlangeFeatures' : '{A7AF22DD-A689-4BEA-84BF-AEE3496BB26E}',
	'ContourRollFeature' : '{1492BD29-4122-41C8-AA02-B871BC06CCA1}',
	'ContourRollFeatureProxy' : '{206F590B-1854-41A8-9ACE-CB18BCF1154B}',
	'ContourRollFeatures' : '{762B1B03-F049-467E-8BFC-DB28CF0DAD27}',
	'CoreCavityFeatureProxy' : '{71360893-BD99-4D41-96CD-A3BD2AE0DB4D}',
	'CornerChamferFeatureProxy' : '{DDD17D41-9A17-4ADD-BDB2-E2701A524903}',
	'CornerFeatureProxy' : '{64868FC5-AFD9-4602-A5D5-02D93B65BB05}',
	'CornerFeatures' : '{63F4004E-C9FE-4B75-A7CB-F526543A5C29}',
	'CornerRoundFeatureProxy' : '{F8B2175E-285B-4787-B12A-6E485CA1885B}',
	'CosmeticBendFeatureProxy' : '{7958ED54-7E29-490B-9963-BF61E39E98E0}',
	'Weld' : '{FFC0E573-23C5-4DB1-A1DC-F6B12EA2907B}',
	'CosmeticWeldDefinition' : '{D857DD50-A568-4AA5-BB97-DA1B5C460F63}',
	'CosmeticWeld' : '{7338F36B-6CD8-4296-90AE-EFEAC0FED72B}',
	'CosmeticWelds' : '{4A2D7396-8300-4424-B9B7-EB9A8CA5D89E}',
	'CurveAndEntityWorkPointDef' : '{FFFA6714-4FA1-4191-B746-8F0493DF7C06}',
	'CustomConstraintProxy' : '{5E600148-DA27-47DD-8286-E38CC9466B2F}',
	'CustomConstraint3DProxy' : '{5E46D694-BC48-4071-9B6A-8A7F6DDBB685}',
	'CutAcrossBendsExtent' : '{061C46D9-4A71-40EB-9DDC-4D425A6ABE3E}',
	'CutFeatureProxy' : '{58370C0B-5F01-422A-AA66-DC7FD8AAC4CD}',
	'DecalFeatureProxy' : '{3BE697C4-0242-46F3-A420-27E86761D1D7}',
	'DeleteFaceFeatureProxy' : '{FA1ACA84-839B-4F18-97FA-5AA81875B0EB}',
	'DerivedAliasComponentProxy' : '{51182028-01DC-4629-AD22-8BFF0D74FA1A}',
	'DerivedAssemblyComponentProxy' : '{D2E7C9A2-CB9A-4619-B0AA-B7BA2870CDEE}',
	'ShrinkwrapComponentProxy' : '{6D54C427-62E1-4EB9-A4DC-DA926F059819}',
	'DerivedPartComponentProxy' : '{1B986C9A-B329-45B0-B682-95F04FF16E87}',
	'DiameterDimConstraintProxy' : '{C7A68CFB-14FA-11D6-8E01-0010B541CAA8}',
	'DirectionAndDistanceMoveDefinition' : '{080ECFB1-9C78-4A73-8FC9-7A438D08B3A6}',
	'DistanceAndAngleChamferDef' : '{8F25CE45-DF1F-4669-BAA8-E2042ED68811}',
	'DistanceChamferDef' : '{E17AC68F-D333-4DF4-BBAD-BDD9B8377C9C}',
	'DistanceExtent' : '{A7D32953-D38C-4EB4-B9D0-79F7275B37C1}',
	'DistanceFromFaceExtent' : '{335DE8A2-438A-4B8C-B331-18107E0E328F}',
	'DistanceHeightExtent' : '{3C49109C-CDDD-4D4F-A4F3-A0CA3E9EF7F2}',
	'_VbaImplementationDrawingEvents' : '{296442E1-7AB3-46B9-8494-7FBB585F6B50}',
	'DrawingPrintManager' : '{55C72DAA-3307-43D6-89F0-CBF7DD348E4D}',
	'DSServer' : '{457D2D49-6354-461E-AE0F-2C42B371D313}',
	'EdgeWidthExtent' : '{E59EEDF7-48F4-4328-AF62-EBBE19BD09C1}',
	'EllipseRadiusDimConstraintProxy' : '{C7A68CFF-14FA-11D6-8E01-0010B541CAA8}',
	'EmbossFeatureProxy' : '{152C858E-87FE-45AD-867B-80622EF4B8AC}',
	'EndOfFeatures' : '{A89E388A-13C9-4FFA-B777-9C0E1C81F136}',
	'EqualLengthConstraintProxy' : '{C7A68CD9-14FA-11D6-8E01-0010B541CAA8}',
	'EqualRadiusConstraintProxy' : '{C7A68CDB-14FA-11D6-8E01-0010B541CAA8}',
	'EqualConstraint3DProxy' : '{039A89FA-EBE5-4D7D-AC2F-46A67FE7D824}',
	'ExtendFeatureProxy' : '{F057A860-3896-4C4A-87CB-E634F9BA681B}',
	'ExtrudeFeatureProxy' : '{C75F478E-81C5-4E92-BC2A-630E598E34E5}',
	'FaceDraftFeatureProxy' : '{5874F2D8-29C2-4D48-91C2-BB239564CF26}',
	'FaceFeatureDefinition' : '{67BD386A-CC79-48F0-BCFF-6C25FFBF59AA}',
	'FaceFeature' : '{600E3CEE-1600-4999-ACE4-7CED6483BECE}',
	'FaceFeatureProxy' : '{6DEF95B4-C5EF-4FBA-AEE9-B9486F648CAB}',
	'FaceFeatures' : '{C0D71AC3-E085-4A0E-85FF-549C000BA1E7}',
	'FeatureBasedOccurrencePatternProxy' : '{B134AF6F-7FE5-4485-B5E8-493541D94E3F}',
	'FeatureDimensionProxy' : '{57184DE5-2055-47CD-BC40-0277AD066D70}',
	'FeaturePatternElementProxy' : '{B4298554-2144-4054-A4EA-81888D6F6997}',
	'FilletFeatureProxy' : '{4F16A71E-1337-40DE-B13F-DB996F9A716E}',
	'FixedWorkAxisDef' : '{28DD48C5-8D70-11D4-8DDE-0010B541CAA8}',
	'FixedWorkPlaneDef' : '{2C16786F-83FF-11D4-8DDB-0010B541CAA8}',
	'FixedWorkPointDef' : '{28DD48D5-8D70-11D4-8DDE-0010B541CAA8}',
	'FlangeFeature' : '{5475DDC1-3397-46D6-A7A3-E1C34FA5BD7E}',
	'FlangeDefinition' : '{3978BB7A-4A07-475B-BD57-13A05A343EDB}',
	'FlangeFeatureProxy' : '{494427B8-E911-4706-9814-35980AC5621D}',
	'FlangeFeatures' : '{F9B17D1C-6918-44FE-B072-7B4F00CD2BB3}',
	'FlatPatternSettings' : '{F1904548-5E12-4B16-B798-8177BD9F7F38}',
	'FlushConstraintProxy' : '{F36456A4-780C-4CA6-B420-5DBEFFBBCA7D}',
	'FlushiMateDefinitionProxy' : '{2A87493C-AFCD-42D8-A4AE-8385513E63E9}',
	'FoldFeature' : '{4594DFB7-06DB-4707-9F10-B42F740EE37D}',
	'FoldDefinition' : '{0AE09AED-1DFB-41D3-B640-E0E9A24FA8C0}',
	'FoldFeatureProxy' : '{10FCE1AE-95AF-49F4-99FD-B391C181212F}',
	'FoldFeatures' : '{2B564484-AF79-47BF-836B-15F288717791}',
	'FreeformFeatureProxy' : '{FA24DA04-D875-4E23-AD4E-312F5B7EC61A}',
	'DirectEditFeatureProxy' : '{C7FD7CEA-3C30-4BCF-A6E4-A458D3A0F728}',
	'DirectEditOperationProxy' : '{8A4D2830-7D4A-49E5-99BC-3E6C760463E7}',
	'DirectEditMoveOperation' : '{F6A6A22F-70E4-418E-BC65-F39947C6D1E7}',
	'DirectEditMoveOperationProxy' : '{3B833858-7410-47C9-BCAD-F3BE5DEA191D}',
	'DirectEditSizeOperation' : '{047BD59F-24A4-40D2-A47E-6FED9726BA88}',
	'DirectEditSizeOperationProxy' : '{3181BFE4-BAD1-4C7A-9107-114093E4238A}',
	'DirectEditRotateOperation' : '{3913A482-D11A-4B13-A6B1-C1310F935B09}',
	'DirectEditRotateOperationProxy' : '{264513E0-16F5-4AE8-A80D-46EE06D2C99B}',
	'DirectEditDeleteOperation' : '{A7E03766-451A-4BFB-B4CF-FE7F1F258494}',
	'DirectEditDeleteOperationProxy' : '{EAFC6907-44B0-482F-A30F-A46E227A57BC}',
	'DirectEditScaleOperation' : '{D3067CC6-4526-4797-B62D-54AF0E415A47}',
	'DirectEditScaleOperationProxy' : '{BC329A16-2294-4C2D-AEAC-AE61F5433C7B}',
	'FreeMoveDefinition' : '{D26E4888-3FA1-4A45-94E5-AA1A3A41B4AE}',
	'FromToExtent' : '{95852FC2-F171-47D3-9435-A478AFF2353E}',
	'FromToWidthExtent' : '{78E9A7D5-C2AD-48C2-85D5-3A0A58D2FDA5}',
	'FullSweepExtent' : '{9A6F5F04-E0DD-463B-96C3-117B88E7BE25}',
	'GeneralPreferences' : '{9C88D3A8-C3EB-11D3-B79E-0060B0F159EF}',
	'GraphicsPreferences' : '{92353969-0350-11D3-B787-0060B0F159EF}',
	'GrillFeatureProxy' : '{E19AC563-EC57-4E4A-9FE3-35AEB2C6B59A}',
	'GroundConstraintProxy' : '{C7A68CDD-14FA-11D6-8E01-0010B541CAA8}',
	'GroundConstraint3DProxy' : '{F870DE76-265A-4AD2-BACB-5E0137EF0B3A}',
	'HelicalConstraint3D' : '{33E293A8-9DD6-4B9A-8274-E436A3BB3876}',
	'HelicalConstraint3DProxy' : '{5DE610F3-F512-4973-B78A-F50669560B4B}',
	'HemDefinition' : '{532E5229-0B80-4B9B-968F-69BC150C59CC}',
	'HemFeature' : '{D9AB7AE5-6A67-4165-9E0B-0F008C9135B0}',
	'HemFeatureProxy' : '{0F6DEA5E-48E4-49BE-854E-164A89406DDC}',
	'HemFeatures' : '{DF566DD8-E3A3-45E3-844D-78F8C072ECDC}',
	'SingleHemDefinition' : '{BB5A14E9-4213-4965-9B76-F9B33C807FB3}',
	'TeardropHemDefinition' : '{4F1B00F2-FA18-46EA-9C2F-97574189230D}',
	'RolledHemDefinition' : '{F899D5C4-5961-43ED-A66C-E44A186C1B67}',
	'DoubleHemDefinition' : '{C534F040-9826-411E-8C6F-4A73C3A998FC}',
	'HoleFeatureProxy' : '{AD86A222-E8A0-4754-A764-65A958389DF5}',
	'HorizontalAlignConstraintProxy' : '{C7A68CE1-14FA-11D6-8E01-0010B541CAA8}',
	'HorizontalConstraintProxy' : '{C7A68CDF-14FA-11D6-8E01-0010B541CAA8}',
	'ReferenceFeatureProxy' : '{3D65F35E-2F1A-469E-9E5D-E02437A6E3BA}',
	'iFeatureProxy' : '{736ED1B9-7434-4044-B439-EEC1AA84CAAE}',
	'iFeatureEntityInput' : '{84526202-5E30-403F-8700-397646B4BBD0}',
	'iFeatureParameterInput' : '{95B2DD02-374C-41C5-998C-7FCF8BDCA452}',
	'iFeatureSketchPlaneInput' : '{77244784-A1C1-429E-A61F-E6E480B8DFEF}',
	'iFeatureVectorInput' : '{F302D8D2-7DF4-4AD2-9933-9037EB507A90}',
	'iFeatureWorkPlaneInput' : '{F21B5BBF-DBA8-480A-95A6-83D27D52343B}',
	'iMateResultProxy' : '{5EA2744B-95DB-4104-B06A-E9BB6712D59E}',
	'ImportedModelEntities' : '{FC6CACA3-208B-40AD-8B3A-0949B6CBBD3A}',
	'ImportedModelEntity' : '{3F35DB6C-C158-4203-B420-AE4ABCC4B908}',
	'ImportedDWGComponentDefinition' : '{AEFCDC34-A275-44DF-8A40-DF4B0BFD215F}',
	'ImportedDWGLayer' : '{1EC4F1F9-A5A3-4F48-A4D7-071C588F9C8A}',
	'ImportedDWGLayersEnumerator' : '{711D0964-C6EF-4105-B02F-A5D6B14DA971}',
	'ImportedGenericComponent' : '{D2653F5F-C73A-4FAE-9172-EA1B60098B07}',
	'ImportedGenericComponentProxy' : '{B3D5D60A-6CE4-4F7B-A6A6-88A15E433F95}',
	'ImportedGenericComponentDefinition' : '{53196161-A966-4EE7-9080-3F75C7D5876D}',
	'InsertConstraintProxy' : '{35C3BC01-5C75-4BDF-B92E-97205EE57219}',
	'InsertiMateDefinitionProxy' : '{1DC001D8-CAAE-4132-A265-4E17E74A9410}',
	'IntersectionCurveProxy' : '{D2CF1030-CA32-48F6-8865-298BE7E11CCC}',
	'OutOfProcessInventorServerObject' : '{5ABB74D4-90C9-490E-A58F-A2FE0986AFBC}',
	'KnitFeatureProxy' : '{091BB62A-D3D9-4DBE-B8DA-69D51538AC92}',
	'LayoutConstraintProxy' : '{81807A32-C016-4239-8D61-28B44957393D}',
	'LegacyDistanceHeightExtent' : '{31B7388A-3B81-4568-B697-9C1F0D09E7AC}',
	'LineAndFaceWorkPointDef' : '{28DD48CF-8D70-11D4-8DDE-0010B541CAA8}',
	'LineAndPlaneWorkAxisDef' : '{28DD48C3-8D70-11D4-8DDE-0010B541CAA8}',
	'LineAndPointWorkAxisDef' : '{18A18CCA-283E-4E06-9358-1949A91CECF1}',
	'LineAndPointWorkPlaneDef' : '{46785C43-7F4A-11D4-8DDB-0010B541CAA8}',
	'LineAndTangentWorkPlaneDef' : '{2C167869-83FF-11D4-8DDB-0010B541CAA8}',
	'LineLengthDimConstraint3DProxy' : '{2F041963-4B68-415F-BE07-F1FB6C6342A3}',
	'LinePlaneAndAngleWorkPlaneDef' : '{46785C45-7F4A-11D4-8DDB-0010B541CAA8}',
	'LineWorkAxisDef' : '{28DD48B9-8D70-11D4-8DDE-0010B541CAA8}',
	'LipFeatureProxy' : '{8742661B-564A-4CE3-A32C-6F08894FB760}',
	'LoftedFlangeDefinition' : '{C16DE191-DEEC-449E-BEF1-1F1220233FB3}',
	'LoftedFlangeFeature' : '{A7EA6C3E-D3A4-48BB-B600-E8D1097B9A55}',
	'LoftedFlangeFeatureProxy' : '{87DB004A-F974-4BFE-A8BD-65BA290F2D43}',
	'LoftedFlangeFeatures' : '{C14E0C19-443E-41D2-95B5-B46AB974CF0D}',
	'LoftFeatureProxy' : '{D3CB21DB-DF14-45FC-ADD6-8E8EED0AECC3}',
	'Machining' : '{CF3DEE6F-DBB2-4393-A409-5D0ADC6CB12C}',
	'MateConstraintProxy' : '{531B0D86-9BDA-4992-8D31-C42A8788000B}',
	'MateiMateDefinitionProxy' : '{619B5213-A92D-4D4B-BE3F-6CA4B1715A78}',
	'MidpointConstraintProxy' : '{C7A68CE3-14FA-11D6-8E01-0010B541CAA8}',
	'MidpointConstraint3DProxy' : '{2B2BEA0C-F141-4B3E-B061-1B2C8C6B5D9F}',
	'MidPointWorkPointDef' : '{28DD48D3-8D70-11D4-8DDE-0010B541CAA8}',
	'MidSurfaceFeatureProxy' : '{3F96EC38-31B5-46BD-B45D-CA049B450786}',
	'MirrorFeatureProxy' : '{0AD283F9-4020-423B-9C18-A192FEBFA285}',
	'ModelCompositeAnnotationProxy' : '{6BD96D54-7EE0-4E2C-B851-95FA6A9C5236}',
	'ModelDatumIdentifierProxy' : '{B879F99D-E87D-4F95-AD7C-8B6EB246C872}',
	'ModelDatumReferenceFrameProxy' : '{8B7BBAEA-6709-47A4-9C19-946C8D3D21C0}',
	'ModelFeatureControlFrameProxy' : '{E2784ADF-29DA-48AF-BF30-A04DA9B33FF4}',
	'ModelGeneralNoteProxy' : '{0F2F8695-4E4D-465C-B51B-D347C9352AAA}',
	'ModelHoleThreadNoteProxy' : '{4F8CBF41-F056-4F52-862E-4AF730389EE2}',
	'ModelLeaderNoteProxy' : '{95B50D6B-D5AC-4331-8957-ADE73D47785A}',
	'ModelSurfaceTextureSymbolProxy' : '{EE7ED037-D09F-4FC4-BB55-9D7DBB5C52E6}',
	'ModelToleranceFeatureProxy' : '{B0EBE9C5-14C6-4952-A839-B873883547DA}',
	'MoveFaceFeatureProxy' : '{F5CB0108-0E0A-416F-AE41-83FAE56D3D10}',
	'MoveFeatureProxy' : '{70FCCBEE-EF8F-4917-98E0-B26399EAB6CE}',
	'NonLinearEdgeWorkPointDef' : '{25188AF6-308D-4181-879A-1B1084288928}',
	'NonParametricBaseFeatureProxy' : '{0E7B7C43-1EA3-4FA9-95ED-5A1370E81E3F}',
	'NormalToCurveWorkPlaneDef' : '{EEEC1AAC-5A0C-4405-B0A7-63EBCF82A3A3}',
	'NormalToSurfaceWorkAxisDef' : '{B25B8DC2-B557-4E6B-81D2-A7D0C2A992F4}',
	'OffsetConstraint' : '{8006A07C-ECC4-11D4-8DE9-0010B541CAA8}',
	'OffsetConstraintProxy' : '{C7A68CD7-14FA-11D6-8E01-0010B541CAA8}',
	'OffsetDimConstraintProxy' : '{C7A68CF3-14FA-11D6-8E01-0010B541CAA8}',
	'OffsetSplineDimConstraintProxy' : '{B8E1A8FF-EE38-49CD-BC33-FBA4E8E6073C}',
	'OffsetWidthExtent' : '{2EF323DC-CEC7-4E75-9C92-E7571F6653C3}',
	'OnFaceConstraint3DProxy' : '{24339BC2-0B85-4B40-A1DA-1B3473A11B62}',
	'OnFaceCurveProxy' : '{F5C1C3DB-EE51-4B1A-B754-BA0D82974A31}',
	'ParallelConstraintProxy' : '{C7A68CE5-14FA-11D6-8E01-0010B541CAA8}',
	'ParallelConstraint3DProxy' : '{3163F506-342D-4D68-8AB1-39C306DCA6F6}',
	'ParallelToXAxisConstraint3DProxy' : '{071F1650-979B-4FFC-9027-D6E15E251C99}',
	'ParallelToYAxisConstraint3DProxy' : '{01076B1B-C497-401C-B096-23D432B35BF8}',
	'ParallelToZAxisConstraint3DProxy' : '{54759E01-984F-4540-8D3F-82EB1EA6BDD6}',
	'ParallelToXYPlaneConstraint3DProxy' : '{5224F310-1B50-480C-BDB7-DFF90F6068D9}',
	'ParallelToYZPlaneConstraint3DProxy' : '{78671AF0-CC9B-4046-B21E-2FC5F075769F}',
	'ParallelToXZPlaneConstraint3DProxy' : '{205C7990-C5B5-4FE2-BE5C-D5CAC441BF9C}',
	'PartComponentDefinition' : '{DA33F1A3-7C3F-11D3-B794-0060B0F159EF}',
	'PartComponentDefinitions' : '{575F2830-2B6A-11D4-B7A8-0060B0F159EF}',
	'Sketch3DSettings' : '{1D23FF98-1FB3-434F-847F-452217821819}',
	'_VbaImplementationPartEvents' : '{4B98058A-A232-47FD-9186-1070297036FB}',
	'PartDocument' : '{29F0D463-C114-11D2-B77F-0060B0F159EF}',
	'PathProxy' : '{75445952-FFF4-405D-B057-E2EFD1B882BC}',
	'PathAndGuideRailSweepDef' : '{BF000E43-1F0C-464A-A9F3-E1C5EEBA433E}',
	'PathAndGuideSurfaceSweepDef' : '{7D7EAE29-869F-48FB-AD5E-797AB5B87F65}',
	'PathAndSectionTwistsSweepDef' : '{F369E470-65BE-4BB7-B3E8-AB32C9F6CC22}',
	'PathEntityProxy' : '{A19C2D06-4C43-41EC-93EB-AD104ABEE1B9}',
	'PathSweepDef' : '{B7FE7553-8DF0-4F70-9798-C85438D3109E}',
	'PatternConstraint' : '{C173A073-012F-11D5-8DEA-0010B541CAA8}',
	'PatternConstraintProxy' : '{C7A68CF1-14FA-11D6-8E01-0010B541CAA8}',
	'PerpendicularConstraintProxy' : '{C7A68CE7-14FA-11D6-8E01-0010B541CAA8}',
	'PerpendicularConstraint3DProxy' : '{E2CF70B0-55E2-49E6-81AC-41FD6A6C3DB2}',
	'PitchAndHeightCoilExtent' : '{7F1F13A7-39BD-4720-AB79-E17BC3922427}',
	'PitchAndRevolutionCoilExtent' : '{83B2573C-3DBB-44C1-B88D-2D12EF0A9EE2}',
	'PlanarMoveDefinition' : '{501F1ACA-00D4-47CF-A0D1-1F4D1BB1A633}',
	'PlanarSketchProxy' : '{C7A68CBB-14FA-11D6-8E01-0010B541CAA8}',
	'PlaneAndOffsetWorkPlaneDef' : '{2C167867-83FF-11D4-8DDB-0010B541CAA8}',
	'PlaneAndPointWorkPlaneDef' : '{46785C4B-7F4A-11D4-8DDB-0010B541CAA8}',
	'PlaneAndTangentWorkPlaneDef' : '{2C16786B-83FF-11D4-8DDB-0010B541CAA8}',
	'PointAndPlaneDistanceDimConstraint3DProxy' : '{246ADF11-4A5F-43AF-ADDE-440B0532ED2F}',
	'PointAndPlaneWorkAxisDef' : '{28DD48C1-8D70-11D4-8DDE-0010B541CAA8}',
	'PointAndTangentWorkPlaneDef' : '{66E2ABF7-3454-41E6-9115-62879698C194}',
	'RipDefinition' : '{453A1005-42C9-469C-847E-CEA7D550751B}',
	'RipFeature' : '{38D353FC-D30E-4B08-B73A-785787D4D7AD}',
	'PointToPointRipTypeDef' : '{2E264D50-AF7C-4FDE-96DA-12EBD46CAB9B}',
	'PointWorkPointDef' : '{28DD48D1-8D70-11D4-8DDE-0010B541CAA8}',
	'Preparations' : '{1691F301-F2AF-48F4-946F-185CEF9A7EEE}',
	'_VbaImplementationPresentationEvents' : '{33DE76BF-3E58-4EF2-AE90-AA540F2A6C52}',
	'ProfileProxy' : '{C7A68CCB-14FA-11D6-8E01-0010B541CAA8}',
	'Profile3DProxy' : '{75120650-FD69-4DFD-A738-9E5E34F5934B}',
	'ProfileEntityProxy' : '{C7A68CCF-14FA-11D6-8E01-0010B541CAA8}',
	'ProfileEntity3DProxy' : '{BD923BF8-C5DD-4AE4-B577-0988B48FA89D}',
	'ProfilePathProxy' : '{C7A68CCD-14FA-11D6-8E01-0010B541CAA8}',
	'ProfilePath3DProxy' : '{EA49DCCB-E7AE-4B7D-BEAC-80F835167854}',
	'ProjectedCutProxy' : '{1F3DB03A-352E-44EA-807B-8D3C4FCF855C}',
	'PunchToolFeatureProxy' : '{B716CEF3-32C9-4A9A-911D-0D1CF52A74C9}',
	'RadiusDimConstraintProxy' : '{C7A68CFD-14FA-11D6-8E01-0010B541CAA8}',
	'ArcLengthDimConstraintProxy' : '{F0780498-03E3-471D-A733-92EFAC4FF0EE}',
	'RadiusDimConstraint3DProxy' : '{8DD13222-E35F-4EEA-93BA-87F73A069481}',
	'RectangularOccurrencePatternProxy' : '{17FD3E5D-FF18-4E1C-AE86-C9A5A295B2BE}',
	'RectangularPatternFeatureProxy' : '{2A705B9C-82D0-4F14-9137-164642028E77}',
	'RefoldFeature' : '{6FF869B7-4D60-4A01-9CCA-9F5F71433014}',
	'RefoldFeatureProxy' : '{325DB945-8B2D-4574-A023-A2864A85896A}',
	'RefoldFeatures' : '{AD87B241-B3FD-475C-B369-AD3C5D3E3E0D}',
	'ReplaceFaceFeatureProxy' : '{63FB8F95-6B59-4039-B9E1-F6D74E1B3716}',
	'RestFeatureProxy' : '{1B63BB78-7EC2-4D21-A312-A867DCF54110}',
	'RevolutionAndHeightCoilExtent' : '{F0541886-3BF7-4E4D-8A11-D113578E5110}',
	'RevolvedFaceWorkAxisDef' : '{28DD48BF-8D70-11D4-8DDE-0010B541CAA8}',
	'RevolveFeatureProxy' : '{FD16E33C-AE0F-4CB3-8E44-9C6F2A9A8FF6}',
	'RipFeatureProxy' : '{A77799B5-136D-4FEB-9902-CAEC8E122A24}',
	'RipFeatures' : '{8A0202C7-6ADF-454C-AF47-09E3027E8E7C}',
	'RotateRotateConstraintProxy' : '{1753D82F-BEAA-4770-82B9-78FFBF2BEC3D}',
	'RotateRotateiMateDefinitionProxy' : '{D9E903E5-29EE-4164-8701-2CB853CFEE99}',
	'RotateTranslateConstraintProxy' : '{9DFB56E1-F6A4-4D2A-99CE-47CBB8A3145D}',
	'RotateTranslateiMateDefinitionProxy' : '{0BD0BDD4-2716-42A0-B258-09F689CFDFB5}',
	'RuleFilletFeatureProxy' : '{3F51C434-F75E-487F-93A2-5D1438AD5D41}',
	'RuledSurfaceFeatureProxy' : '{1CEE32D6-4997-4E37-ADBB-9AE5873BF30D}',
	'SculptFeatureProxy' : '{78F10980-2892-46CD-8F0E-B709A4835B9B}',
	'UnfoldFeatures' : '{8C80204E-CFE9-43C8-BFAE-4D022F3E2339}',
	'UnfoldFeature' : '{B03877E4-31F6-4B1E-8F38-FCCFD0B0DCAA}',
	'SheetMetalFeatures' : '{41ADE507-16D9-4103-BD0C-FA1C196B9DAA}',
	'ShellFeatureProxy' : '{EE0E6545-A868-4A60-A152-2AF4C5FB44DC}',
	'SilhouetteCurveProxy' : '{49F63CD1-212B-4BCB-B43C-5CAF969A2EAC}',
	'SinglePointRipTypeDef' : '{E8320E6D-E219-4F7C-954C-484A94137FD1}',
	'Sketch3DProxy' : '{FA39B171-CAA5-4FB2-94D0-4E0DF357D13E}',
	'SketchArcProxy' : '{C7A68CC1-14FA-11D6-8E01-0010B541CAA8}',
	'SketchArc3DProxy' : '{856FF591-895A-4A94-9FB1-16F5265C91C8}',
	'SketchBlockProxy' : '{36B9F8B4-FD23-4AC9-A41F-4778F124C0B7}',
	'SketchBlockDefinitionProxy' : '{83C558ED-EC43-41A6-8FCB-36461DF6319B}',
	'SketchCircleProxy' : '{C7A68CC9-14FA-11D6-8E01-0010B541CAA8}',
	'SketchCircle3DProxy' : '{D4B12468-31B2-4885-BE17-B55DE2D561AF}',
	'SketchControlPointSplineProxy' : '{E3757DA9-1C29-477B-838A-B84E896410B2}',
	'SketchControlPointSpline3DProxy' : '{7D3BDDB1-82EF-4AF6-80C2-96BED3462559}',
	'SketchDrivenPatternFeatureProxy' : '{31F0000E-C045-438F-8630-24EC11C60ABC}',
	'SketchEllipseProxy' : '{C7A68CC5-14FA-11D6-8E01-0010B541CAA8}',
	'SketchEllipse3DProxy' : '{A50E48BD-8D0E-4C9A-B3C7-D6EC114ACB3D}',
	'SketchEllipticalArcProxy' : '{C7A68CC7-14FA-11D6-8E01-0010B541CAA8}',
	'SketchEllipticalArc3DProxy' : '{DD3E1C70-8EDA-466B-B455-5CCE10BBA910}',
	'SketchEquationCurveProxy' : '{70180CA4-8BB6-4D2A-B750-E7A17EF35B99}',
	'SketchEquationCurve3DProxy' : '{72DDFCC0-DEBA-46D6-AA95-3B4B91E957F6}',
	'SketchFixedSplineProxy' : '{C5195DC5-0D96-45C2-8E51-BE1A305AC086}',
	'SketchFixedSpline3DProxy' : '{DBABE302-0C4A-4F2D-B67B-768F87C54E32}',
	'SketchImageProxy' : '{0FCBB605-3830-4C3F-95F6-76A4CB15F659}',
	'SketchLineProxy' : '{C7A68CBD-14FA-11D6-8E01-0010B541CAA8}',
	'SketchLine3DProxy' : '{BD020927-670F-4F30-943B-75A2EC87E052}',
	'SketchOffsetSplineProxy' : '{BF18368A-A9B1-4295-9242-18D1AC91F8D3}',
	'SketchPointProxy' : '{C7A68CBF-14FA-11D6-8E01-0010B541CAA8}',
	'SketchPoint3DProxy' : '{9AA5A91E-286C-4F3E-A93D-863BAFD4B80C}',
	'SketchSplineProxy' : '{C7A68CC3-14FA-11D6-8E01-0010B541CAA8}',
	'SketchSpline3DProxy' : '{933CA2AC-EC02-4BA1-9B5B-AFDEDFF20CBF}',
	'SketchSplineHandleProxy' : '{37D2C08C-F2F6-4D4A-9A53-CEBC0A504DA1}',
	'SketchSplineHandle3DProxy' : '{7C693E2E-D4D3-433A-A90F-112E3C52E543}',
	'HelicalCurveProxy' : '{81D122D0-F88A-485C-BFEA-2968E2F3456D}',
	'SmoothConstraintProxy' : '{22324A8F-65DF-48BC-84CD-8A3B457B6A6E}',
	'SmoothConstraint3DProxy' : '{748041B9-77F8-481D-BADA-8F03152C3AF1}',
	'SnapFitFeatureProxy' : '{B13C95CF-8B79-4F03-8EF0-BE81A400529F}',
	'SphereCenterPointWorkPointDef' : '{609506AD-969B-4FEA-9DA5-D2FC535472FA}',
	'SpiralCoilExtent' : '{8D41F569-6407-4C82-A25E-762F6F8AA4B9}',
	'SplineFitPointConstraint' : '{8006A07A-ECC4-11D4-8DE9-0010B541CAA8}',
	'SplineFitPointConstraintProxy' : '{C7A68CD5-14FA-11D6-8E01-0010B541CAA8}',
	'SplineFitPointsConstraint3D' : '{641D6ED0-4DF1-4FA3-B04D-86107C00A62B}',
	'SplineFitPointsConstraint3DProxy' : '{A5F4CA62-8A29-408E-AC56-0B95E44CE781}',
	'SplineLengthDimConstraint3DProxy' : '{A2D2EF5E-37D0-4B0A-8227-F31A60090C8E}',
	'SplitFeatureProxy' : '{38C1B59A-0C1B-4076-A22C-291C34157BBD}',
	'SurfaceTextureANSIDefinition' : '{47B53154-8132-47E5-8733-9D9B4268F21C}',
	'SurfaceTextureBSIDefinition' : '{201C8CF3-0801-49F5-B87E-F39CEA7508D7}',
	'SurfaceTextureDINDefinition' : '{90D115A7-34B8-4E35-9242-8B3FAB10CAB5}',
	'SurfaceTextureGBDefinition' : '{53A282CD-46BF-4A34-BE2D-1CB7FF469B34}',
	'SurfaceTextureGOSTDefinition' : '{0B1630B9-41C0-4DCA-BCBC-2E9D0BA096FE}',
	'SurfaceTextureISODefinition' : '{587A7801-DF86-4DC8-BD20-ADA5FB1193C2}',
	'SurfaceTextureJISDefinition' : '{78B82408-F848-4E5B-A657-67059CC86235}',
	'SweepFeatureProxy' : '{2A5668A8-5EA5-45AE-B3DB-A4C7BD2F7E9D}',
	'SymmetryConstraintProxy' : '{C7A68CE9-14FA-11D6-8E01-0010B541CAA8}',
	'TangentConstraintProxy' : '{25C0112A-8E78-45F9-A50F-3C4E14AB60E2}',
	'TangentConstraint3DProxy' : '{F2BCCD2A-83E0-4528-A039-318A93C7ABBA}',
	'TangentDistanceDimConstraintProxy' : '{C7A68D01-14FA-11D6-8E01-0010B541CAA8}',
	'TangentiMateDefinitionProxy' : '{4FD9CE51-8E4D-4E4B-865F-FC4F0D5A0D5C}',
	'TangentSketchConstraintProxy' : '{C7A68CEB-14FA-11D6-8E01-0010B541CAA8}',
	'TextBoxProxy' : '{C18888BF-ACD9-481C-BE9C-F8921846BE2D}',
	'TextBoxConstraint' : '{037C3FDB-8A3C-443F-8CF6-993D3295335C}',
	'TextBoxConstraintProxy' : '{2F77E2FF-BAD3-43A4-9874-8A99E824E060}',
	'TextBoxDefinitionHandler' : '{92A50081-D0B7-428F-BFF0-B0D277C3AEB0}',
	'ThickenFeatureProxy' : '{D07B4A7B-08EE-4CEA-BC85-525E882714BC}',
	'FaceOffsetFeatureProxy' : '{E139EE45-18F4-404E-972E-08C6008BD225}',
	'ThreadFeatureProxy' : '{DA05EA7F-D509-4D65-AA86-AB596110425C}',
	'ThreePlanesWorkPointDef' : '{28DD48CB-8D70-11D4-8DDE-0010B541CAA8}',
	'ThreePointAngleDimConstraintProxy' : '{C7A68CF9-14FA-11D6-8E01-0010B541CAA8}',
	'ThreePointsWorkPlaneDef' : '{46785C3F-7F4A-11D4-8DDB-0010B541CAA8}',
	'ThroughAllExtent' : '{AFEA608B-F136-4BD1-995B-333BCAFDED08}',
	'ToExtent' : '{C73A295D-CB57-4B32-AA53-652422FACF65}',
	'ToHeightExtent' : '{2C292AFE-8044-4E68-AB51-56340FBF0231}',
	'ToNextExtent' : '{4E5273FA-20B0-41E3-BB29-03BB6C09B0FE}',
	'TorusCenterPointWorkPointDef' : '{E205D028-CE6C-4BE5-AE33-AB6F9770D869}',
	'TorusMidPlaneWorkPlaneDef' : '{662FBA92-6903-4455-9395-207E48749986}',
	'TransitionalConstraintProxy' : '{9E7FC002-194A-4CB7-9862-4A3308F586C8}',
	'TranslateTranslateConstraint' : '{6D92FD04-C569-4F19-8A54-A83B1CBA7080}',
	'TranslateTranslateConstraintProxy' : '{FBC6B272-3033-4F57-8279-7D70F3FFD508}',
	'TranslatorAddIn' : '{6ECCBC87-A50D-11D4-8DE4-0010B541CAA8}',
	'TranslatorAddInServer' : '{6ECCBC7F-A50D-11D4-8DE4-0010B541CAA8}',
	'TrimFeatureProxy' : '{7BCA4B05-379A-4960-BE68-236689EDAEF1}',
	'TwoDistancesChamferDef' : '{5B7A8CDA-6F27-4396-9E39-C21A67CA03D3}',
	'TwoLineAngleDimConstraintProxy' : '{C7A68CF7-14FA-11D6-8E01-0010B541CAA8}',
	'TwoLineAngleDimConstraint3DProxy' : '{407A9D14-6E3A-4F39-9AD6-CDD8873B9FCB}',
	'TwoLinesWorkPlaneDef' : '{46785C41-7F4A-11D4-8DDB-0010B541CAA8}',
	'TwoLinesWorkPointDef' : '{28DD48CD-8D70-11D4-8DDE-0010B541CAA8}',
	'TwoPlanesWorkAxisDef' : '{28DD48BB-8D70-11D4-8DDE-0010B541CAA8}',
	'TwoPlanesWorkPlaneDef' : '{C0E159EB-2FFE-483E-B4CE-585BEE76E710}',
	'TwoPointDistanceDimConstraintProxy' : '{C7A68CF5-14FA-11D6-8E01-0010B541CAA8}',
	'TwoPointDistanceDimConstraint3DProxy' : '{5B29EB3A-F2F2-4998-B713-03042554E46C}',
	'TwoPointsWorkAxisDef' : '{28DD48BD-8D70-11D4-8DDE-0010B541CAA8}',
	'UnfoldFeatureProxy' : '{550A5700-23FB-4E1F-98D6-5BD7D9701ACD}',
	'UnwrapFeatureProxy' : '{5E480B67-C221-4DB3-B6CF-976A72FCD09B}',
	'VerticalAlignConstraintProxy' : '{C7A68CEF-14FA-11D6-8E01-0010B541CAA8}',
	'VerticalConstraintProxy' : '{C7A68CED-14FA-11D6-8E01-0010B541CAA8}',
	'VirtualComponentDefinition' : '{D4652AC1-D4B9-4D65-8C2B-942D74411B1C}',
	'WeldBead' : '{D8DEC5C0-4E92-4D60-B107-6D5FBBA9923A}',
	'WeldBeads' : '{F44EE9AE-7D98-49C7-8634-700050114F38}',
	'Welds' : '{F3C8A2A2-E9DF-454D-8769-8544374BB882}',
	'WeldsComponentDefinition' : '{268D663B-4B37-11D6-8E06-0010B541CAA8}',
	'WeldmentComponentDefinition' : '{9A750C49-0384-4CD8-B1D9-DAADD3E28657}',
	'WidthOffsetWidthExtent' : '{91578449-A1E5-4865-BF53-D297549308B0}',
	'WorkAxisProxy' : '{3CBE8AA5-3D92-11D5-8DEE-0010B541CAA8}',
	'WorkPlaneProxy' : '{3CBE8A9F-3D92-11D5-8DEE-0010B541CAA8}',
	'WorkPointProxy' : '{3CBE8AA7-3D92-11D5-8DEE-0010B541CAA8}',
	'WorkSurfaceProxy' : '{9A104FEF-2749-4112-AA6D-937CB4F44420}',
	'UserCoordinateSystemProxy' : '{85577108-087D-4E36-994A-48CA4F1D2AB9}',
	'PointCloudProxy' : '{4EDC3AD5-669B-40A9-A3DC-3261C16F4642}',
	'PointCloudPoint' : '{3485FEA9-8865-44EE-8F03-72F46DAB0634}',
	'PointCloudPointProxy' : '{50325C62-766C-41C2-A97C-8951BD4D0E56}',
	'PointCloudPlane' : '{6B3ECB2F-78BA-492E-9235-E68EA88F66E9}',
	'PointCloudPlaneProxy' : '{E65DEA7B-63C6-4F6E-9FCE-8177FEE904F9}',
	'DWGBlockDefinition' : '{50E1E017-584C-4C7D-8001-4CF9AEAB7E5E}',
	'DWGArcsEnumerator' : '{F5CC3DD7-BC15-476C-853B-3E63BA66A29B}',
	'DWGArc' : '{6D0B30F0-4279-46EC-8D96-EDD140C3EC72}',
	'ImportedDWGComponent' : '{DF1920AB-6CC5-4C6A-AA29-F4D3B0A30BA6}',
	'DWGEntity' : '{6B46D5EC-57DE-414D-8ACC-EF1E7C6C1AAF}',
	'DWGBlockReferencesEnumerator' : '{E2012607-EC0A-4F31-A888-E389AF5667E7}',
	'DWGBlockReference' : '{942BDD59-6622-4CF0-BAD6-4F4EAD7A4DCA}',
	'DWGEllipticalArcsEnumerator' : '{E825D13E-DAE3-4CA1-A275-5C0A62A67E6B}',
	'DWGEllipticalArc' : '{E9455662-85DE-499A-9965-81270D314D70}',
	'DWGEntitiesEnumerator' : '{5F9B0BEB-E30C-4750-A733-1FCFE4218750}',
	'DWGLinesEnumerator' : '{C70B926C-2519-4760-B513-DB4FD170208A}',
	'DWGLine' : '{18F5F2F4-26CB-49E9-A105-F83638FEFB3E}',
	'DWGPointsEnumerator' : '{19B7AC3A-9E5C-424E-AE7D-33B805717AF5}',
	'DWGPoint' : '{CE96A92D-B3F9-4607-9E47-30722770F9AD}',
	'DWGPolylinesEnumerator' : '{E25D1002-8B00-4E7A-A6F3-DF7BDCC7A63A}',
	'DWGPolyline' : '{249D0F99-CAD8-4B05-9A8C-AAF415CEA2DC}',
	'DWGEntitySegmentsEnumerator' : '{F813785A-FF19-40AC-B383-EC47CB8EBF15}',
	'DWGEntitySegment' : '{34F5AE9B-CDD6-49ED-B3AD-AEFB61DD9DC0}',
	'DWGPolylines2DEnumerator' : '{8C2B0FE6-3B3F-4897-BD44-806DA59E436A}',
	'DWGPolyline2D' : '{AD47616F-A657-4363-AB07-360A1A38AD44}',
	'DWGPolylines3DEnumerator' : '{7CC584DD-262F-45D6-A383-6705655F2435}',
	'DWGPolyline3D' : '{BC6242DB-ABCC-4605-8A0F-9A42F26F9D9C}',
	'DWGSplinesEnumerator' : '{0FEC3515-6F9A-4BFB-BD87-7070E60B0010}',
	'DWGSpline' : '{A19EC228-CE1D-4B2D-BE30-584AF42A18AA}',
	'DWGACMStandardPartsEnumerator' : '{AED943D3-0351-4161-8916-0E99234DA2F8}',
	'DWGACMStandardPart' : '{9EF3521A-24B6-4CE5-8A36-543E8E6C4D4F}',
	'DWGAcadSupportedProxiesEnumerator' : '{EC661E99-6315-4974-99F8-7018045C351F}',
	'DWGAcadSupportedProxy' : '{E1FDDE0A-AAFB-4069-8266-D6389559A1A3}',
	'ImportedDWGComponentProxy' : '{B1EECF0D-991E-44FD-8244-61AB5E826B35}',
	'DWGEntityProxy' : '{7A458570-4422-40E6-B40E-008C2183AF1C}',
	'DWGBlockReferenceProxy' : '{93545775-90CE-4E69-B0A5-4E3F23C30677}',
	'DWGBlockDefinitionProxy' : '{518CD473-78CC-4B12-A831-AE93812A2774}',
	'DWGArcProxy' : '{E5CFA472-5D23-4486-8D2C-A4D8D564C196}',
	'DWGEllipticalArcProxy' : '{5EE74326-54FB-4C26-97AD-B78830B6E0C0}',
	'DWGLineProxy' : '{7EB60BBC-FF1C-428E-BB89-5F69BD727E83}',
	'DWGPointProxy' : '{BA9FAF37-B4D2-45C1-BBBE-78E7B8ECB219}',
	'DWGPolylineProxy' : '{6755F53A-DF74-4D7A-AB08-340C5AAD6F5C}',
	'DWGSplineProxy' : '{EF97259E-0689-42D1-AFAC-1FFD9F6A1980}',
	'DWGPolyline2DProxy' : '{C5A7AC9D-A15D-46B9-8582-31BD4E8D05CD}',
	'DWGPolyline3DProxy' : '{078D1300-9A94-4644-BB80-BFD3B4600F3A}',
	'DWGACMStandardPartProxy' : '{A3DF761A-289E-4DBA-9BBE-4FC0A9665559}',
	'DWGAcadSupportedProxyProxy' : '{3E8A1835-A481-4153-A44C-8B75A94A5C05}',
	'DWGEntitySegmentProxy' : '{3CDDC905-E3FD-4255-890B-028E2523B0BF}',
	'DWGEntityArcSegment' : '{143A4592-E2D5-47BD-9161-9CD37E6948F9}',
	'DWGEntityArcSegmentProxy' : '{6DB61529-F8A8-46C6-988A-3E37306EAEC7}',
	'DWGEntityEllipticalArcSegment' : '{D27C87CF-D6D4-4B7C-BE3F-04623C44910D}',
	'DWGEntityEllipticalArcSegmentProxy' : '{6DEC7317-ECC4-4007-9FAF-E1F7A570A2D2}',
	'DWGEntityLineSegment' : '{5B34AC50-EB91-4C51-AD13-6D9994BF1C62}',
	'DWGEntityLineSegmentProxy' : '{E66320B8-E8EC-499F-AB2D-ACC633020A1C}',
	'DWGEntitySplineSegment' : '{B19DEB3B-9A69-4BAC-AEBB-20B92FD93B16}',
	'DWGEntitySplineSegmentProxy' : '{66345F07-0F3F-4480-9D7F-80493F361595}',
	'MeshFeatureProxy' : '{C2F5F99E-12F8-4AC2-9DC8-74F076FE9036}',
	'MeshFeatureSetProxy' : '{873C598A-4E73-4BC1-BFF2-8370A1CDC935}',
	'MeshFeatureEntityProxy' : '{8D2C37E8-0C75-4B02-A09D-93F648E72CE7}',
	'MeshFace' : '{FEA9A836-D065-45BD-9898-564E67B5F11A}',
	'MeshFaceProxy' : '{EDE2434F-2FED-4902-82B0-8112FD7079C1}',
	'MeshEdge' : '{46BC8F99-10AF-4045-AADB-79A062E6508A}',
	'MeshEdgeProxy' : '{AAE3F8BA-A09D-4788-B4E3-F637183206DA}',
	'MeshVertex' : '{3C6AA9D5-971C-4753-9293-4E806CA49074}',
	'MeshVertexProxy' : '{D94E7C45-598A-4EA3-AD99-F4562C267BA3}',
	'PublicationMeshEdge' : '{A697A765-A9A9-4ACC-842D-4071034B9BCB}',
	'PublicationMeshFace' : '{4B3E3AD0-F07C-4CD0-A184-EA58A11EB9B3}',
	'PublisherServer' : '{A8B09AA7-B712-47AC-B188-00B659E84903}',
	'PresentationTrailSegmentsEnumerator' : '{F08B385C-86E0-4A1A-9E06-5A30BBE96ACB}',
	'DerivedFuturePartComponentProxy' : '{E06DD476-868C-43C7-A3F5-3D624ADD40AF}',
	'DerivedFutureAssemblyComponentProxy' : '{27802D7B-DD17-4A6E-9889-99BB57A833E2}',
	'IPictureDisp' : '{7BF80981-BF32-101A-8BBB-00AA00300CAB}',
	'IRxDocumentEvents' : '{70109AA7-63C1-11D2-B78B-0060B0EC020B}',
	'IRxApplicationEvents' : '{70109AA8-63C1-11D2-B78B-0060B0EC020B}',
	'IRxUserInputEvents' : '{9235396C-0350-11D3-B787-0060B0F159EF}',
	'IRxFileAccessEvents' : '{32E4A318-C5E8-11D2-B77F-0060B0F159EF}',
	'IRxTransactionEvents' : '{AE277671-2FDC-11D3-B78F-0060B0F159EF}',
	'IRxFileUIEvents' : '{70109AA6-63C1-11D2-B78B-0060B0EC020B}',
	'IRxSurfaceBody' : '{5DF86067-6B16-11D3-B794-0060B0F159EF}',
	'IRxEnumFaceShells' : '{5DF86071-6B16-11D3-B794-0060B0F159EF}',
	'IRxFaceShell' : '{5DF86068-6B16-11D3-B794-0060B0F159EF}',
	'IRxEnumFaces' : '{5DF86072-6B16-11D3-B794-0060B0F159EF}',
	'IRxFace' : '{5DF86069-6B16-11D3-B794-0060B0F159EF}',
	'IRxEnumEdgeLoops' : '{5DF86073-6B16-11D3-B794-0060B0F159EF}',
	'IRxEdgeLoop' : '{5DF8606A-6B16-11D3-B794-0060B0F159EF}',
	'IRxEnumEdgeUses' : '{5DF86074-6B16-11D3-B794-0060B0F159EF}',
	'IRxEdgeUse' : '{5DF8606B-6B16-11D3-B794-0060B0F159EF}',
	'IRxEdge' : '{5DF8606C-6B16-11D3-B794-0060B0F159EF}',
	'IRxVertex' : '{5DF8606D-6B16-11D3-B794-0060B0F159EF}',
	'IRxEnumEdges' : '{5DF86075-6B16-11D3-B794-0060B0F159EF}',
	'IRxCurveEvaluator' : '{5DF8603C-6B16-11D3-B794-0060B0F159EF}',
	'IRxBox' : '{5DF8602A-6B16-11D3-B794-0060B0F159EF}',
	'IRxPoint' : '{CB69F15D-558E-11D3-B793-0060B0F159EF}',
	'IRxCurve2dEvaluator' : '{5DF8603D-6B16-11D3-B794-0060B0F159EF}',
	'IRxBox2d' : '{5DF8602B-6B16-11D3-B794-0060B0F159EF}',
	'IRxPoint2d' : '{CB69F15E-558E-11D3-B793-0060B0F159EF}',
	'IRxEnumVertices' : '{5DF86076-6B16-11D3-B794-0060B0F159EF}',
	'IRxSurfaceEvaluator' : '{5DF8606E-6B16-11D3-B794-0060B0F159EF}',
	'IRxComponentDefinition' : '{5DF8600D-6B16-11D3-B794-0060B0F159EF}',
	'IRxEnumSurfaceBodies' : '{5DF86070-6B16-11D3-B794-0060B0F159EF}',
	'IRxEnumComponentOccurrences' : '{5DF86012-6B16-11D3-B794-0060B0F159EF}',
	'IRxComponentOccurrence' : '{9D7CECDD-2CF1-11D4-B7A8-0060B0F159EF}',
	'IRxComponentOccurrenceOld' : '{5DF8600F-6B16-11D3-B794-0060B0F159EF}',
	'IRxMatrix' : '{CB69F15B-558E-11D3-B793-0060B0F159EF}',
	'IRxReferenceKey' : '{5DF86026-6B16-11D3-B794-0060B0F159EF}',
	'IRxGeometryProxy' : '{5DF86010-6B16-11D3-B794-0060B0F159EF}',
	'IRxEnumComponentDefinitionReferences' : '{5DF86013-6B16-11D3-B794-0060B0F159EF}',
	'IRxComponentDefinitionReference' : '{5DF8600E-6B16-11D3-B794-0060B0F159EF}',
	'IRxComponentDocument' : '{5DF8600C-6B16-11D3-B794-0060B0F159EF}',
	'IRxEnumComponentDefinitions' : '{5DF86011-6B16-11D3-B794-0060B0F159EF}',
	'IRxAlternateSurfaceBody' : '{5DF8606F-6B16-11D3-B794-0060B0F159EF}',
	'IRxApplicationAddIn' : '{E3571291-DB40-11D2-B783-0060B0F159EF}',
	'IRxEnumApplicationAddIns' : '{E3571290-DB40-11D2-B783-0060B0F159EF}',
	'IRxBSplineCurve' : '{5DF86032-6B16-11D3-B794-0060B0F159EF}',
	'IRxBSplineCurve2d' : '{5DF86033-6B16-11D3-B794-0060B0F159EF}',
	'IRxBSplineSurface' : '{5DF8609C-6B16-11D3-B794-0060B0F159EF}',
	'IRxUnitVector' : '{CB69F161-558E-11D3-B793-0060B0F159EF}',
	'IRxCircle' : '{5DF8602E-6B16-11D3-B794-0060B0F159EF}',
	'IRxCircle2d' : '{5DF8602F-6B16-11D3-B794-0060B0F159EF}',
	'IRxCone' : '{5DF86099-6B16-11D3-B794-0060B0F159EF}',
	'IRxCylinder' : '{5DF86098-6B16-11D3-B794-0060B0F159EF}',
	'IRxVector' : '{CB69F15F-558E-11D3-B793-0060B0F159EF}',
	'IRxEllipseFull' : '{5DF86030-6B16-11D3-B794-0060B0F159EF}',
	'IRxVector2d' : '{CB69F160-558E-11D3-B793-0060B0F159EF}',
	'IRxEllipseFull2d' : '{5DF86031-6B16-11D3-B794-0060B0F159EF}',
	'IRxEllipticalCone' : '{97ED8AED-EF9D-11D3-B7A2-0060B0F159EF}',
	'IRxEllipticalCylinder' : '{FA34A3FE-F063-11D3-B7A2-0060B0F159EF}',
	'IRxEnumComponentDocuments' : '{59D3FA3B-ACE0-11D3-B79A-0060B0F159EF}',
	'IRxReferencedFileDescriptor' : '{00C8476D-E79F-11D2-B785-0060B0F159EF}',
	'IRxFileAndReferences' : '{D4606260-75D8-48EA-A3C3-A971E2384118}',
	'IRxFileAndReferencesOld2' : '{C0E7110B-2136-11D4-8DD0-0010B541CAA8}',
	'IRxFileAndReferencesOld' : '{023BEB56-898C-11D2-86B1-080009DB6864}',
	'IRxEnumFileAndReferences' : '{2C9F9B60-8967-11D2-86B1-080009DB6864}',
	'IRxEnumReferencedFileDescriptors' : '{00C8476F-E79F-11D2-B785-0060B0F159EF}',
	'IRxEnumReferencedOLEFileDescriptors' : '{9CAF9897-33EA-11D3-B78F-0060B0F159EF}',
	'IRxReferencedOLEFileDescriptor' : '{9CAF9896-33EA-11D3-B78F-0060B0F159EF}',
	'IRxPropertySets' : '{73F35CCB-ED6E-11D2-B785-0060B0F159EF}',
	'IRxPropertySet' : '{73F35CCD-ED6E-11D2-B785-0060B0F159EF}',
	'IRxProperty' : '{73F35CCF-ED6E-11D2-B785-0060B0F159EF}',
	'IRxEnumReferenceKeys' : '{5DF86027-6B16-11D3-B794-0060B0F159EF}',
	'IRxFacetsOld' : '{CB69F159-558E-11D3-B793-0060B0F159EF}',
	'IRxFacets' : '{2894395B-1E28-4516-8308-6AD0911B83D5}',
	'IRxFileLocations' : '{42C7E0BF-FDCF-11D2-B785-0060B0F159EF}',
	'IRxGeometricLocate' : '{5DF86015-6B16-11D3-B794-0060B0F159EF}',
	'IRxLine' : '{CB69F163-558E-11D3-B793-0060B0F159EF}',
	'IRxUnitVector2d' : '{CB69F162-558E-11D3-B793-0060B0F159EF}',
	'IRxLine2d' : '{CB69F164-558E-11D3-B793-0060B0F159EF}',
	'IRxMatrix2d' : '{CB69F15C-558E-11D3-B793-0060B0F159EF}',
	'IRxPlane' : '{5DF86097-6B16-11D3-B794-0060B0F159EF}',
	'IRxReferenceKeyManager' : '{5DF86028-6B16-11D3-B794-0060B0F159EF}',
	'IStream' : '{0000000C-0000-0000-C000-000000000046}',
	'ISequentialStream' : '{0C733A30-2A1C-11CE-ADE5-00AA0044773D}',
	'IEnumUnknown' : '{00000100-0000-0000-C000-000000000046}',
	'IRxSphere' : '{5DF8609A-6B16-11D3-B794-0060B0F159EF}',
	'IRxStrokesOld' : '{CB69F15A-558E-11D3-B793-0060B0F159EF}',
	'IRxStrokes' : '{DAEA25A5-513E-41CA-BB8F-8E88B507C52E}',
	'IRxTorus' : '{5DF8609B-6B16-11D3-B794-0060B0F159EF}',
	'IRxTransientGeometry' : '{C1B42715-92E9-4278-BD5F-6DCE4B25FEBE}',
	'IRxApprenticeServer' : '{95105315-340B-4406-AAB1-2039EAA23E7D}',
	'IRxApprenticeServerOld' : '{0A5CE3AB-073D-11D4-B7A4-0060B0F159EF}',
	'IRxFileSaveAs' : '{42C7E0BE-FDCF-11D2-B785-0060B0F159EF}',
	'IPersistFile' : '{0000010B-0000-0000-C000-000000000046}',
	'IPersist' : '{0000010C-0000-0000-C000-000000000046}',
	'IRxApplicationAddInSiteOld' : '{E3571297-DB40-11D2-B783-0060B0F159EF}',
	'IRxApplicationAddInSite' : '{6A2718FD-4CCB-46D8-857A-CB83113FD4B9}',
	'IRxApplicationAddInServer' : '{E3571292-DB40-11D2-B783-0060B0F159EF}',
	'IRxTranslatorAddInServer' : '{6ECCBC7B-A50D-11D4-8DE4-0010B541CAA8}',
	'IRxTranslatorAddInServer2' : '{863741CF-1A34-11D5-8DEC-0010B541CAA8}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

