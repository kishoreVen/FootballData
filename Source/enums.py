from enum import Enum

# EGameResult - Enum that represents possible game results
# W - Win, T - Tie, L - Loss
class EGameResult(Enum):
    W = 0
    T = 1
    L = 2

class EGameLoc(Enum):
    HOME = 0
    AWAY = 1

class EFootballTeams(Enum):
    ARI = 0
    ATL = 1
    BAL = 2
    BUF = 3
    CAR = 4
    CHI = 5
    CIN = 6
    CLE = 7
    DAL = 8
    DEN = 9
    DET = 10
    GB  = 11
    HOU = 12
    IND = 13
    JAX = 14
    KC  = 15
    MIA = 16
    MIN = 17
    NE  = 18
    NO  = 19
    NYG = 20
    NYJ = 21
    OAK = 22
    PHI = 23
    PIT = 24
    SD  = 25
    SEA = 26
    SF  = 27
    STL = 28
    TB  = 29
    TEN = 30
    WAS = 31
    NUM = 32

    def find(value):
        value = value.upper()
        for teamacronym in EFootballTeams:
            if teamacronym.name == value:
                return teamacronym

        return EFootballTeams.NUM

