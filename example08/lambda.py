print (list(filter(lambda s: s and len(s.strip())>0, ['test', None, '', 'str', '  ', 'END'])))
