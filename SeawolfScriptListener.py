# Generated from SeawolfScript.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SeawolfScriptParser import SeawolfScriptParser
else:
    from SeawolfScriptParser import SeawolfScriptParser

# This class defines a complete listener for a parse tree produced by SeawolfScriptParser.
class SeawolfScriptListener(ParseTreeListener):

    # Enter a parse tree produced by SeawolfScriptParser#prog.
    def enterProg(self, ctx:SeawolfScriptParser.ProgContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#prog.
    def exitProg(self, ctx:SeawolfScriptParser.ProgContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#printExpr.
    def enterPrintExpr(self, ctx:SeawolfScriptParser.PrintExprContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#printExpr.
    def exitPrintExpr(self, ctx:SeawolfScriptParser.PrintExprContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#assign.
    def enterAssign(self, ctx:SeawolfScriptParser.AssignContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#assign.
    def exitAssign(self, ctx:SeawolfScriptParser.AssignContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#assignIndex.
    def enterAssignIndex(self, ctx:SeawolfScriptParser.AssignIndexContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#assignIndex.
    def exitAssignIndex(self, ctx:SeawolfScriptParser.AssignIndexContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#assignMatrix.
    def enterAssignMatrix(self, ctx:SeawolfScriptParser.AssignMatrixContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#assignMatrix.
    def exitAssignMatrix(self, ctx:SeawolfScriptParser.AssignMatrixContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#If.
    def enterIf(self, ctx:SeawolfScriptParser.IfContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#If.
    def exitIf(self, ctx:SeawolfScriptParser.IfContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#While.
    def enterWhile(self, ctx:SeawolfScriptParser.WhileContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#While.
    def exitWhile(self, ctx:SeawolfScriptParser.WhileContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#blank.
    def enterBlank(self, ctx:SeawolfScriptParser.BlankContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#blank.
    def exitBlank(self, ctx:SeawolfScriptParser.BlankContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#stat_block.
    def enterStat_block(self, ctx:SeawolfScriptParser.Stat_blockContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#stat_block.
    def exitStat_block(self, ctx:SeawolfScriptParser.Stat_blockContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#Floor.
    def enterFloor(self, ctx:SeawolfScriptParser.FloorContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#Floor.
    def exitFloor(self, ctx:SeawolfScriptParser.FloorContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#parens.
    def enterParens(self, ctx:SeawolfScriptParser.ParensContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#parens.
    def exitParens(self, ctx:SeawolfScriptParser.ParensContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#Cond.
    def enterCond(self, ctx:SeawolfScriptParser.CondContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#Cond.
    def exitCond(self, ctx:SeawolfScriptParser.CondContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#Mod.
    def enterMod(self, ctx:SeawolfScriptParser.ModContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#Mod.
    def exitMod(self, ctx:SeawolfScriptParser.ModContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#Or.
    def enterOr(self, ctx:SeawolfScriptParser.OrContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#Or.
    def exitOr(self, ctx:SeawolfScriptParser.OrContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#Exponent.
    def enterExponent(self, ctx:SeawolfScriptParser.ExponentContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#Exponent.
    def exitExponent(self, ctx:SeawolfScriptParser.ExponentContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#MulDiv.
    def enterMulDiv(self, ctx:SeawolfScriptParser.MulDivContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#MulDiv.
    def exitMulDiv(self, ctx:SeawolfScriptParser.MulDivContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#AddSub.
    def enterAddSub(self, ctx:SeawolfScriptParser.AddSubContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#AddSub.
    def exitAddSub(self, ctx:SeawolfScriptParser.AddSubContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#In.
    def enterIn(self, ctx:SeawolfScriptParser.InContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#In.
    def exitIn(self, ctx:SeawolfScriptParser.InContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#Index.
    def enterIndex(self, ctx:SeawolfScriptParser.IndexContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#Index.
    def exitIndex(self, ctx:SeawolfScriptParser.IndexContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#String.
    def enterString(self, ctx:SeawolfScriptParser.StringContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#String.
    def exitString(self, ctx:SeawolfScriptParser.StringContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#int.
    def enterInt(self, ctx:SeawolfScriptParser.IntContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#int.
    def exitInt(self, ctx:SeawolfScriptParser.IntContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#Array.
    def enterArray(self, ctx:SeawolfScriptParser.ArrayContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#Array.
    def exitArray(self, ctx:SeawolfScriptParser.ArrayContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#Not.
    def enterNot(self, ctx:SeawolfScriptParser.NotContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#Not.
    def exitNot(self, ctx:SeawolfScriptParser.NotContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#Negative.
    def enterNegative(self, ctx:SeawolfScriptParser.NegativeContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#Negative.
    def exitNegative(self, ctx:SeawolfScriptParser.NegativeContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#And.
    def enterAnd(self, ctx:SeawolfScriptParser.AndContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#And.
    def exitAnd(self, ctx:SeawolfScriptParser.AndContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#Real.
    def enterReal(self, ctx:SeawolfScriptParser.RealContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#Real.
    def exitReal(self, ctx:SeawolfScriptParser.RealContext):
        pass


    # Enter a parse tree produced by SeawolfScriptParser#id.
    def enterId(self, ctx:SeawolfScriptParser.IdContext):
        pass

    # Exit a parse tree produced by SeawolfScriptParser#id.
    def exitId(self, ctx:SeawolfScriptParser.IdContext):
        pass


