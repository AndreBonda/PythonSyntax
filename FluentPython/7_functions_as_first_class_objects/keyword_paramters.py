def tag(name, *content, class_=None, **attrs):
    """Generates one or more tag HTML"""

    if class_:
        attrs['class'] = class_
    
    attr_pairs = (f' {attr}="{value}"' for attr, value in sorted(attrs.items()))

    attr_str = ''.join(attr_pairs)

    if content:
        elements = (f'<{name}{attr_str}>{c}<{name}/>' for c in content)
        return '\n'.join(elements)
    else:
        return f'<{name}{attr_str}/>'


br = tag('br')
print(br) # <br/>

# any argument after the first are captured by *content as a tuple
p = tag('p', 'hello')
print(p) # <p>hello</p>

p = tag('p', 'hello', 'world')
print(p)
# <p>hello<p/>
# <p>world<p/>

# keyword arguments that aren't explicity named in the method signature are 'caputered' by
# default **attrs as dict (id in this case) 
p = tag('p', 'hello', id=33)
print(p)

# class_ is a keyword-only argument. It will never capture unnamed positional arguments
p = tag('p', 'hello', 'world', class_='sidebar')
print(p)
# <p class="sidebar">hello<p/>
# <p class="sidebar">world<p/>

img = tag(content='testing', name='img')
print(img) # <img content="testing"/>

my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg',
          'class': 'framed'}
img = tag(**my_tag)
print(img) # <img class="framed" src="sunset.jpg" title="Sunset Boulevard"/>