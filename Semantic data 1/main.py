from durable.lang import *

with ruleset('day'):
  @when_all((m.predicate == 'is') & (m.object == 'conference'))
  def studies(c):
    c.assert_fact({ 'subject': c.m.subject, 'predicate': 'activity', 'object': 'studies' })
    
  @when_all((m.predicate == 'is') & (m.object == 'birthday'))
  def fun(c):
      c.assert_fact({ 'subject': c.m.subject, 'predicate': 'activity', 'object': 'fun' })
  
  @when_all((m.predicate == 'is') & (m.object == 'payday'))
  def shopping(c):
      c.assert_fact({ 'subject': c.m.subject, 'predicate': 'activity', 'object': 'shopping' })
  
  @when_all((m.predicate == 'is') & (m.object == 'lecture'))
  def public_speaking(c):
      c.assert_fact({ 'subject': c.m.subject, 'predicate': 'activity', 'object': 'public speaking' })
  
  @when_all((m.predicate == 'is') & (m.object == 'olympiad'))
  def sport(c):
      c.assert_fact({ 'subject': c.m.subject, 'predicate': 'activity', 'object': 'sport' })
  
  @when_all((m.predicate == 'is') & (m.object == 'weekend'))
  def rest(c):
      c.assert_fact({ 'subject': c.m.subject, 'predicate': 'activity', 'object': 'rest' })
  
  @when_all(+m.subject)
  def output(c):
      print('{0} is a good day for {1}'.format(c.m.subject, c.m.object))


assert_fact('day', { 'subject': 'Monday', 'predicate': 'is', 'object': 'conference' })
assert_fact('day', { 'subject': 'Tuesday', 'predicate': 'is', 'object': 'birthday' })
assert_fact('day', { 'subject': 'Wednesday', 'predicate': 'is', 'object': 'payday' })
assert_fact('day', { 'subject': 'Thursday', 'predicate': 'is', 'object': 'lecture' })
assert_fact('day', { 'subject': 'Friday', 'predicate': 'is', 'object': 'olympiad' })
assert_fact('day', { 'subject': 'Saturday', 'predicate': 'is', 'object': 'weekend' })
