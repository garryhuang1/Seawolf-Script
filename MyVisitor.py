from SeawolfScriptVisitor import SeawolfScriptVisitor
from SeawolfScriptParser import SeawolfScriptParser

class MyVisitor(SeawolfScriptVisitor):
	def __init__(self):
		self.memory={}
	def visitPrintExpr(self, ctx):
		value = self.visit(ctx.expr())
		print(value)
		return 0
	def visitNegative(self, ctx):
		value = self.visit(ctx.expr())
		return -1 * value
	def visitId(self, ctx):
		name = ctx.ID().getText()
		if name in self.memory:
			return self.memory[name]
		return 0
	def visitAssign(self, ctx):
		name = ctx.ID().getText()
		value = self.visit(ctx.expr())
		self.memory[name] = value
		return value
	def visitArray(self, ctx):
		#if self.visit(ctx.expr(2)) is None:
		#	print("YES")
		#newStr = newStr[1:-1]
		#arrayList = newStr.split(' ')
		length = (len(ctx.expr()))
		words = []
		for i in range(0,length):
			words.append(self.visit(ctx.expr(i)))
		return words
	def visitString(self, ctx):
		newStr = str(ctx.STRING().getText())
		newStr = newStr[1:-1]
		return str(newStr)
	def visitReal(self, ctx):
		return float(ctx.REAL().getText())
	def visitInt(self, ctx):
		return int(ctx.INT().getText())
	def visitIn(self, ctx):
		left = self.visit(ctx.expr(0))
		right = self.visit(ctx.expr(1))
		if left in right:
			return 1
		else:
			return 0
	def visitIndex(self, ctx):
		left = self.visit(ctx.expr(0))
		if (type(left) is list or type(left) is str) == False:
			return "SEMANTIC ERROR"
		right = self.visit(ctx.expr(1))
		if (type(right) is int) == False:
			return "SEMANTIC ERROR"
		if (right >= len(left)) == True:
			return "SEMANTIC ERROR"
		indexAt = left[right]
		return indexAt
	def visitExponent(self, ctx):
		left = (self.visit(ctx.expr(0)))
		right = (self.visit(ctx.expr(1)))
		if (type(left) is int or type(left) is float) == False:
			return "SEMANTIC ERROR"
		if (type(right) is int or type(right) is float) == False:
			return "SEMANTIC ERROR"
		return left ** right
	def visitMulDiv(self, ctx):
		left = (self.visit(ctx.expr(0)))
		right = (self.visit(ctx.expr(1)))
		if (type(left) is int or type(left) is float) == False:
			return "SEMANTIC ERROR"
		if (type(right) is int or type(right) is float) == False:
			return "SEMANTIC ERROR"
		if ctx.op.type == SeawolfScriptParser.MUL:
			return left * right
		if(right == 0):
			return "SEMANTIC ERROR"
		return left / right
	def visitAddSub(self, ctx):
		left = (self.visit(ctx.expr(0)))
		right = (self.visit(ctx.expr(1)))
		if(type(left) is int or type(left) is float) and (type(right) is int or type(right) is float) == True and ctx.op.type == SeawolfScriptParser.ADD:
			return left + right
		if(type(left) == type(right)) == False:
			return "SEMANTIC ERROR"
		if (type(left) is str and type(right) is str) and ctx.op.type == SeawolfScriptParser.ADD:
			return str(left + right)
		if (type(left) is list and type (right) is list) and ctx.op.type == SeawolfScriptParser.ADD:
			newList = left + right
			return newList
		if ctx.op.type == SeawolfScriptParser.ADD and (type(left) is int and type(right) is int):
			return left + right
		if (type(left) is int or type(left) is float) == False and ctx.op.type == SeawolfScriptParser.SUB:
			return "SEMANTIC ERROR"
		if (type(right) is int or type(right) is float) == False and ctx.op.type == SeawolfScriptParser.SUB:
			return "SEMANTIC ERROR"
		return left - right
	def visitFloor(self, ctx):
		left = (self.visit(ctx.expr(0)))
		right = (self.visit(ctx.expr(1)))
		if (type(left) is int or type(left) is float) == False:
			return "SEMANTIC ERROR"
		if (type(right) is int or type(right) is float) == False:
			return "SEMANTIC ERROR"
		return left//right
	def visitMod(self, ctx):
		left = (self.visit(ctx.expr(0)))
		right = (self.visit(ctx.expr(1)))
		if (type(left) is int or type(left) is float) == False:
				return "SEMANTIC ERROR"
		if (type(right) is int or type(right) is float) == False:
			return "SEMANTIC ERROR"
		return left % right
	def visitParens(self, ctx):
		return self.visit(ctx.expr())
	def visitAnd(self, ctx):
		left = (self.visit(ctx.expr(0)))
		right = (self.visit(ctx.expr(1)))
		if (type(left) is int and type(right) is int) == False:
			return "SEMANTIC ERROR"
		leftBool = True;
		rightBool = True;
		if left == 0:
			leftBool = False
		if right == 0:
			rightBool = False
		
		if leftBool and rightBool == True:		
			return 1
		else:
			return 0
		return -1
	def visitOr(self, ctx):
		left = (self.visit(ctx.expr(0)))
		right = (self.visit(ctx.expr(1)))
		if (type(left) is int and type(right) is int) == False:
			return "SEMANTIC ERROR"
		leftBool = True;
		rightBool = True;
		if left == 0:
			leftBool = False
		if right == 0:
			rightBool = False
		if leftBool or rightBool == True:
			return 1
		else:
			return 0
	def visitNot(self, ctx):
		num = (self.visit(ctx.expr()))
		if (type(num) is int) == False:
			return "SEMANTIC ERROR"
		if num == 0:
			return 1
		else:
			return 0
		return 0
	def visitCond(self, ctx):
		left = (self.visit(ctx.expr(0)))
		right = (self.visit(ctx.expr(1)))
		if (type(left) is int and type(right) is int) == False:
			return "SEMANTIC ERROR"
		if ctx.op.type == SeawolfScriptParser.LTHAN:
			if(left < right):
				return 1
			else:
				return 0
		if ctx.op.type == SeawolfScriptParser.GTHAN:
			if(left > right):
				return 1
			else:
				return 0
		if ctx.op.type == SeawolfScriptParser.LTHANE:
			if(left<=right):
				return 1
			else:
				return 0
		if ctx.op.type == SeawolfScriptParser.GTHANE:
			if(left>=right):
				return 1
			else:
				return 0
		if ctx.op.type == SeawolfScriptParser.EQUAL:
			if(left==right):
				return 1
			else:
				return 0
		if ctx.op.type == SeawolfScriptParser.NEQUAL:
			if(left!=right):
				return 1
			else:
				return 0
		return 0