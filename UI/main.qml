import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
	visible: true
	width: 600
	height: 300
	title: "Random Quote"
	property string currTime: "00:00:00"
	property string quote: "Quote"
	property string author: "Author"
	property string source: "Source"
	property string detail: "Detail"

	// ackground
	Image {
		sourceSize.width: parent.width
		sourceSize.height: parent.height
		source: "../img/alex-perez-pEgsWN0kwbQ-unsplash.jpg"
		fillMode: Image.PreserveAspectCrop
	}
		
	// Quote
	Rectangle {
		anchors.fill: parent
		color: "transparent"
		Text {
			width: parent.width
			anchors {
				top: parent.top
				left: parent.left
				topMargin: 12
				leftMargin: 12
			}
			text: quote
			font.pixelSize: 19
			color: "white"
			wrapMode: Text.WordWrap
		}
	}

	// Details
	Rectangle {
		anchors.fill: parent
		color: "transparent"
		Text {
			anchors {
				bottom: parent.bottom
				bottomMargin: 12
				right: parent.right
				rightMargin: 12
			}
			text: detail
			font.pixelSize: 22
			color: "white"
		}
	}
}