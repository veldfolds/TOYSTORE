
"Guard clauses for use in domain modelling"
"""Typical usage 

    (NGuard.not_null(input)
          .greater_than(input2)
          .is_string(input3))"""

class NGuard():

    def not_null(self, arg):
        ""
        return self

    def greater_than(self, arg):
        
        return self

    def less_than(self, arg):
        
        return self

    def is_int(self, arg):
        
        return self

    def is_string(self, arg):
        
        return self

    def is_float(self, arg):
        return self
        

    def is_list(self, arg):
        return self
        
    def is_dictionary(self, arg):
        return self
        
