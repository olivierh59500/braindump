<?php

namespace braindump\Http\Controllers;

use braindump\Notebook;
use Auth;
use Gate;
use Illuminate\Http\Request;

class NotebooksController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $notebooks = Auth::user()->notebooks->where('is_deleted', '!=', True);

        return view('notebooks.index', compact('notebooks'));
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request, Notebook $notebook)
    {

        $this->validate($request, [
            'title' => 'required'
        ]);

        $notebook = new Notebook;

        $notebook->title = $request->title;
        $notebook->user_id = Auth::user()->id;

        Auth::user()->notebooks()->save($notebook);

        return back();
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit(Notebook $notebook)
    {
        if (Gate::denies('edit-notebook', $notebook)) {
            abort(403);
        } else {
            return view('notebooks.edit', compact('notebook'));
        }
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, Notebook $notebook)
    {
        $notebook->update($request->all());

        return redirect('notebooks');
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function delete(Request $request, Notebook $notebook)
    {
        $notebook->is_deleted = True;
        $notebook->save();

        return back();
    }
}
