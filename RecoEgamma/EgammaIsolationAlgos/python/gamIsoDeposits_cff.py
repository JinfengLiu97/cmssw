import FWCore.ParameterSet.Config as cms

from RecoEgamma.EgammaIsolationAlgos.egammaIsoSetup_cff import *

from RecoEgamma.EgammaIsolationAlgos.gamIsoDepositTk_cff import *
from RecoEgamma.EgammaIsolationAlgos.gamIsoDepositEcalFromHits_cff import *
from RecoEgamma.EgammaIsolationAlgos.gamIsoDepositHcalFromTowers_cff import *

gamIsoDepositsTask = cms.Task(
    gamIsoDepositTk , 
    gamIsoDepositEcalFromHits , 
    gamIsoDepositHcalFromTowers ,
    gamIsoDepositHcalDepth1FromTowers ,
    gamIsoDepositHcalDepth2FromTowers
)
