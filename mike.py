@site.route('/profile')
@login_required
def profile():
    form = newMusicForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            namedata = form.name.data
            genredata = form.genre.data
            banddata = form.band.data
            playlistdata = form.playlist.data
            print(namedata, banddata)

            new_Music = Music(namedata, genredata, banddata, playlistdata)

            db.session.add(new_Music)
            db.session.commit()

            flash(
                f'You have successfully added the Music {namedata} to your database.')

            return redirect(url_for('site.profile'))
    except:
        flash(f'Invaild form input try again')
        return redirect(url_for('site.profile'))
    return render_template('profile.html', form=form)