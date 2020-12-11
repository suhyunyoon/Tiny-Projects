import React, { Component } from 'react';

const Problematic = () => {
	throw (new Error('버그발생!'));
	return (
		<div></div>
	);
};
class Counter extends Component {
	state = {
		number: 0,
		error: false
	}

	// 생성자
	constructor(props){
		super(props);
		console.log("생성자");
	}
	
	// 화면에 나타난 후 호출, 외부 라이브러리, Ajax, DOM에 관련 된 작업
	componentDidMount() {
		console.log('componentDidMount');
	}

	// props로 받아온 값을 state로 동기화 하는 작업
	static getDerivedStateFromProps(nextProps, prevState) {
		console.log('getDerivedStateFromProps');
		return null;
	}

	// 언제 컴포넌트를 업데이트하는 지 결정
	shouldComponentUpdate(nextProps, nextState){
		console.log('shouldComponentUpdate');
		if (nextState.number % 5 === 0) return false;
		return true;
	}

	// shouldComponentUpdate의 반환값이 true이고 render직후 호출, DOM의 직전 상태를 가져오고 componentDidUpdate의 3번째 파라미터를 리턴
	getSnapshotBeforeUpdate(prevProps, prevState){
		return null;
	}

	// render 호출 후 발생, 이 시점에는 this.props와 this.state가 바뀌어 있음 
	componentDidUpdate(prevProps, prevState, snapshot){
		console.log('componentDidUpdate');
	}

	// 이벤트 제거, setTimeout -> clearTimeout으로 제거, 외부 라이브러리 dispose 호출
	componentWillUnmount(){
	}

	// react catch func
	componentDidCatch(error, info){
		this.setState({
			error: true
		});
	}

	// When Press +
	handleIncrease = () => {
		this.setState(
			({ number }) => ({
				number: number + 1
			})
		);
	}

	// When Press -
	handleDecrease = () => {
		const { number } = this.state;
		this.setState({
			number: number - 1
		});
	}

	// Render
	render(){
		console.log('render-------------------------------------------------');
		if (this.state.error) return (<h1>에러발생!</h1>);

		return (
			<div>
				<h1>카운터</h1>
				<div>값: {this.state.number}</div>
				{ this.state.number === 4 && <Problematic /> }
				<button onClick={this.handleIncrease}>+</button>
				<button onClick={this.handleDecrease}>-</button>
			</div>
		);
	}
}

export default Counter;

