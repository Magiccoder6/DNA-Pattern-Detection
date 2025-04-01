class DNA:
    def __init__(self, sequence):
        self.sequence = sequence.upper()  # Ensure uppercase for consistency
        self.original_sequence = sequence.upper()
        self.current_state = "Q0"
    
    def _find_start_codon(self):
        transitions = {
            'Q0': {'Q1':'A', 'DS0': ['T', 'G', 'C']},
            'Q1': {'Q2':'T', 'DS0': ['A', 'G', 'C']},
            'Q2': {'Q3':'G', 'DS0': ['A', 'T', 'C']},
            'DS0': {'DS0': ['A','T', 'G', 'C']},
            'Q3': {}
        }
        
        return self._process_sequence(transitions)
    
    def _find_huntington_disease(self):
        self.sequence = self.original_sequence
        transitions = {
            'Q3' : {'Q4':'C', 'Q3': ['T', 'A']},
            'Q4' : {'Q5': 'A', 'Q3': ['T','G','C']},
            'Q5' : {'Q6': 'G', 'Q3': ['A','T','C']},
            'Q6' : {'Q13': 'C', 'Q3': ['A','T','G']},
            'Q13' : {'Q14': 'A', 'Q3': ['T','G','C']},
            'Q14' : {'Q15': 'G', 'Q3': ['A','T','C']},
            'Q15' : {'Q16': 'C', 'Q3': ['A','T','G']},
            'Q16' : {'Q17': 'A', 'Q3': ['T','G','C']},
            'Q17' : {'Q12': 'G', 'Q3': ['A','T','C']},
            'Q12' : {}
        }
        
        found = self._process_sequence(transitions)
        if(not found):
            self.current_state = 'Q3'

        return found
    
    def _find_cancer_mutation(self):
        
        transitions = {
            'Q3' : {'Q7':'G', 'Q3': ['A','T']},
            'Q7' : {'Q8': 'G', 'Q3': ['A','T','C']},
            'Q8' : {'Q8': 'G', 'Q9':'T', 'Q3': ['A','C']},
            'Q9' : {'Q10': 'G', 'Q3': ['T','C','A']},
            'Q10' : {'Q11': 'A', 'Q3': ['T','G','C']},
            'Q11' : {'Q12': 'T', 'Q3': ['A','G','C']},
            'Q12' : {}
        }

        found = self._process_sequence(transitions)
        
        if(not found):
            self.current_state = 'Q3'

        return found

    def _process_sequence(self, transitions):
        index = 0
        for char in self.sequence:
            index +=1
            dict = transitions[self.current_state]

            next_state = None
            for key, value in dict.items():
                if value == char or (isinstance(value, list) and char in value):
                    next_state = key
                    break

            if(next_state):
                self.current_state = next_state

            print(next_state)
            if(not next_state):
                self.sequence = self.sequence[index-1:]
                break
        
        
        if(transitions[self.current_state]):
            return False
        
        return True
    
    def analyze(self):
        self.current_state = 'Q0'

        if(not self._find_start_codon()):
            return "Start codon (ATG) not found.", False
        
        if(self._find_cancer_mutation()):
            return "Possible cancer mutation (GGTGAT) found.", True
        '''elif(self._find_huntington_disease()):
            return "Huntington's disease gene (CAG)^3 found", True'''
        
        
        return "No significant patterns found", True

        

