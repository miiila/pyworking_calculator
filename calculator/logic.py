from PyQt5 import QtWidgets, uic
import pkg_resources

def main():
	app = QtWidgets.QApplication([])
	window = QtWidgets.QDialog()

	with pkg_resources.resource_stream('calculator','calculator.ui') as f:
		uic.loadUi(f, window)

	sb_operand1 = window.findChild(QtWidgets.QDoubleSpinBox, 'sb_operand1')
	sb_operand2 = window.findChild(QtWidgets.QDoubleSpinBox, 'sb_operand2')
	cb_operator = window.findChild(QtWidgets.QComboBox, 'cb_operator')
	sb_result = window.findChild(QtWidgets.QDoubleSpinBox, 'sb_result')

	def calculate():
		operand1 = sb_operand1.value()
		operand2 = sb_operand2.value()
		operator = cb_operator.currentText()

		try:
			if operator == '+':
				result = operand1 + operand2
			elif operator == '-':
				result = operand1 - operand2
			elif operator == '*':
				result = operand1 * operand2
			elif operator == '/':
				result = operand1 / operand2
			elif operator == '%':
				result = operand1 % operand2
			elif operator == '^':
				result = operand1 ** operand2
			elif operator == '√':
				result = operand1 ** (1/operand2)
			else:
				raise ValueError('bad operator')
		except Exception as e:
			sb_result.setPrefix('ERR ')
			sb_result.setValue(0)
		else:
			sb_result.setPrefix('')
			sb_result.setValue(result)

	sb_operand1.valueChanged.connect(calculate)
	sb_operand2.valueChanged.connect(calculate)
	cb_operator.currentTextChanged.connect(calculate)

	window.show()
	return app.exec()
