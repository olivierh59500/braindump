<?php

namespace braindump;

use Illuminate\Database\Eloquent\Model;

class Notebook extends Model
{
    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'title'
    ];

    public function user()
    {
        return $this->belongsTo(User::class);
    }

}
