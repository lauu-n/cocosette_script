# Generated from Cocosette.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CocosetteParser import CocosetteParser
else:
    from CocosetteParser import CocosetteParser

# This class defines a complete generic visitor for a parse tree produced by CocosetteParser.

class CocosetteVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CocosetteParser#programa.
    def visitPrograma(self, ctx:CocosetteParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#sentencia.
    def visitSentencia(self, ctx:CocosetteParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#asignacion.
    def visitAsignacion(self, ctx:CocosetteParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#fuenteCarga.
    def visitFuenteCarga(self, ctx:CocosetteParser.FuenteCargaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#fuentePipeline.
    def visitFuentePipeline(self, ctx:CocosetteParser.FuentePipelineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#fuenteExpresion.
    def visitFuenteExpresion(self, ctx:CocosetteParser.FuenteExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cargaCSV.
    def visitCargaCSV(self, ctx:CocosetteParser.CargaCSVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoGuardarCSV.
    def visitCocoGuardarCSV(self, ctx:CocosetteParser.CocoGuardarCSVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoImprimir.
    def visitCocoImprimir(self, ctx:CocosetteParser.CocoImprimirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoMientras.
    def visitCocoMientras(self, ctx:CocosetteParser.CocoMientrasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoDefFuncion.
    def visitCocoDefFuncion(self, ctx:CocosetteParser.CocoDefFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#listaParams.
    def visitListaParams(self, ctx:CocosetteParser.ListaParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoRetornar.
    def visitCocoRetornar(self, ctx:CocosetteParser.CocoRetornarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#llamadaFuncion.
    def visitLlamadaFuncion(self, ctx:CocosetteParser.LlamadaFuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#listaArgumentos.
    def visitListaArgumentos(self, ctx:CocosetteParser.ListaArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoLlamadaML.
    def visitCocoLlamadaML(self, ctx:CocosetteParser.CocoLlamadaMLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoRegresionLineal.
    def visitCocoRegresionLineal(self, ctx:CocosetteParser.CocoRegresionLinealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoRegresionPoli.
    def visitCocoRegresionPoli(self, ctx:CocosetteParser.CocoRegresionPoliContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoPerceptron.
    def visitCocoPerceptron(self, ctx:CocosetteParser.CocoPerceptronContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoCalcular.
    def visitCocoCalcular(self, ctx:CocosetteParser.CocoCalcularContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#operacion.
    def visitOperacion(self, ctx:CocosetteParser.OperacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoCrear.
    def visitCocoCrear(self, ctx:CocosetteParser.CocoCrearContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoOrdenar.
    def visitCocoOrdenar(self, ctx:CocosetteParser.CocoOrdenarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoRenombrar.
    def visitCocoRenombrar(self, ctx:CocosetteParser.CocoRenombrarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoEliminarDuplicados.
    def visitCocoEliminarDuplicados(self, ctx:CocosetteParser.CocoEliminarDuplicadosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoTratarNulos.
    def visitCocoTratarNulos(self, ctx:CocosetteParser.CocoTratarNulosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoConvertir.
    def visitCocoConvertir(self, ctx:CocosetteParser.CocoConvertirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#tipoDato.
    def visitTipoDato(self, ctx:CocosetteParser.TipoDatoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoAgrupar.
    def visitCocoAgrupar(self, ctx:CocosetteParser.CocoAgruparContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoResumir.
    def visitCocoResumir(self, ctx:CocosetteParser.CocoResumirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#asignacionAgregada.
    def visitAsignacionAgregada(self, ctx:CocosetteParser.AsignacionAgregadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#funcionAgregacion.
    def visitFuncionAgregacion(self, ctx:CocosetteParser.FuncionAgregacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoSeleccion.
    def visitCocoSeleccion(self, ctx:CocosetteParser.CocoSeleccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoFiltro.
    def visitCocoFiltro(self, ctx:CocosetteParser.CocoFiltroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#listaCocolumnas.
    def visitListaCocolumnas(self, ctx:CocosetteParser.ListaCocolumnasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocondicion.
    def visitCocondicion(self, ctx:CocosetteParser.CocondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoGraficar.
    def visitCocoGraficar(self, ctx:CocosetteParser.CocoGraficarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#cocoGrafica.
    def visitCocoGrafica(self, ctx:CocosetteParser.CocoGraficaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#ejeX.
    def visitEjeX(self, ctx:CocosetteParser.EjeXContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#ejeY.
    def visitEjeY(self, ctx:CocosetteParser.EjeYContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#expAditiva.
    def visitExpAditiva(self, ctx:CocosetteParser.ExpAditivaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#expIgualdad.
    def visitExpIgualdad(self, ctx:CocosetteParser.ExpIgualdadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#expPotencia.
    def visitExpPotencia(self, ctx:CocosetteParser.ExpPotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#expRelacional.
    def visitExpRelacional(self, ctx:CocosetteParser.ExpRelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#expOr.
    def visitExpOr(self, ctx:CocosetteParser.ExpOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#expMultiplicativa.
    def visitExpMultiplicativa(self, ctx:CocosetteParser.ExpMultiplicativaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#expLlamadaML.
    def visitExpLlamadaML(self, ctx:CocosetteParser.ExpLlamadaMLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#expIdentificador.
    def visitExpIdentificador(self, ctx:CocosetteParser.ExpIdentificadorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#expUnaria.
    def visitExpUnaria(self, ctx:CocosetteParser.ExpUnariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#expAnd.
    def visitExpAnd(self, ctx:CocosetteParser.ExpAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#expLlamada.
    def visitExpLlamada(self, ctx:CocosetteParser.ExpLlamadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#expParentesis.
    def visitExpParentesis(self, ctx:CocosetteParser.ExpParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#expLiteral.
    def visitExpLiteral(self, ctx:CocosetteParser.ExpLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CocosetteParser#literal.
    def visitLiteral(self, ctx:CocosetteParser.LiteralContext):
        return self.visitChildren(ctx)



del CocosetteParser