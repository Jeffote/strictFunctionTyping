import unittest
from strictFunctionTyping import *


class MyTestCase(unittest.TestCase):
	def argsToKwargsTester(self, function: Callable, args: tuple, kwargs: dict, argsExpected: tuple, kwargsExpected: dict):
		argsResult, kwargsResult = mapArgsToKwargs(function, args, kwargs)
		self.assertEqual(argsResult, argsExpected)
		self.assertEqual(kwargsResult, kwargsExpected)

	def testMapArgsToKwargs1(self):
		def myFunc(arg1):
			print(arg1)

		argsInsert: tuple = (1,)
		argsInsert2: tuple = ()
		argsExpected: tuple = ()

		kwargsInsert: dict = {}
		kwargsInsert2: dict = {'arg1': 1}
		kwargsExpected: dict = {'arg1': 1}

		self.argsToKwargsTester(myFunc, argsInsert, kwargsInsert, argsExpected, kwargsExpected)
		self.argsToKwargsTester(myFunc, argsInsert2, kwargsInsert2, argsExpected, kwargsExpected)

	def testMapArgsToKwargs2(self):
		def myFunc(arg1, arg2):
			print(arg1, arg2)

		argsInsert: tuple = (1, 2)
		argsInsert2: tuple = ()
		argsInsert3: tuple = (1,)

		argsExpected: tuple = ()

		kwargsInsert: dict = {}
		kwargsInsert2: dict = {'arg1': 1, 'arg2': 2}
		kwargsInsert20: dict = {'arg2': 2, 'arg1': 1}
		kwargsInsert3: dict = {'arg2': 2}

		kwargsExpected: dict = {'arg1': 1, 'arg2': 2}

		self.argsToKwargsTester(myFunc, argsInsert, kwargsInsert, argsExpected, kwargsExpected)
		self.argsToKwargsTester(myFunc, argsInsert2, kwargsInsert2, argsExpected, kwargsExpected)
		self.argsToKwargsTester(myFunc, argsInsert2, kwargsInsert20, argsExpected, kwargsExpected)  # myfunc(arg2=2, arg1=1)
		self.argsToKwargsTester(myFunc, argsInsert3, kwargsInsert3, argsExpected, kwargsExpected)  # myFunc(1, arg2=2)

	def testMapArgsToKwargs3(self):
		def myFunc(arg1, arg2, arg3):
			print(arg1, arg2, arg3)

		argsInsert: tuple = (1, 2, 3)
		argsInsert2: tuple = ()
		argsInsert3: tuple = (1,)
		argsInsert4: tuple = (1, 2)

		argsExpected: tuple = ()

		kwargsInsert: dict = {}
		kwargsInsert2: dict = {'arg1': 1, 'arg2': 2, 'arg3': 3}
		kwargsInsert3: dict = {'arg2': 2, 'arg3': 3}
		kwargsInsert4: dict = {'arg3': 3}

		kwargsExpected: dict = {'arg1': 1, 'arg2': 2, 'arg3': 3}

		self.argsToKwargsTester(myFunc, argsInsert, kwargsInsert, argsExpected, kwargsExpected)  # myFunc(1, 2, 3)
		self.argsToKwargsTester(myFunc, argsInsert2, kwargsInsert2, argsExpected, kwargsExpected)  # myFunc(arg1=1, arg2=2, arg3=3)
		self.argsToKwargsTester(myFunc, argsInsert3, kwargsInsert3, argsExpected, kwargsExpected)  # myFunc(1, arg2=2, arg3=3)
		self.argsToKwargsTester(myFunc, argsInsert4, kwargsInsert4, argsExpected, kwargsExpected)  # myFunc(1, 2, arg3=3)

	def testMapArgsToKwargs4(self):
		def myFunc(arg1=1):
			print(arg1)

		argsInsert: tuple = (1,)
		argsInsert2: tuple = ()
		argsExpected: tuple = ()

		kwargsInsert: dict = {}
		kwargsInsert2: dict = {'arg1': 1}
		kwargsExpected: dict = {'arg1': 1}

		self.argsToKwargsTester(myFunc, argsInsert, kwargsInsert, argsExpected, kwargsExpected)  # myFunc(1)
		self.argsToKwargsTester(myFunc, argsInsert2, kwargsInsert2, argsExpected, kwargsExpected)  # myFunc(arg1=1)
		self.argsToKwargsTester(myFunc, argsInsert2, kwargsInsert, argsExpected, kwargsExpected)  # myFunc()

	def testMapArgsToKwargs5(self):
		def myFunc(arg1, arg2=2):
			print(arg1, arg2)

		argsInsert: tuple = (1,)
		argsInsert2: tuple = ()

		argsExpected: tuple = ()

		kwargsInsert: dict = {}
		kwargsInsert2: dict = {'arg2': 2, 'arg1': 1}

		kwargsExpected: dict = {'arg1': 1, 'arg2': 2}

		self.argsToKwargsTester(myFunc, argsInsert, kwargsInsert, argsExpected, kwargsExpected)  # myFunc(1)
		self.argsToKwargsTester(myFunc, argsInsert2, kwargsInsert2, argsExpected, kwargsExpected)  # myFunc(arg2=2, arg1=1)

	def testMapArgsToKwargs6(self):
		def myFunc(arg1=1, arg2=2):
			print(arg1, arg2)

		argsInsert2: tuple = ()

		argsExpected: tuple = ()

		kwargsInsert2: dict = {'arg2': 2}

		kwargsExpected: dict = {'arg1': 1, 'arg2': 2}

		self.argsToKwargsTester(myFunc, argsInsert2, kwargsInsert2, argsExpected, kwargsExpected)  # myFunc(arg2=2)

	def testMapArgsToKwargs7(self):
		def myFunc(arg1, arg2=2, arg3=3):
			print(arg1, arg2, arg3)

		argsInsert1: tuple = (1,)
		argsInsert2: tuple = (1, 2)

		argsExpected: tuple = ()

		kwargsInsert1: dict = {}
		kwargsInsert2: dict = {'arg3': 3, 'arg1': 1}

		kwargsExpected: dict = {'arg1': 1, 'arg2': 2, 'arg3': 3}

		self.argsToKwargsTester(myFunc, argsInsert1, kwargsInsert1, argsExpected, kwargsExpected)  # myFunc(1)
		self.argsToKwargsTester(myFunc, argsInsert2, kwargsInsert1, argsExpected, kwargsExpected)  # myFunc(1, 2)
		self.argsToKwargsTester(myFunc, argsExpected, kwargsInsert2, argsExpected, kwargsExpected)  # myFunc(arg3=3, arg1=1)

	def testEnforceStrictTyping1(self):
		@enforceStrictTyping()
		def myFunc(arg: int) -> bool:
			return True

		self.assertTrue(myFunc(5))

		with self.assertRaises(TypeError):
			myFunc(5.0)
		with self.assertRaises(TypeError):
			myFunc('5')
		with self.assertRaises(TypeError):
			myFunc(True)
		with self.assertRaises(TypeError):
			class MyClass:
				x = None

			myFunc(MyClass())

	def testEnforceStrictTyping2(self):
		class MyClass:
			x = None

		@enforceStrictTyping()
		def myFunc(arg: MyClass) -> bool:
			return True

		self.assertTrue(MyClass())

		with self.assertRaises(TypeError):
			myFunc(5.0)
		with self.assertRaises(TypeError):
			myFunc('5')
		with self.assertRaises(TypeError):
			myFunc(True)

	def testEnforceStrictTyping3(self):
		@enforceStrictTyping(False)
		def myFunc(x):
			return True

		self.assertTrue(myFunc(5))
		self.assertTrue(myFunc('5'))

	def testEnforceStrictTyping4(self):
		@enforceStrictTyping()
		def myFunc(x: int):
			return True

		with self.assertRaises(TypeError):
			myFunc(5)

	def testEnforceStrictTyping5(self):
		@enforceStrictTyping()
		def myFunc(x):
			return True

		with self.assertRaises(TypeError):
			myFunc(5)

	def testEnforceStrictTyping6(self):
		class MyClass:
			y = True

		@enforceStrictTyping()
		def myFunc(x: int) -> MyClass:
			myClass = MyClass()
			return myClass

		self.assertTrue(myFunc(5).y)

	def testEnforceStrictTyping7(self):
		class MyClass:
			y = True

		@enforceStrictTyping()
		def myFunc(x: MyClass) -> MyClass:
			myClass = MyClass()
			return myClass

		self.assertTrue(myFunc(MyClass()).y)

		with self.assertRaises(TypeError):
			myFunc(5)


if __name__ == '__main__':
	unittest.main()
