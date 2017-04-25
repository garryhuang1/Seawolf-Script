# Generated from SeawolfScript.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SeawolfScriptParser import SeawolfScriptParser
else:
    from SeawolfScriptParser import SeawolfScriptParser

# This class defines a complete generic visitor for a parse tree produced by SeawolfScriptParser.

class SeawolfScriptVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SeawolfScriptParser#prog.
    def visitProg(self, ctx:SeawolfScriptParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#printExpr.
    def visitPrintExpr(self, ctx:SeawolfScriptParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#assign.
    def visitAssign(self, ctx:SeawolfScriptParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#assignIndex.
    def visitAssignIndex(self, ctx:SeawolfScriptParser.AssignIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#assignMatrix.
    def visitAssignMatrix(self, ctx:SeawolfScriptParser.AssignMatrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#If.
    def visitIf(self, ctx:SeawolfScriptParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#While.
    def visitWhile(self, ctx:SeawolfScriptParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#blank.
    def visitBlank(self, ctx:SeawolfScriptParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#stat_block.
    def visitStat_block(self, ctx:SeawolfScriptParser.Stat_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#Floor.
    def visitFloor(self, ctx:SeawolfScriptParser.FloorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#parens.
    def visitParens(self, ctx:SeawolfScriptParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#Cond.
    def visitCond(self, ctx:SeawolfScriptParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#Mod.
    def visitMod(self, ctx:SeawolfScriptParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#Or.
    def visitOr(self, ctx:SeawolfScriptParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#Exponent.
    def visitExponent(self, ctx:SeawolfScriptParser.ExponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#MulDiv.
    def visitMulDiv(self, ctx:SeawolfScriptParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#AddSub.
    def visitAddSub(self, ctx:SeawolfScriptParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#In.
    def visitIn(self, ctx:SeawolfScriptParser.InContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#Index.
    def visitIndex(self, ctx:SeawolfScriptParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#String.
    def visitString(self, ctx:SeawolfScriptParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#int.
    def visitInt(self, ctx:SeawolfScriptParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#Array.
    def visitArray(self, ctx:SeawolfScriptParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#Not.
    def visitNot(self, ctx:SeawolfScriptParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#Negative.
    def visitNegative(self, ctx:SeawolfScriptParser.NegativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#And.
    def visitAnd(self, ctx:SeawolfScriptParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#Real.
    def visitReal(self, ctx:SeawolfScriptParser.RealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SeawolfScriptParser#id.
    def visitId(self, ctx:SeawolfScriptParser.IdContext):
        return self.visitChildren(ctx)



del SeawolfScriptParser