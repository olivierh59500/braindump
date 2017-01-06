<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Auth::routes();

Route::get('/home', 'HomeController@index');

Route::get('/notebooks', 'NotebooksController@index');
Route::post('/notebooks', 'NotebooksController@store');
Route::get('/notebooks/{notebook}/edit', 'NotebooksController@edit');
Route::patch('/notebooks/{notebook}', 'NotebooksController@update');
Route::get('/notebooks/{notebook}/delete', 'NotebooksController@delete');