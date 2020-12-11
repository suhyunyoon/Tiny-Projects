import React, { Component } from 'react';
import Logo from '../../resources/icon/logo.svg';
import MyName from './MyName';
import Counter from './Counter';
import './FirstApp.css';

class FirstApp extends Component {
  constructor(props) {
    super(props);
    this.state = { username: null };
  }

  componentDidMount() {
    fetch('/api/getUsername')
      .then(res => res.json())
      .then(user => this.setState({ username: user.username }));
  }

  render() {
	return (
	  <div className="App">
      	<header className="App-header">
          <Logo className="App-logo" alt="logo" />  
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>**********</code> and save to reload.
	    </p>
		<br/>
		<div>
        {this.state.username ? (
          <h1>Hello {this.state.username}</h1>
        ) : (
          <h1>Loading.. please wait!</h1>
        )}
		</div>
		<MyName name="리액트"/>
		<Counter />
      </div>	  
    );
  }
}

export default FirstApp;

// 1. componentDidMount(){
// 	Ajax 등등, DOM의 속성을 읽거나 직접 변경
// }
//
// 2. static getDerivedStateFromProps(nextProps, prevState){
// 	props의 값 -> state의 값
// 	if(nextProps.value !== prevState.value){
// 		return { value: nextProps.value };
// 	}
// 	return null;
// }
// 
// 3. shouldComponentUpdate(nextProps, nextState) {
// 	return this.props.props.checked !== nextProps.checked;
// 	false는 업데이트가 필요 없을 때, true는 업데이트
// 
// 4. getSnapshotBeforeUpdate(prevProps, prevState){
// 	if(prevState.array !== this.state.array){
// 		const {
// 			scrollTop, scrollHeight
// 		} = this.list;
//		componentDidMount에서 snapshot값으로 받음
// 		return { scrollTop, scrollHeight};
// 	}
// }
//
// 5. componentDidUpdate(prevProps, prevState, snapshot){
// 	이 시점에서 this.props와 this.state가 바뀌어 있음
// 	if (snapshot) {
// 		const {scrollTop } = this.list;
// 		if (scrollTop !== snapshot.scrollTop) return; // 이미 구현되어 있을 경우
// 		const diff = this.list.scrollHeight - snapshot.scrollHeight;
// 		this.list.scrollTop += diff;
// 	}
// }
//
// 6. componentWillUnmount(){
// 	이벤트, setTimeout, 외부 라이브러리 인스턴스 제거
// 	컴포넌트 제거
// }
//
