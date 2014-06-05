from collections import namedtuple

Category = namedtuple('Category',
                      'fps sps tps fpp spp tpp')

Category.__doc__ = """Grammatical category - encompasses person, number, gender
		      fp = first person, sp = second person, tp = third person
		      s = singular, p = plural"""
