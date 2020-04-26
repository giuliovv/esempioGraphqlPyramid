#!/usr/bin/env python
# -*- coding: utf-8 -*-

import graphene
from graphene import Schema

import sorgente

class Esempio(graphene.ObjectType):
    esempio = graphene.String()

class Risultato(graphene.ObjectType):
    buongiorno = graphene.String(
        nome=graphene.String(default_value="Mario"),
        )
    ciao = graphene.List(
        Esempio,
        nome=graphene.String(default_value="Mario"),
        )

    def resolve_buongiorno(root, info, nome):
        """
            {
                buongiorno(nome:"Ugo")
            }
        """
        return sorgente.buongiorno(nome)

    def resolve_ciao(root, info, nome):
        """
            {
                ciao(nome:"Ugo"){
                    esempio
                }
            }
        """
        return [Esempio(sorgente.ciao(nome))]