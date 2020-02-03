from moebtr import *
from circletree import *

def main():
    A = HComplex(complex(-5.9, -1.39))
    B = HComplex(complex(-1.3, 2.89))
    C = HComplex(complex(5.76, -0.93))
    D = HComplex(complex(-2.69986, -8.657969))
    α = HComplex(complex(-7.4734297, 4.675903))
    β = HComplex(complex(8.492723, 6.5929834))
    γ = HComplex(complex(-12.5395907, -6.8426021))
    δ = HComplex(complex(26.58786, -12.1157866))

    C1 = Circle(B, α, A)
    C2 = Circle(β, B, C)
    C3 = Circle(D, A, γ)
    C4 = Circle(δ, C, D)

    M1 = MoebTr.fromTo(B, α, A, B, β, C)
    M1_inv = M1.inv()
    M2 = MoebTr.fromTo(D, A, γ, D, C, δ)
    M2_inv = M2.inv()

    tree = [TreeNode(C1, M1_inv, M1, M2, M2_inv, 7),
            TreeNode(C2, M1, M1_inv, M2, M2_inv, 7),
            TreeNode(C3, M2_inv, M2, M1, M1_inv, 7),
            TreeNode(C4, M2, M2_inv, M1, M1_inv, 7)]

    plot_tree(tree)
    return

if __name__ == "__main__":
    main()
