import argparse
import asyncio
import multiprocessing
import os.path
import threading
import time
import aiohttp
import requests


# list_url = ['https://media.geeksforgeeks.org/wp-content/uploads/20230426115225/computer-image.jpg',
#             'https://c1.wallpaperflare.com/preview/427/745/192/notebook-natural-laptop-macbook.jpg',
#             'https://www.pngmart.com/files/21/Internet-Of-Things-PNG-Transparent.png']


def download_image(url):
    """Функция скачивания изображений по URL-адресу"""
    if not os.path.exists('downloaded_images'):
        os.mkdir('downloaded_images')
    start_time = time.time()
    filename = url.split('/')[-1]
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(f'downloaded_images/{filename}', 'wb') as file:
            file.write(resp.content)
    print(f'Время скачивания изображения({filename}): {time.time() - start_time:.2f} сек.')


async def download_image_async(url):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = url.split('/')[-1]
    with open(filename, "w", encoding='utf-8') as f:
        f.write(text)
        print(f'Время скачивания изображения({filename}): {time.time() - start_time:.2f} сек.')


async def download_asyncio(list_url):
    """Асинхронный подход"""
    start_time = time.time()
    tasks = []
    for url in list_url:
        task = asyncio.create_task(download_image_async(url))
        tasks.append(task)

    await asyncio.gather(*tasks)

    print(f'(async) Время скачивания изображения: {time.time() - start_time:.2f} сек.')


def download_threading(list_url):
    start_point = time.time()
    threads = []
    for url in list_url:
        thread = threading.Thread(target=download_image, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        print('(threading) ', end='')
        thread.join()
    print(f'Итоговое время работы программы (многопоточный подход): {round(time.time() - start_point, 2)} сек.\n')


def download_multiproccessing(list_url):
    processes = []
    start_point = time.time()
    for url in list_url:
        process = multiprocessing.Process(target=download_image, args=(url,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()
    print(f'Итоговое время работы программы (многопроцессорный подход): {round(time.time() - start_point, 2)} сек.\n')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Download images from URLs and save them to disk.")
    parser.add_argument("--list_url", nargs="+", default='https://photo.brestcity.com/2021/05/404.jpg',
                        help="A list of URLs to download images from.")
    args = parser.parse_args()

    list_url = args.list_url

    start_point = time.time()

    for url in list_url:
        download_image(url)
        print(f'Итоговое время работы программы (синхронный подход): {round(time.time() - start_point, 2)} сек.\n')

    download_threading(list_url)

    download_multiproccessing(list_url)

    asyncio.run(download_asyncio(list_url))
