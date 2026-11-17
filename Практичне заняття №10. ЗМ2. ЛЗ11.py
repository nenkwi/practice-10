class Telement:


    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def rezult(self) -> float:
        raise NotImplementedError("Віртуальний метод rezult має бути реалізований у нащадках")


class Number(Telement):


    def __init__(self, value: float):
        super().__init__(None, None)
        self.value = value

    def rezult(self) -> float:
        return self.value


class Plus(Telement):


    def __init__(self, left: Telement, right: Telement):
        super().__init__(left, right)

    def rezult(self) -> float:
        return self.left.rezult() + self.right.rezult()


class Mult(Telement):


    def __init__(self, left: Telement, right: Telement):
        super().__init__(left, right)

    def rezult(self) -> float:
        return self.left.rezult() * self.right.rezult()


def form(s: str, x_val: float = 0.0) -> Telement:

    s = s.strip()


    p_plus = s.find('+')
    if p_plus > 0:
        s1 = s[:p_plus]
        s2 = s[p_plus + 1:]
        return Plus(form(s1, x_val), form(s2, x_val))


    p_mult = s.find('*')
    if p_mult > 0:
        s1 = s[:p_mult]
        s2 = s[p_mult + 1:]
        return Mult(form(s1, x_val), form(s2, x_val))


    if s == 'x':
        return Number(x_val)


    return Number(float(s))


def main():
    print("=== Інтерпретатор математичних виразів ===")

    try:

        expr_x = input("Введіть вираз для x (наприклад, 2+3 або число): ").strip()


        tree_x = form(expr_x, x_val=0.0)
        x_val = tree_x.rezult()
        print(f"Отримане значення x = {x_val}")


        expr_fx = input("Введіть вираз для f(x) (наприклад, x*x+2*x+3): ").strip()


        tree_fx = form(expr_fx, x_val=x_val)
        fx_val = tree_fx.rezult()


        precision_str = input("Введіть кількість десяткових знаків (за замовчуванням 2): ").strip()
        dec = int(precision_str) if precision_str else 2

        print("\n--- Результуючі значення ---")
        print(f"x = {x_val:.{dec}f}")
        print(f"f(x) = {fx_val:.{dec}f}")

    except Exception as e:

        print(f"\n[ПОМИЛКА] Сталася помилка під час обробки виразу: {e}")
        print(
            "Будь ласка, перевірте правильність введення (допускаються лише числа, операції '+' та '*', і змінна 'x').")


if __name__ == "__main__":
    main()
