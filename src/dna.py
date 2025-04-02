class DNA:
    def __init__(self, sequence):
        self.sequence = sequence.upper() + "ε"  # Ensure uppercase for consistency
        self.current_state = "Q0"
        self.start_codon_final_state = "Q3"
        self.cancer_final_state = "Q18"
        self.huntington_final_state = "Q15"

        self.transitions = {
            'Q0': {'Q1':'A', 'DS0': ['T', 'G', 'C','ε']},
            'Q1': {'Q2':'T', 'DS0': ['A', 'G', 'C','ε']},
            'Q2': {'Q3':['G','ε'], 'DS0': ['A', 'T', 'C','ε']},
            'DS0': {'DS0': ['A','T', 'G', 'C','ε']},
            'Q3': {'Q3':['A','T','ε'], 'Q4':'C', 'Q6':'G'},
            'Q4': {'Q4':'C', 'Q5':'A', 'Q3':['T','ε'], 'Q6':'G'},
            'Q5': {'Q9':'G','Q3':['T','A','C','ε']},
            'Q9': {'Q7':'G','Q10':'C','Q3':['T','A','ε']},
            'Q10': {'Q11':'A','Q3':['T','G','C','ε']},
            'Q11': {'Q12':'G','Q3':['T','A','C','ε']},
            'Q12': {'Q13':'C','Q7':'G','Q3':['T','A','ε']},
            'Q13': {'Q14':'A','Q7':'G','Q3':['T','C','ε']},
            'Q14': {'Q15':'G','Q3':['T','A','C','ε']},
            'Q15': {'Q15':'A','Q15':'T','Q15':'G','Q15':'C','Q15':'ε'},
            'Q6': {'Q4':'C','Q7':'G','Q3':['T','A','ε']},
            'Q7': {'Q4':'C','Q7':'G','Q8':'T','Q3':['A','ε']},
            'Q8': {'Q4':'C','Q16':'G','Q3':['T','A','ε']},
            'Q16': {'Q4':'C','Q17':'A','Q3':['T','G','ε']},
            'Q17': {'Q4':'C','Q18':'T','Q3':['A','G','ε']},
            'Q18': {'Q18':'A','Q18':'T','Q18':'G','Q18':'C','Q18':'ε'}
        }
    
    def _process_sequence(self, transitions):
        for char in self.sequence:
            dict = transitions[self.current_state]

            next_state = None
            for key, value in dict.items():
                if value == char or (isinstance(value, list) and char in value):
                    next_state = key
                    break

            if(next_state):
                self.current_state = next_state

    
    def analyze(self):
        self._process_sequence(self.transitions)
        print(self.current_state)

        if(self.current_state == self.cancer_final_state):
            return "Possible cancer mutation (GGTGAT) found.", True
        elif(self.current_state == self.huntington_final_state):
            return "Huntington's disease gene (CAG)^3 found", True
        
        if(self.current_state != self.start_codon_final_state):
            return "Start codon (ATG) not found.", False
        
        return "No significant patterns found", True

        

