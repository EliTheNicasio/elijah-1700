from h2o_wave import Q, main, app, ui

textToAnalyze = ''

@app('/')
async def serve(q: Q):
    global textToAnalyze
    
    if q.args.analyze:
        textToAnalyze = q.args.submittedText

    # Display a form on the page
    q.page['REM'] = ui.form_card(
        box='1 1 2 4',
        items=[
            ui.text_xl('Enter text to analyze'),
            ui.textbox(name='submittedText', label=''),
            ui.button(name='analyze', label='Analyze'),
            ui.text_xl(textToAnalyze),
        ],
    )
    
    # Save the page
    await q.page.save()
