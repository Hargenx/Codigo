#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations
from decimal import Decimal, ROUND_HALF_UP, getcontext
from dataclasses import dataclass

getcontext().prec = 28  # boa precisão para dinheiro

# ---------- Utilidades ----------
def BR(v: Decimal) -> str:
    """Formata Decimal como moeda brasileira (R$ 1.234.567,89)."""
    q = v.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    s = f"{q:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {s}"

@dataclass
class ITBIInput:
    valor_venal_referencia: Decimal   # base arbitrada pela prefeitura
    valor_transacao: Decimal          # preço real de compra
    aliquota: Decimal                 # ex.: 0.03 para 3%

@dataclass
class ITBIResultado:
    itbi_pago: Decimal
    itbi_correto: Decimal
    diferenca_devida: Decimal
    diferenca_atualizada: Decimal | None

def calcular_itbi_restituicao(inp: ITBIInput,
                              fator_atualizacao: Decimal | None = None,
                              taxa_mensal: Decimal | None = None,
                              meses: int | None = None) -> ITBIResultado:
    """
    Calcula o ITBI devido e o valor a restituir.
    - fator_atualizacao: multiplicador já conhecido (ex.: 1.0842).
    - taxa_mensal + meses: alternativa para atualizar pela mesma taxa a.m. por N meses (ex.: 0.004 para 0,4%/mês).
    Priorize fator_atualizacao se ambos forem fornecidos.
    """
    a = inp.aliquota
    itbi_pago = (inp.valor_venal_referencia * a)
    itbi_correto = (inp.valor_transacao * a)

    diferenca = itbi_pago - itbi_correto
    if diferenca <= Decimal("0"):
        # não há restituição (ou há diferença a maior a recolher, cenário incomum)
        return ITBIResultado(
            itbi_pago=itbi_pago,
            itbi_correto=itbi_correto,
            diferenca_devida=Decimal("0.00"),
            diferenca_atualizada=None,
        )

    atualizada = None
    if fator_atualizacao is not None:
        atualizada = (diferenca * fator_atualizacao)
    elif taxa_mensal is not None and meses is not None and meses > 0:
        # capitalização simples composta mensal
        atualizada = diferenca * ((Decimal("1") + taxa_mensal) ** Decimal(meses))

    return ITBIResultado(
        itbi_pago=itbi_pago,
        itbi_correto=itbi_correto,
        diferenca_devida=diferenca,
        diferenca_atualizada=atualizada.quantize(Decimal("0.01"), ROUND_HALF_UP) if atualizada else None,
    )

# ---------- Exemplo do enunciado ----------
if __name__ == "__main__":
    # Exemplo prático:
    exemplo = ITBIInput(
        valor_venal_referencia=Decimal("600000.00"),
        valor_transacao=Decimal("320000.00"),
        aliquota=Decimal("0.03"),  # 3%
    )

    # Sem atualização:
    r = calcular_itbi_restituicao(exemplo)
    print("=== Cálculo do ITBI a restituir ===")
    print("Base prefeitura      :", BR(exemplo.valor_venal_referencia))
    print("Valor da transação   :", BR(exemplo.valor_transacao))
    print("Alíquota             :", f"{(exemplo.aliquota * 100):.2f}%")
    print("ITBI pago            :", BR(r.itbi_pago))      # 600.000 x 3% = 18.000
    print("ITBI correto         :", BR(r.itbi_correto))   # 320.000 x 3% = 9.600
    print("A restituir (líquido):", BR(r.diferenca_devida))  # 8.400

    # Opcional: atualização monetária (ex.: fator acumulado 1,10 -> 10% de correção)
    r_at = calcular_itbi_restituicao(exemplo, fator_atualizacao=Decimal("1.10"))
    if r_at.diferenca_atualizada:
        print("Atualizado (fator 1,10):", BR(r_at.diferenca_atualizada))

    # Opcional: usando taxa mensal e meses (ex.: 0,4%/mês por 18 meses)
    r_tx = calcular_itbi_restituicao(
        exemplo,
        taxa_mensal=Decimal("0.004"),  # 0,4%/mês
        meses=18
    )
    if r_tx.diferenca_atualizada:
        print("Atualizado (0,4% a.m. por 18 meses):", BR(r_tx.diferenca_atualizada))
