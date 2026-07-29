"""Basic proof of life check for numpoly."""


def test_numpoly():
    import numpoly
    x = numpoly.variable(1)
    p = x**2 + 3*x + 1

    assert numpoly.diff(p, x) == 2*x + 3
