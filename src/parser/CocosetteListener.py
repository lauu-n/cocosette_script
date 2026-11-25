# Generated from Cocosette.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CocosetteParser import CocosetteParser
else:
    from CocosetteParser import CocosetteParser

# This class defines a complete listener for a parse tree produced by CocosetteParser.
class CocosetteListener(ParseTreeListener):

    # Enter a parse tree produced by CocosetteParser#programa.
    def enterPrograma(self, ctx:CocosetteParser.ProgramaContext):
        pass

    # Exit a parse tree produced by CocosetteParser#programa.
    def exitPrograma(self, ctx:CocosetteParser.ProgramaContext):
        pass


    # Enter a parse tree produced by CocosetteParser#sentencia.
    def enterSentencia(self, ctx:CocosetteParser.SentenciaContext):
        pass

    # Exit a parse tree produced by CocosetteParser#sentencia.
    def exitSentencia(self, ctx:CocosetteParser.SentenciaContext):
        pass


    # Enter a parse tree produced by CocosetteParser#asignacion.
    def enterAsignacion(self, ctx:CocosetteParser.AsignacionContext):
        pass

    # Exit a parse tree produced by CocosetteParser#asignacion.
    def exitAsignacion(self, ctx:CocosetteParser.AsignacionContext):
        pass


    # Enter a parse tree produced by CocosetteParser#fuenteCarga.
    def enterFuenteCarga(self, ctx:CocosetteParser.FuenteCargaContext):
        pass

    # Exit a parse tree produced by CocosetteParser#fuenteCarga.
    def exitFuenteCarga(self, ctx:CocosetteParser.FuenteCargaContext):
        pass


    # Enter a parse tree produced by CocosetteParser#fuentePipeline.
    def enterFuentePipeline(self, ctx:CocosetteParser.FuentePipelineContext):
        pass

    # Exit a parse tree produced by CocosetteParser#fuentePipeline.
    def exitFuentePipeline(self, ctx:CocosetteParser.FuentePipelineContext):
        pass


    # Enter a parse tree produced by CocosetteParser#fuenteExpresion.
    def enterFuenteExpresion(self, ctx:CocosetteParser.FuenteExpresionContext):
        pass

    # Exit a parse tree produced by CocosetteParser#fuenteExpresion.
    def exitFuenteExpresion(self, ctx:CocosetteParser.FuenteExpresionContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cargaCSV.
    def enterCargaCSV(self, ctx:CocosetteParser.CargaCSVContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cargaCSV.
    def exitCargaCSV(self, ctx:CocosetteParser.CargaCSVContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoGuardarCSV.
    def enterCocoGuardarCSV(self, ctx:CocosetteParser.CocoGuardarCSVContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoGuardarCSV.
    def exitCocoGuardarCSV(self, ctx:CocosetteParser.CocoGuardarCSVContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoImprimir.
    def enterCocoImprimir(self, ctx:CocosetteParser.CocoImprimirContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoImprimir.
    def exitCocoImprimir(self, ctx:CocosetteParser.CocoImprimirContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoMientras.
    def enterCocoMientras(self, ctx:CocosetteParser.CocoMientrasContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoMientras.
    def exitCocoMientras(self, ctx:CocosetteParser.CocoMientrasContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoDefFuncion.
    def enterCocoDefFuncion(self, ctx:CocosetteParser.CocoDefFuncionContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoDefFuncion.
    def exitCocoDefFuncion(self, ctx:CocosetteParser.CocoDefFuncionContext):
        pass


    # Enter a parse tree produced by CocosetteParser#listaParams.
    def enterListaParams(self, ctx:CocosetteParser.ListaParamsContext):
        pass

    # Exit a parse tree produced by CocosetteParser#listaParams.
    def exitListaParams(self, ctx:CocosetteParser.ListaParamsContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoRetornar.
    def enterCocoRetornar(self, ctx:CocosetteParser.CocoRetornarContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoRetornar.
    def exitCocoRetornar(self, ctx:CocosetteParser.CocoRetornarContext):
        pass


    # Enter a parse tree produced by CocosetteParser#llamadaFuncion.
    def enterLlamadaFuncion(self, ctx:CocosetteParser.LlamadaFuncionContext):
        pass

    # Exit a parse tree produced by CocosetteParser#llamadaFuncion.
    def exitLlamadaFuncion(self, ctx:CocosetteParser.LlamadaFuncionContext):
        pass


    # Enter a parse tree produced by CocosetteParser#listaArgumentos.
    def enterListaArgumentos(self, ctx:CocosetteParser.ListaArgumentosContext):
        pass

    # Exit a parse tree produced by CocosetteParser#listaArgumentos.
    def exitListaArgumentos(self, ctx:CocosetteParser.ListaArgumentosContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoLlamadaML.
    def enterCocoLlamadaML(self, ctx:CocosetteParser.CocoLlamadaMLContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoLlamadaML.
    def exitCocoLlamadaML(self, ctx:CocosetteParser.CocoLlamadaMLContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoRegresionLineal.
    def enterCocoRegresionLineal(self, ctx:CocosetteParser.CocoRegresionLinealContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoRegresionLineal.
    def exitCocoRegresionLineal(self, ctx:CocosetteParser.CocoRegresionLinealContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoRegresionPoli.
    def enterCocoRegresionPoli(self, ctx:CocosetteParser.CocoRegresionPoliContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoRegresionPoli.
    def exitCocoRegresionPoli(self, ctx:CocosetteParser.CocoRegresionPoliContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoPerceptron.
    def enterCocoPerceptron(self, ctx:CocosetteParser.CocoPerceptronContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoPerceptron.
    def exitCocoPerceptron(self, ctx:CocosetteParser.CocoPerceptronContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoCalcular.
    def enterCocoCalcular(self, ctx:CocosetteParser.CocoCalcularContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoCalcular.
    def exitCocoCalcular(self, ctx:CocosetteParser.CocoCalcularContext):
        pass


    # Enter a parse tree produced by CocosetteParser#operacion.
    def enterOperacion(self, ctx:CocosetteParser.OperacionContext):
        pass

    # Exit a parse tree produced by CocosetteParser#operacion.
    def exitOperacion(self, ctx:CocosetteParser.OperacionContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoCrear.
    def enterCocoCrear(self, ctx:CocosetteParser.CocoCrearContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoCrear.
    def exitCocoCrear(self, ctx:CocosetteParser.CocoCrearContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoOrdenar.
    def enterCocoOrdenar(self, ctx:CocosetteParser.CocoOrdenarContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoOrdenar.
    def exitCocoOrdenar(self, ctx:CocosetteParser.CocoOrdenarContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoRenombrar.
    def enterCocoRenombrar(self, ctx:CocosetteParser.CocoRenombrarContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoRenombrar.
    def exitCocoRenombrar(self, ctx:CocosetteParser.CocoRenombrarContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoEliminarDuplicados.
    def enterCocoEliminarDuplicados(self, ctx:CocosetteParser.CocoEliminarDuplicadosContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoEliminarDuplicados.
    def exitCocoEliminarDuplicados(self, ctx:CocosetteParser.CocoEliminarDuplicadosContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoTratarNulos.
    def enterCocoTratarNulos(self, ctx:CocosetteParser.CocoTratarNulosContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoTratarNulos.
    def exitCocoTratarNulos(self, ctx:CocosetteParser.CocoTratarNulosContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoConvertir.
    def enterCocoConvertir(self, ctx:CocosetteParser.CocoConvertirContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoConvertir.
    def exitCocoConvertir(self, ctx:CocosetteParser.CocoConvertirContext):
        pass


    # Enter a parse tree produced by CocosetteParser#tipoDato.
    def enterTipoDato(self, ctx:CocosetteParser.TipoDatoContext):
        pass

    # Exit a parse tree produced by CocosetteParser#tipoDato.
    def exitTipoDato(self, ctx:CocosetteParser.TipoDatoContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoAgrupar.
    def enterCocoAgrupar(self, ctx:CocosetteParser.CocoAgruparContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoAgrupar.
    def exitCocoAgrupar(self, ctx:CocosetteParser.CocoAgruparContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoResumir.
    def enterCocoResumir(self, ctx:CocosetteParser.CocoResumirContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoResumir.
    def exitCocoResumir(self, ctx:CocosetteParser.CocoResumirContext):
        pass


    # Enter a parse tree produced by CocosetteParser#asignacionAgregada.
    def enterAsignacionAgregada(self, ctx:CocosetteParser.AsignacionAgregadaContext):
        pass

    # Exit a parse tree produced by CocosetteParser#asignacionAgregada.
    def exitAsignacionAgregada(self, ctx:CocosetteParser.AsignacionAgregadaContext):
        pass


    # Enter a parse tree produced by CocosetteParser#funcionAgregacion.
    def enterFuncionAgregacion(self, ctx:CocosetteParser.FuncionAgregacionContext):
        pass

    # Exit a parse tree produced by CocosetteParser#funcionAgregacion.
    def exitFuncionAgregacion(self, ctx:CocosetteParser.FuncionAgregacionContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoSeleccion.
    def enterCocoSeleccion(self, ctx:CocosetteParser.CocoSeleccionContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoSeleccion.
    def exitCocoSeleccion(self, ctx:CocosetteParser.CocoSeleccionContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoFiltro.
    def enterCocoFiltro(self, ctx:CocosetteParser.CocoFiltroContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoFiltro.
    def exitCocoFiltro(self, ctx:CocosetteParser.CocoFiltroContext):
        pass


    # Enter a parse tree produced by CocosetteParser#listaCocolumnas.
    def enterListaCocolumnas(self, ctx:CocosetteParser.ListaCocolumnasContext):
        pass

    # Exit a parse tree produced by CocosetteParser#listaCocolumnas.
    def exitListaCocolumnas(self, ctx:CocosetteParser.ListaCocolumnasContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocondicion.
    def enterCocondicion(self, ctx:CocosetteParser.CocondicionContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocondicion.
    def exitCocondicion(self, ctx:CocosetteParser.CocondicionContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoGraficar.
    def enterCocoGraficar(self, ctx:CocosetteParser.CocoGraficarContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoGraficar.
    def exitCocoGraficar(self, ctx:CocosetteParser.CocoGraficarContext):
        pass


    # Enter a parse tree produced by CocosetteParser#cocoGrafica.
    def enterCocoGrafica(self, ctx:CocosetteParser.CocoGraficaContext):
        pass

    # Exit a parse tree produced by CocosetteParser#cocoGrafica.
    def exitCocoGrafica(self, ctx:CocosetteParser.CocoGraficaContext):
        pass


    # Enter a parse tree produced by CocosetteParser#ejeX.
    def enterEjeX(self, ctx:CocosetteParser.EjeXContext):
        pass

    # Exit a parse tree produced by CocosetteParser#ejeX.
    def exitEjeX(self, ctx:CocosetteParser.EjeXContext):
        pass


    # Enter a parse tree produced by CocosetteParser#ejeY.
    def enterEjeY(self, ctx:CocosetteParser.EjeYContext):
        pass

    # Exit a parse tree produced by CocosetteParser#ejeY.
    def exitEjeY(self, ctx:CocosetteParser.EjeYContext):
        pass


    # Enter a parse tree produced by CocosetteParser#expAditiva.
    def enterExpAditiva(self, ctx:CocosetteParser.ExpAditivaContext):
        pass

    # Exit a parse tree produced by CocosetteParser#expAditiva.
    def exitExpAditiva(self, ctx:CocosetteParser.ExpAditivaContext):
        pass


    # Enter a parse tree produced by CocosetteParser#expIgualdad.
    def enterExpIgualdad(self, ctx:CocosetteParser.ExpIgualdadContext):
        pass

    # Exit a parse tree produced by CocosetteParser#expIgualdad.
    def exitExpIgualdad(self, ctx:CocosetteParser.ExpIgualdadContext):
        pass


    # Enter a parse tree produced by CocosetteParser#expPotencia.
    def enterExpPotencia(self, ctx:CocosetteParser.ExpPotenciaContext):
        pass

    # Exit a parse tree produced by CocosetteParser#expPotencia.
    def exitExpPotencia(self, ctx:CocosetteParser.ExpPotenciaContext):
        pass


    # Enter a parse tree produced by CocosetteParser#expRelacional.
    def enterExpRelacional(self, ctx:CocosetteParser.ExpRelacionalContext):
        pass

    # Exit a parse tree produced by CocosetteParser#expRelacional.
    def exitExpRelacional(self, ctx:CocosetteParser.ExpRelacionalContext):
        pass


    # Enter a parse tree produced by CocosetteParser#expOr.
    def enterExpOr(self, ctx:CocosetteParser.ExpOrContext):
        pass

    # Exit a parse tree produced by CocosetteParser#expOr.
    def exitExpOr(self, ctx:CocosetteParser.ExpOrContext):
        pass


    # Enter a parse tree produced by CocosetteParser#expMultiplicativa.
    def enterExpMultiplicativa(self, ctx:CocosetteParser.ExpMultiplicativaContext):
        pass

    # Exit a parse tree produced by CocosetteParser#expMultiplicativa.
    def exitExpMultiplicativa(self, ctx:CocosetteParser.ExpMultiplicativaContext):
        pass


    # Enter a parse tree produced by CocosetteParser#expLlamadaML.
    def enterExpLlamadaML(self, ctx:CocosetteParser.ExpLlamadaMLContext):
        pass

    # Exit a parse tree produced by CocosetteParser#expLlamadaML.
    def exitExpLlamadaML(self, ctx:CocosetteParser.ExpLlamadaMLContext):
        pass


    # Enter a parse tree produced by CocosetteParser#expIdentificador.
    def enterExpIdentificador(self, ctx:CocosetteParser.ExpIdentificadorContext):
        pass

    # Exit a parse tree produced by CocosetteParser#expIdentificador.
    def exitExpIdentificador(self, ctx:CocosetteParser.ExpIdentificadorContext):
        pass


    # Enter a parse tree produced by CocosetteParser#expUnaria.
    def enterExpUnaria(self, ctx:CocosetteParser.ExpUnariaContext):
        pass

    # Exit a parse tree produced by CocosetteParser#expUnaria.
    def exitExpUnaria(self, ctx:CocosetteParser.ExpUnariaContext):
        pass


    # Enter a parse tree produced by CocosetteParser#expAnd.
    def enterExpAnd(self, ctx:CocosetteParser.ExpAndContext):
        pass

    # Exit a parse tree produced by CocosetteParser#expAnd.
    def exitExpAnd(self, ctx:CocosetteParser.ExpAndContext):
        pass


    # Enter a parse tree produced by CocosetteParser#expLlamada.
    def enterExpLlamada(self, ctx:CocosetteParser.ExpLlamadaContext):
        pass

    # Exit a parse tree produced by CocosetteParser#expLlamada.
    def exitExpLlamada(self, ctx:CocosetteParser.ExpLlamadaContext):
        pass


    # Enter a parse tree produced by CocosetteParser#expParentesis.
    def enterExpParentesis(self, ctx:CocosetteParser.ExpParentesisContext):
        pass

    # Exit a parse tree produced by CocosetteParser#expParentesis.
    def exitExpParentesis(self, ctx:CocosetteParser.ExpParentesisContext):
        pass


    # Enter a parse tree produced by CocosetteParser#expLiteral.
    def enterExpLiteral(self, ctx:CocosetteParser.ExpLiteralContext):
        pass

    # Exit a parse tree produced by CocosetteParser#expLiteral.
    def exitExpLiteral(self, ctx:CocosetteParser.ExpLiteralContext):
        pass


    # Enter a parse tree produced by CocosetteParser#literal.
    def enterLiteral(self, ctx:CocosetteParser.LiteralContext):
        pass

    # Exit a parse tree produced by CocosetteParser#literal.
    def exitLiteral(self, ctx:CocosetteParser.LiteralContext):
        pass



del CocosetteParser