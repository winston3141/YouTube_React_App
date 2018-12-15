import React from 'react';

const NavBarItem = ({video, onVideoSelect}) => {

	const imageUrl = video.snippet.thumbnails.default.url;

	return (
		<li onClick={() => onVideoSelect(video)} className="nav-bar-item">
			<div className="video-list media">
				<div className="media-left">
					<img className="media-object" src={imageUrl}/>
				</div>
				<div className="media-body">
					<div className="media-heading">{video.snippet.title}</div>
				</div>
			</div>
		</li>
	);
};

export default NavBarItem;