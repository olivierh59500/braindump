@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row">
        <div class="col-md-8 col-md-offset-2">
            <div class="panel panel-default">
                <div class="panel-heading">Edit Notebook</div>

                <div class="panel-body">
                    
                    <form method="POST" action="/notebooks/{{ $notebook->id }}">

                        {{ method_field('PATCH') }}
                        
                        <input type="hidden" name="_token" value="{{ csrf_token() }}">
                        <div class="form-group">
                            <input type="text" name="title" class="form-control" value="{{ $notebook->title }}"></input>
                        </div>

                        <div class="form-group">
                            <button type="submit" class="btn btn-success">Update Notebook</button>
                        </div>
                    </form>
                    
                </div>
            </div>
        </div>
    </div>
</div>
@endsection