import os
import asyncio
from metaapi_cloud_sdk import MetaApi
from datetime import datetime, timedelta

# Note: for information on how to use this example code please read https://metaapi.cloud/docs/client/usingCodeExamples

token = os.getenv('TOKEN') or 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI3ZDlhMDcxYTRmMGM5YzI4NTdhM2RmNjJmYjFiZjUxOCIsInBlcm1pc3Npb25zIjpbXSwiYWNjZXNzUnVsZXMiOlt7ImlkIjoidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJ0cmFkaW5nLWFjY291bnQtbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6MmJmMTljZjAtMDRhOC00N2I3LTkwOGQtZmU0ODVjNDE0ODZlIl19LHsiaWQiOiJtZXRhYXBpLXJlc3QtYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDoyYmYxOWNmMC0wNGE4LTQ3YjctOTA4ZC1mZTQ4NWM0MTQ4NmUiXX0seyJpZCI6Im1ldGFhcGktcnBjLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOjJiZjE5Y2YwLTA0YTgtNDdiNy05MDhkLWZlNDg1YzQxNDg2ZSJdfSx7ImlkIjoibWV0YWFwaS1yZWFsLXRpbWUtc3RyZWFtaW5nLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOjJiZjE5Y2YwLTA0YTgtNDdiNy05MDhkLWZlNDg1YzQxNDg2ZSJdfSx7ImlkIjoibWV0YXN0YXRzLWFwaSIsIm1ldGhvZHMiOlsibWV0YXN0YXRzLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDoyYmYxOWNmMC0wNGE4LTQ3YjctOTA4ZC1mZTQ4NWM0MTQ4NmUiXX0seyJpZCI6InJpc2stbWFuYWdlbWVudC1hcGkiLCJtZXRob2RzIjpbInJpc2stbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6MmJmMTljZjAtMDRhOC00N2I3LTkwOGQtZmU0ODVjNDE0ODZlIl19XSwidG9rZW5JZCI6IjIwMjEwMjEzIiwiaW1wZXJzb25hdGVkIjpmYWxzZSwicmVhbFVzZXJJZCI6IjdkOWEwNzFhNGYwYzljMjg1N2EzZGY2MmZiMWJmNTE4IiwiaWF0IjoxNzIyOTYyNDQ0LCJleHAiOjE3MzA3Mzg0NDR9.dPbZNN6ZIzJW_ce4TzYihZjjZ42LucopoqmMBW2K4lIwCFgxsKhX4e05OcFMfrLJSnrmcvtviK9b232Ww1Kj0WZjIAO5Efj_Ay8GFML3ZtLt0tg47qDdi-fHZCEeZ5R5yz60CM-yzhwCZvvrFS03fQ9PXRKbDxMGsn_D7HrFVi11lczG9ZptNNdSWZLLny8YvmdGGVdkwDlnqaFEEQu25vNxS3qe56t4hV6B-KcgirH2c8YBl6ydbIEXqWfgtJl25nz5Ro85830HlHHr1MpMAayT4PUt8tUS0fq-CHzO_yT1YRX8yRbmxJc6dubhwzBeIZWnduMA0ILgeM9URO1XoC91G4d40KlvRwwNw_nDlbrxSqoW1vBo1X0WJBWncqXKFD0SFC7tls_jP8MTQgrIHVFFC7ilnu1vny7DpkECFDgt1i1cwRuv2_9maOAtQjFmj3NiZnpdPNxELNzymIxmCpKrWt77NRZg3a9SQRCKXuyRDEe2966fuOQC156UF-mepFutjULmsLuTuVoWd2AzbgVYEUwjW05NYlRRKcEiSrtXyHSgfVJYpB3YTX6gKKZKdSFLdhS0WZ87xjCp-iqrMSYHhMNuS6UAyP5nikhOVSvfwnXOKAlNVE72ui7S137V7Ns2ujTnBppof7zbPvvE3ejWBoAcNdVLGaZdPgz-b-4'

accountId = os.getenv('ACCOUNT_ID') or '2bf19cf0-04a8-47b7-908d-fe485c41486e'


async def test_meta_api_synchronization(type):
    api = MetaApi(token)
    try:
        account = await api.metatrader_account_api.get_account(accountId)
        initial_state = account.state
        deployed_states = ['DEPLOYING', 'DEPLOYED']

        if initial_state not in deployed_states:
            #  wait until account is deployed and connected to broker
            print('Deploying account')
            await account.deploy()

        print('Waiting for API server to connect to broker (may take couple of minutes)')
        await account.wait_connected()

        # connect to MetaApi API
        connection = account.get_rpc_connection()
        await connection.connect()

        # wait until terminal state synchronized to the local state
        print('Waiting for SDK to synchronize to terminal state (may take some time depending on your history size)')
        await connection.wait_synchronized()

        # invoke RPC API (replace ticket numbers with actual ticket numbers which exist in your MT account)
        # print('Testing MetaAPI RPC API')
        # print('account information:', await connection.get_account_information())
        # print('positions:', await connection.get_positions())
        # # print(await connection.get_position('1234567'))
        # print('open orders:', await connection.get_orders())
        # # print(await connection.get_order('1234567'))
        # print('history orders by ticket:', await connection.get_history_orders_by_ticket('1234567'))
        # print('history orders by position:', await connection.get_history_orders_by_position('1234567'))
        # print(
        #     'history orders (~last 3 months):',
        #     await connection.get_history_orders_by_time_range(
        #         datetime.utcnow() - timedelta(days=90), datetime.utcnow()
        #     ),
        # )
        # print('history deals by ticket:', await connection.get_deals_by_ticket('1234567'))
        # print('history deals by position:', await connection.get_deals_by_position('1234567'))
        # print(
        #     'history deals (~last 3 months):',
        #     await connection.get_deals_by_time_range(datetime.utcnow() - timedelta(days=90), datetime.utcnow()),
        # )
        # print('server time', await connection.get_server_time())

        # # calculate margin required for trade
        # print(
        #     'margin required for trade',
        #     await connection.calculate_margin(
        #         {'symbol': 'GBPUSD', 'type': 'ORDER_TYPE_BUY', 'volume': 0.1, 'openPrice': 1.1}
        #     ),
        # )

        # trade
        print('Submitting pending order')

        if(type=='buy'):
            print(await connection.create_market_buy_order(symbol='USOIL', volume=20, stop_loss=0, take_profit=0,options={'comment': 'comment','clientId': 'TE_GBPUSD_7hyINWqAl'}))
        if (type == 'sell'):
            print(await connection.create_market_sell_order(symbol='USOIL', volume=20, stop_loss=0, take_profit=0,options={'comment': 'comment','clientId': 'TE_GBPUSD_7hyINWqAl'}))
        if (type == 'close'):
            print(await connection.close_positions_by_symbol(symbol='USOIL'))

        # except Exception as err:
        #     print('Trade failed with error:')
        #     print(api.format_error(err))
        if initial_state not in deployed_states:
            # undeploy account if it was undeployed
            print('Undeploying account')
            await connection.close()
            await account.undeploy()

    except Exception as err:
        print(api.format_error(err), "HELLO")
    # exit()

# asyncio.run(test_meta_api_synchronization('buy'))

