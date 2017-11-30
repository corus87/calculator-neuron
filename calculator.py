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
        self.add = kwargs.get('add', False)       
        self.subtract = kwargs.get('subtract', False)
        self.multiply = kwargs.get('multiply', False)
        self.divide = kwargs.get('divide', False)

        self.operators = [self.add, self.subtract, self.multiply, self.divide]
        
        # check if parameters have been provided
        if self._is_parameters_ok():
            def calculate(x,y):
                x = int(x)
                y = int(y)
                if self.add:
                    solution = x + y
                
                if self.subtract:
                    solution = x - y     
                    
                if self.multiply:
                    solution = x * y
                
                if self.divide:
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
        
        if sum(self.operators) == 0:
            raise MissingParameterException("[Calculator] You have to set an operator")
        
        if sum(self.operators) > 1:
            raise MissingParameterException("[Calculator] You can only set one operator")
        

        return True