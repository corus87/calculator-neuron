# -*- coding: iso-8859-1 -*-
from __future__ import division

import logging
from kalliope.core.NeuronModule import NeuronModule, InvalidParameterException, MissingParameterException


logging.basicConfig()
logger = logging.getLogger("kalliope")

class Calculator(NeuronModule):
    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        # the args from the neuron configuration
        self.variable_1 = kwargs.get('variable_1', None)
        self.variable_2 = kwargs.get('variable_2', None)
        self.operator = kwargs.get('operator', None)
        
        # check if parameters have been provided
        if self._is_parameters_ok():
            def calculate(x,y):
                x = int(x)
                y = int(y)
                if "add" == self.operator:
                    solution = x + y
                elif "subtract" == self.operator:
                    solution = x - y     
                elif "multiply" == self.operator:   
                    solution = x * y
                elif "divide" == self.operator:
                    solution = x / y

                solution = (("%.1f" % solution)).rstrip('0').rstrip('.')
                return solution

            message = {"solution": calculate(self.variable_1,self.variable_2)}        
            self.say(message)
            
    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise
        .. raises:: InvalidParameterException, MissingParameterException
        """
        def check_for_integer(parameter): 
            try:
                parameter = int(parameter)
            except ValueError:   
                raise InvalidParameterException("[Calculator] %s is not a valid integer" % parameter)
        
        if self.variable_1:
            check_for_integer(self.variable_1)
        else:
            raise MissingParameterException("[Calculator] Variable_1 is missing")
        
        if self.variable_2:
            check_for_integer(self.variable_2)
        else:
            raise MissingParameterException("[Calculator] Variable_2 is missing")
        
        if self.operator:
            operators = ["add", "subtract", "multiply", "divide"]
            if self.operator not in operators:
                raise MissingParameterException("[Calculator] %s is not a valid operator" % self.operator)
        else:
            raise MissingParameterException("[Calculator] You have to set a valid operator")
        

        return True