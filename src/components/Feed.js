import { h, Component } from 'preact';
import { connect } from 'preact-redux';

import { bindActions } from './../util';
import reduce from './../reducers';
import * as actions from './../actions';

import command from './../utils/command';
import Item from './Item';

@connect(reduce, bindActions(actions))
export default class Feed extends Component {
  
  shouldComponentUpdate({ images }) {
    return images !== this.props.images;
  }

  selectImage = (image) => {
    this.props.setSelected(image);
  }

  render({ images }) {
    return (
      <div id="feed">
        {(images.length < 1) ? (
          <main>
            <div className="container">
              <p>Post pictures of your pebbles!</p>
              {('serviceWorker' in navigator) ? (<p />) : (
                <p>Sadly your browser does not support this functionality yet.</p>
              )}
            </div>
          </main>
        ) : images.map(image => (
          <Item key={image.id} image={image} onSelect={this.selectImage} />
        ))}
      </div>
    );
  }
}