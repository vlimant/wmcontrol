# Auto generated configuration file
# using: 
# Revision: 1.381.2.13 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: STEP1 --step DIGI,L1,DIGI2RAW,HLT:7E33v2 --conditions START53_V16::All --geometry DB:ExtendedHFLibraryNoCastor --datamix NODATAMIXER --eventcontent RAWDEBUG --datatier GEN-SIM-RAWDEBUG --customise Configuration/GenProduction/noCastorHFSL_customise.customise_digi -n -10 --no_exec --inline_custom
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_7E33v2_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-10)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring('file:STEP1_SIM.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.13 $'),
    annotation = cms.untracked.string('STEP1 nevts:-10'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RAWDEBUGoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWDEBUGEventContent.outputCommands,
    fileName = cms.untracked.string('STEP1_DIGI_L1_DIGI2RAW_HLT.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-RAWDEBUG')
    )
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'START53_V16::All', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWDEBUGoutput_step = cms.EndPath(process.RAWDEBUGoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.RAWDEBUGoutput_step])

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC

def customizeHLTforMC(process):
  """adapt the HLT to run on MC, instead of data
  see Configuration/StandardSequences/Reconstruction_Data_cff.py
  which does the opposite, for RECO"""

  # CSCHaloDataProducer - not used at HLT
  #if 'CSCHaloData' in process.__dict__:
  #  process.CSCHaloData.ExpectedBX = cms.int32(6)

  # EcalUncalibRecHitProducer - not used at HLT
  #if 'ecalGlobalUncalibRecHit' in process.__dict__:
  #  process.ecalGlobalUncalibRecHit.doEBtimeCorrection = cms.bool(False)
  #  process.ecalGlobalUncalibRecHit.doEEtimeCorrection = cms.bool(False)

  # HcalRecAlgoESProducer - these flags are not used at HLT (they should stay set to the default value for both data and MC)
  #if 'hcalRecAlgos' in process.__dict__:
  #  import RecoLocalCalo.HcalRecAlgos.RemoveAddSevLevel as HcalRemoveAddSevLevel
  #  HcalRemoveAddSevLevel.AddFlag(process.hcalRecAlgos, "HFDigiTime",     8)
  #  HcalRemoveAddSevLevel.AddFlag(process.hcalRecAlgos, "HBHEFlatNoise",  8)
  #  HcalRemoveAddSevLevel.AddFlag(process.hcalRecAlgos, "HBHESpikeNoise", 8)

  # PFRecHitProducerHCAL
  if 'hltParticleFlowRecHitHCAL' in process.__dict__:
    process.hltParticleFlowRecHitHCAL.ApplyPulseDPG      = cms.bool(False)
    process.hltParticleFlowRecHitHCAL.LongShortFibre_Cut = cms.double(1000000000.0)

  return process

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# Automatic addition of the customisation function from Configuration.GenProduction.noCastorHFSL_customise

def customise_gensim(process): 

    # extended geometric acceptance (full CASTOR acceptance)

    process.g4SimHits.Generator.MinEtaCut = cms.double(-6.7)
    process.g4SimHits.Generator.MaxEtaCut = cms.double(6.7)

    # use HF shower library instead of GFlash parameterization

    process.g4SimHits.HCalSD.UseShowerLibrary = cms.bool(True)
    process.g4SimHits.HCalSD.UseParametrize = cms.bool(False)
    process.g4SimHits.HCalSD.UsePMTHits = cms.bool(False)
    process.g4SimHits.HCalSD.UseFibreBundleHits = cms.bool(False)
    process.g4SimHits.HFShower.ApplyFiducialCut = cms.bool(True)
    process.g4SimHits.HFShowerLibrary.ApplyFiducialCut = cms.bool(False)
      
    return(process)

def customise_digi(process):

    process.mix.mixObjects.mixCH = cms.PSet(
        input = cms.VInputTag(cms.InputTag("g4SimHits","CaloHitsTk"), cms.InputTag("g4SimHits","EcalHitsEB"), cms.InputTag("g4SimHits","EcalHitsEE"), cms.InputTag("g4SimHits","EcalHitsES"), cms.InputTag("g4SimHits","EcalTBH4BeamHits"), cms.InputTag("g4SimHits","HcalHits"), cms.InputTag("g4SimHits","HcalTB06BeamHits"), cms.InputTag("g4SimHits","ZDCHITS")),
        type = cms.string('PCaloHit'),
        subdets = cms.vstring('CaloHitsTk',
            'EcalHitsEB',      
            'EcalHitsEE',      
            'EcalHitsES',      
            'EcalTBH4BeamHits',
            'HcalHits',        
            'HcalTB06BeamHits',
            'ZDCHITS')         
    )
    process.calDigi = cms.Sequence(process.ecalDigiSequence+process.hcalDigiSequence)
    process.DigiToRaw = cms.Sequence(process.csctfpacker+process.dttfpacker+process.gctDigiToRaw+process.l1GtPack+process.l1GtEvmPack+process.siPixelRawData+process.SiStripDigiToRaw+process.ecalPacker+process.esDigiToRaw+process.hcalRawData+process.cscpacker+process.dtpacker+process.rpcpacker+process.rawDataCollector)

    return(process) 

def customise_validation(process):

    process.mix.mixObjects.mixCH = cms.PSet(
        input = cms.VInputTag(cms.InputTag("g4SimHits","CaloHitsTk"), cms.InputTag("g4SimHits","EcalHitsEB"), cms.InputTag("g4SimHits","EcalHitsEE"), cms.InputTag("g4SimHits","EcalHitsES"), cms.InputTag("g4SimHits","EcalTBH4BeamHits"), cms.InputTag("g4SimHits","HcalHits"), cms.InputTag("g4SimHits","HcalTB06BeamHits"), cms.InputTag("g4SimHits","ZDCHITS")),
        type = cms.string('PCaloHit'),
        subdets = cms.vstring('CaloHitsTk',
            'EcalHitsEB',      
            'EcalHitsEE',      
            'EcalHitsES',      
            'EcalTBH4BeamHits',
            'HcalHits',        
            'HcalTB06BeamHits',
            'ZDCHITS')         
    )

    return(process)

#call to customisation function customise_digi imported from Configuration.GenProduction.noCastorHFSL_customise
process = customise_digi(process)

# End of customisation functions
