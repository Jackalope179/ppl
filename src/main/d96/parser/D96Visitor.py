# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_dcl.
    def visitClass_dcl(self, ctx:D96Parser.Class_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#super_class.
    def visitSuper_class(self, ctx:D96Parser.Super_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_body.
    def visitClass_body(self, ctx:D96Parser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#declare.
    def visitDeclare(self, ctx:D96Parser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attr_dcl.
    def visitAttr_dcl(self, ctx:D96Parser.Attr_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#id_list.
    def visitId_list(self, ctx:D96Parser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr_list.
    def visitExpr_list(self, ctx:D96Parser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_dcl.
    def visitMethod_dcl(self, ctx:D96Parser.Method_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor_dcl.
    def visitConstructor_dcl(self, ctx:D96Parser.Constructor_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor_dcl.
    def visitDestructor_dcl(self, ctx:D96Parser.Destructor_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#params.
    def visitParams(self, ctx:D96Parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#var_dcl.
    def visitVar_dcl(self, ctx:D96Parser.Var_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#const_dcl.
    def visitConst_dcl(self, ctx:D96Parser.Const_dclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#nonstatic_list.
    def visitNonstatic_list(self, ctx:D96Parser.Nonstatic_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#nonstatic.
    def visitNonstatic(self, ctx:D96Parser.NonstaticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ass_stmt.
    def visitAss_stmt(self, ctx:D96Parser.Ass_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lhs.
    def visitLhs(self, ctx:D96Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalar.
    def visitScalar(self, ctx:D96Parser.ScalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idx_expr.
    def visitIdx_expr(self, ctx:D96Parser.Idx_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#if_stmt.
    def visitIf_stmt(self, ctx:D96Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseif_stmt.
    def visitElseif_stmt(self, ctx:D96Parser.Elseif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#else_stmt.
    def visitElse_stmt(self, ctx:D96Parser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#loop_stmt.
    def visitLoop_stmt(self, ctx:D96Parser.Loop_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#by_stmt.
    def visitBy_stmt(self, ctx:D96Parser.By_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#loop_body.
    def visitLoop_body(self, ctx:D96Parser.Loop_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D96Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#cont_stmt.
    def visitCont_stmt(self, ctx:D96Parser.Cont_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#return_stmt.
    def visitReturn_stmt(self, ctx:D96Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#method_invo_stmt.
    def visitMethod_invo_stmt(self, ctx:D96Parser.Method_invo_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        return self.visitChildren(ctx)



del D96Parser