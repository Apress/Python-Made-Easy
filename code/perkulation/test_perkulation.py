from perkulation import *

def test_periodische_nachbarn():
    matrix = [[0, 1, 2], 
              [3, 4, 5], 
              [6, 7, 8]]
    n_0 = periodische_nachbarn(Punkt(0, 0), matrix)
    assert n_0.__contains__(1)
    assert n_0.__contains__(2)
    assert n_0.__contains__(3)
    print(n_0)
    n_4 = periodische_nachbarn(Punkt(1, 1), matrix)
    assert n_4.__contains__(1)
    assert n_4.__contains__(3)
    assert n_4.__contains__(5)
    assert n_4.__contains__(7)

def test_nachbar_brennt():
    matrix = [[Feld.BRENNT, Feld.BAUM, Feld.NICHTS],
              [Feld.NICHTS, Feld.NICHTS, Feld.BAUM],
              [Feld.BAUM, Feld.NICHTS, Feld.NICHTS]]
    assert nachbar_brennt(Punkt(0, 1), matrix) == True
    assert nachbar_brennt(Punkt(1, 1), matrix) == False
    assert nachbar_brennt(Punkt(1, 2), matrix) == False
    assert nachbar_brennt(Punkt(2, 0), matrix) == False

def test_beginnt_zu_brennen():
    matrix = [[Feld.BAUM, Feld.BAUM, Feld.NICHTS],
              [Feld.BRENNT, Feld.NICHTS, Feld.BAUM],
              [Feld.NICHTS, Feld.NICHTS, Feld.NICHTS]]
    assert beginnt_zu_brennen(Punkt(0, 0), matrix) == True
    assert beginnt_zu_brennen(Punkt(0, 1), matrix) == False
    assert beginnt_zu_brennen(Punkt(1, 1), matrix) == False
    assert beginnt_zu_brennen(Punkt(1, 2), matrix) == True

def test_perkuliere_schritt():
    matrix = [[Feld.BAUM, Feld.BAUM, Feld.NICHTS],
              [Feld.BRENNT, Feld.NICHTS, Feld.BAUM],
              [Feld.NICHTS, Feld.NICHTS, Feld.NICHTS]]
    neue_matrix = perkuliere_schritt(matrix)
    assert neue_matrix[0][0] == Feld.BRENNT
    assert neue_matrix[0][1] == Feld.BAUM
    assert neue_matrix[1][0] == Feld.ASCHE
    assert neue_matrix[1][1] == Feld.NICHTS
    assert neue_matrix[1][2] == Feld.BRENNT
    assert neue_matrix[2][0] == Feld.NICHTS