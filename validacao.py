def validar_cpf(cpf: str) -> bool:
    # Remove todos os caracteres que não são dígitos
    cpf = ''.join(c for c in cpf if c.isdigit())
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calc_digito(cpf, peso):
        soma = sum(int(digito) * (peso - idx) for idx, digito in enumerate(cpf[:peso-1]))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    digito1 = calc_digito(cpf, 10)
    digito2 = calc_digito(cpf, 11)
    return cpf[-2:] == digito1 + digito2