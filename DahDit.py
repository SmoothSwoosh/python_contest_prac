class morse:
    def __init__(self, params=[]):
        first, last, dash, sep = 'di', 'dit', 'dah', ''
        if not params or (' ' in params and params[-1] != ' '):
            sep = '.'
        if ' ' in params:
            params = params.split()
            self.regime = 'words'
        elif not params:
            self.regime = 'words'
        else:
            params = list(params)
            self.regime = 'chars'
                                     
        match len(params):
            case 1:
                first, last, dash, sep = params[0]
            case 2:
                first, last, dash = params[0], params[0], params[1]
            case 3:
                first, last, dash = params
            case 4:
                first, last, dash, sep = params

        self.first, self.last, self.dash, self.sep = first, last, dash, sep
        self.str = ''

    def __pos__(self):
        self.str = '+' + self.str
        return self

    def __neg__(self):
        self.str = '-' + self.str
        return self

    def __invert__(self):
        self.str = '~' + self.str
        return self

    def __str__(self):
        repr = ''
        str = self.str
        for i in range(len(str)):
            if str[i] == '-':
                repr += self.dash
                if i + 1 < len(str) and str[i + 1] != '~':
                    if self.regime == 'words':
                        repr += ' '
            elif str[i] == '~':
                if self.regime == 'words':
                    repr += ', '
                else:
                    repr += ' '
            else:
                if i == 0 or (i + 1 < len(str) and str[i + 1] != '~'):
                    repr += self.first
                    if self.regime == 'words':
                        repr += ' '
                else:
                    repr += self.last

        repr += self.sep
        return repr
