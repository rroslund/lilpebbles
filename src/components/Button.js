import { h, Component } from 'preact';
import { connect } from 'preact-redux';

import { bindActions } from './../util';
import reduce from './../reducers';
import * as actions from './../actions';
import command from './../utils/command';

@connect(reduce, bindActions(actions))
export default class Button extends Component {

  shouldComponentUpdate({ modal, network }) {
    return modal !== this.props.modal || network !== this.props.network;
  }

  toggleModal = () => {
    this.props.setModal(!this.props.modal);
  };
  refresh = (e) =>{
    e.preventDefault();
    if ('serviceWorker' in navigator) {
      command({ command: 'refresh' })
      .then((response) => {
        var button = this;
        console.log(response);
        Object.keys(response.data).forEach(function(img){
          button.props.addImage(response.data[img].small);  
        })
        //this.props.setRefreshed(!this.props.refreshed);
      });
    } else {
      this.props.setRefreshed(!this.props.refreshed);
    }
  }
  handleChange = (e) =>{
    e.preventDefault();
    if ('serviceWorker' in navigator) {
      command({ command: 'addimg', file: e.target.files[0] })
      .then((response) => {
        console.log(this);
        this.props.addImage(response.data.small);
      });
    } else {
      this.props.addImage(response.data.small);
    }
  }
  render({ modal, network }) {
    const style = {
      transform: modal || !network ? 'scale3d(0, 0, 0)' : 'scale3d(1, 1, 1)',
    };
    return (
      <div>
        <div style="position:absolute;right:10%;top:84%;width:56px;height:56px;">
          <form action="" onSubmit={this.handleSubmit}>
            
          <label id="labelForPicker" class="picker" for="filepicker" tabindex="1" aria-label="Choose a photo">
            <svg fill="#FFFFFF" height="55" viewBox="0 0 24 24" width="24">
              <path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z" />
              <path d="M0 0h24v24H0z" fill="none" />
            </svg>
            </label>
            <input id="filepicker" style="display:none;width:0px;" type="file" accept="image/*;capture=camera" onChange={this.handleChange}/>
          </form>
        </div>

        <div style="position:absolute;left:10%;top:84%;width:56px;height:56px;">
          <form action="" onSubmit={this.handleSubmit}>
            
          <label id="labelForRefresh" class="picker" for="refresh" tabindex="1" aria-label="Refresh">
            <span class="refresh fa-stack fa-lg">
              <i class="fa fa-refresh fa-stack-1x fa-inverse"></i>
            </span>
            </label>
            <button type="button" id="refresh" style="display:none;width:0px;" onClick={this.refresh}/>
          </form>
        </div>
      </div>
    );
  }
}