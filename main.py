
def main() -> None:
    print('Rombusz kerület és terület és számolás!')
    A: float = float(input('a: '))
    M: float = float(input('m: '))
    Terület: float = 0
    Kerület: float = 0
    if A <= 0 or M <= 0:
        print("Nullával és annál kisebb számmal nem lehet számolni")
    else:
        Terület = A * M
        Kerület = 4 * A
        print(f'A rombusz területe: {Terület} és a kerülete {Kerület}')


if __name__ == "__main__":
    main()
