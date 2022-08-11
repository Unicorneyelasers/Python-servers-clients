#!/usr/bin/python3

import asyncio
import sys
import traceback
import subprocess

BUF_SIZE = 1024
PORT = 12345

async def echo(reader, writer):
    
    try:
          
        received = await reader.readline()
        print(received)
        command = received.decode('utf-8')
        command = command.strip()
        
        print(f'{command}')

    except Exception as detail:
        print(detail,traceback.format_exc())

    if(received):
        try:   
            with open("commands.conf", 'r') as f:             
                for line in f:
                    if not line:
                        break
                    substr = line.strip().split('\t')
                    if command in substr:
                        print("nailed it")
                        
                        sub = substr[1:]
                        print(sub)
                        output = subprocess.check_output([sub], encoding='utf-8')
                        print(output)
                        #sub = command.encode('utf-8')
                        writer.write(output)
                        await writer.drain() # waits until the data is written
                        break

        except Exception as detail:
            print(detail,traceback.format_exc())

    writer.close()
    await writer.wait_closed()


async def main():
    try:
        server = await asyncio.start_server(echo, '::', PORT)
    except Exception as detail:
         print(detail,traceback.format_exc())
     #server = await asyncio.start_server(echo, '127.0.0.1', 12345)
    await server.serve_forever() # without this, program terminates
asyncio.run(main())