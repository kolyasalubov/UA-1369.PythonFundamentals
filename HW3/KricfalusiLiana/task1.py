def process_text(Zen_Of):
    upper_text = Zen_Of.upper()
    better_count = Zen_Of_lower.count('better')
    never_count = Zen_Of_lower.count('never')
    is_count = Zen_Of_lower.count ('is')

    print("Count 'better':" , better_count)
    print("Count 'never':" , never_count)
    print("Count 'is':" , is_count)

    print ("\nZen_Of in uppercase:")
    print(text.upper())
    
    replaced_text = text.replaced("i" , "&")

input_text = """
 Zen of Python
 Beautiful is better than ugly.
 Explicit is better than implicit.
 Simple is better than complex.
 Complex is better than complicated.
 Flat is better than nested.
 Sparse is better than dense.
 Readability counts.
 Special cases aren't special enough to break the rules.
 Although practicality beats purity.
 Errors should never pass silently.
 Unless explicitly silenced.
 In the face of ambiguity, refuse the temptation to guess.
 There should be one-- and preferably only one --obvious way to do it.
 Although that way may not be obvious at first unless you're Dutch.
 Now is better than never.
 Although never is often better than *right* now.
 If the implementation is hard to explain, it's a bad idea.
 If the implementation is easy to explain, it may be a good idea.
 Namespaces are one honking great idea -- let's do more of those!

 """
process_text(input_text)




