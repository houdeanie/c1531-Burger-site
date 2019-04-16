# test.py for testing things

# storing some html code that could be useful for later
# re: iterating through a menus items
{% for item in _menu %}
    <tr>
        <td> {{ item.name}} </td>
        <td> {{ item.price }} </td>
        <td><input name='{{ item.name }}' type="number" min="0"/></td>
    </tr>
{% endfor %}
