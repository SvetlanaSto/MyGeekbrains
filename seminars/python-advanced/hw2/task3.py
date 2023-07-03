from fractions import Fraction

def fraction_addition(fraction1, fraction2):
    fraction1_split = fraction1.split('/')
    numerator1 = int(fraction1_split[0])
    denominator1 = int(fraction1_split[1])
    fraction2_split = fraction2.split('/')
    numerator2 = int(fraction2_split[0])
    denominator2 = int(fraction2_split[1])

    common_denominator = denominator1 * denominator2

    new_numerator1 = numerator1 * denominator2
    new_numerator2 = numerator2 * denominator1

    sum_numerator = new_numerator1 + new_numerator2

    return f"{sum_numerator}/{common_denominator}"


def fraction_multiplication(fraction1, fraction2):
    fraction1_split = fraction1.split('/')
    numerator1 = int(fraction1_split[0])
    denominator1 = int(fraction1_split[1])
    fraction2_split = fraction2.split('/')
    numerator2 = int(fraction2_split[0])
    denominator2 = int(fraction2_split[1])

    product_numerator = numerator1 * numerator2
    product_denominator = denominator1 * denominator2

    return f"{product_numerator}/{product_denominator}"

fract1 = input("Введите первую дробь (вида a/b): ")
fract2 = input("Введите вторую дробь (вида a/b): ")

sum_fraction = fraction_addition(fract1, fract2)
print("Сумма дробей:", sum_fraction)

product_fraction = fraction_multiplication(fract1, fract2)
print("Произведение дробей:", product_fraction)

expected_sum = Fraction(fract1) + Fraction(fract2)
print('ожидаемая сумма через Fractions: {}'.format(expected_sum))

expected_mult = Fraction(fract1) * Fraction(fract2)
print('ожидаемое произведение через Fractions: {}'.format(expected_mult))
