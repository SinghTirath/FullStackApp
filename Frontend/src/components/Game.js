import React from 'react';

const Game = (props) => {
    return (
        <tr>
            <td>{props.game.title}</td>
            <td>{props.game.genre}</td>
            <td>{props.game.played.toString()}</td>
            <td>
                <div class="btn-group">
                    <button type="button" class="btn btn-danger" onClick={(e) => props.handleDelete(e,props.id)}>Delete</button>
                </div>
            </td>
        </tr>
    );
};

export default Game;
