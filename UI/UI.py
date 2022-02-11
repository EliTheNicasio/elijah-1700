from h2o_wave import Q, main, app, ui

bean_count = 0

@app('/counter')
async def serve(q: Q):
    global bean_count
    # Was the 'increment' button clicked?
    if q.args.increment:
        bean_count += 1

    # Display a form on the page
    q.page['beans'] = ui.form_card(
        box='1 1 1 2',
        items=[
            ui.text_xl('Beans!'),
            ui.button(name='increment', label=f'{bean_count} beans'),
        ],
    )
    
    # Save the page
    await q.page.save()
