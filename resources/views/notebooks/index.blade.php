@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row">
        <div class="col-md-8 col-md-offset-2">
            <div class="panel panel-default">
                <div class="panel-heading">Notebooks</div>

                <div class="panel-body">

                    <ul class="list-group">
                    @foreach ($notebooks as $notebook)
                    <li class="list-group-item">
                        {{ $notebook->title }}
                    </li>
                    @endforeach
                    </ul>
                    
                    <form method="POST" action="/notebooks">
                        <input type="hidden" name="_token" value="{{ csrf_token() }}">
                        <div class="form-group">
                            <input type="text" name="title" class="form-control" placeholder="Notebook Title"></input>
                        </div>

                        <div class="form-group">
                            <button type="submit" class="btn btn-success">Add New Notebook</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection