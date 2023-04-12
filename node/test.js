// require('dotenv').config();
const Web3 = require('web3');

// const prv_key = process.env.PRV_KEY
// const prv_key2 = process.env.PRV_KEY2

/*


var nonce;
var contract;
var alice = wb3.eth.accounts.privateKeyToAccount(prv_key);

const processTx = async(hash) => {
  var ret = await validateTx(hash);
  if (ret.status) {
    console.log(hash)
    frontRun(hash, nonce++);
  }
}

const init = async() => {
  await wb3.eth.accounts.wallet.add(alice);
  nonce = await wb3.eth.getTransactionCount(alice.address, 'latest');

  const { Uniswapv2ABI } = require('./const');
  contract = new wb3.eth.Contract(Uniswapv2ABI, "0x10ED43C718714eb63d5aA57B78B54704E256024E");
}

const validateTx = async(hash) => {
	var tx = await wb3.eth.getTransaction(hash);
  if (tx.from == alice.address) return {status: false, code:0};
	if (tx.to != "0x10ED43C718714eb63d5aA57B78B54704E256024E") return {status: false, code:1};
  var data = tx.input;
  var func = data.substr(0, 10);
  if (func != '0x7ff36ab5') return {status: false, code:2};
  data = data.substr(266); // 10 + 64*4
  var pathLen = Number(data.substr(0, 64));
  for (var x=0; x<pathLen-1; x++) {
    var path1 = '0x' + data.substr(64*(x+1) + 24, 40);
    var path2 = '0x' + data.substr(64*(x+2) + 24, 40);
    if (path1 == '0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c' && path2 == '0xfe9803c5775a7311da5a60bbc3a60946dc335a28') return {status: true, gas: Number(tx.gas), gasPrice: Number(tx.gasPrice)};
  }
  return {status: false, code:3};
}

const frontRun = async(detect, nonce) => {
  var ret = await contract.methods.swapExactETHForTokens(0, ['0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c', '0xfE9803C5775a7311dA5a60BbC3a60946Dc335A28'], alice.address, '99999999999').send({from: alice.address, value:'100000000', gasPrice: '6000000000', gas: '160842', nonce: nonce});
  console.log(detect, ret.transactionHash)
}
*/
const wb3 = new Web3(new Web3.providers.WebsocketProvider('wss://bsc-mainnet.nodereal.io/ws/v1/1f70e06dce7c42ac916e2236a34b89fc'));
// const wb3 = new Web3(new Web3.providers.WebsocketProvider('wss://bsc-mainnet.nodereal.io/ws/v1/58e77623029c44f19e710581ef96915d'));

const run = async () => {
  // await init();

  wb3.eth.subscribe('pendingTransactions', (error, txHash) => {
    if (error) {
      console.error(error);
    } else {
      var currentDateTime = new Date();
      var resultInSeconds=currentDateTime.getTime() / 1000;
      console.log(txHash)
      console.log(resultInSeconds)
      // console.log(`New unconfirmed transaction: ${txHash}`);
      // processTx(txHash);
    }
  });
}

run()