/********************************************************************************
** Form generated from reading UI file 'test_loginKkmUXW.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef TEST_LOGINKKMUXW_H
#define TEST_LOGINKKMUXW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDialog>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTextEdit>

QT_BEGIN_NAMESPACE

class Ui_Login
{
public:
    QPushButton *login_btn;
    QTextEdit *userid;
    QComboBox *combo_02;
    QTextEdit *psswd;
    QComboBox *combo_01;

    void setupUi(QDialog *Login)
    {
        if (Login->objectName().isEmpty())
            Login->setObjectName(QString::fromUtf8("Login"));
        Login->resize(623, 623);
        Login->setMinimumSize(QSize(623, 623));
        Login->setMaximumSize(QSize(623, 623));
        Login->setLayoutDirection(Qt::RightToLeft);
        Login->setStyleSheet(QString::fromUtf8(""));
        login_btn = new QPushButton(Login);
        login_btn->setObjectName(QString::fromUtf8("login_btn"));
        login_btn->setGeometry(QRect(92, 490, 443, 71));
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(login_btn->sizePolicy().hasHeightForWidth());
        login_btn->setSizePolicy(sizePolicy);
        login_btn->setMinimumSize(QSize(443, 71));
        login_btn->setMaximumSize(QSize(443, 71));
        QFont font;
        font.setPointSize(18);
        font.setBold(true);
        login_btn->setFont(font);
        login_btn->setLayoutDirection(Qt::LeftToRight);
        login_btn->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 0);\n"
"background-color: rgb(66, 195, 255);"));
        userid = new QTextEdit(Login);
        userid->setObjectName(QString::fromUtf8("userid"));
        userid->setGeometry(QRect(330, 282, 181, 31));
        sizePolicy.setHeightForWidth(userid->sizePolicy().hasHeightForWidth());
        userid->setSizePolicy(sizePolicy);
        userid->setMinimumSize(QSize(181, 31));
        userid->setMaximumSize(QSize(181, 31));
        userid->setLayoutDirection(Qt::LeftToRight);
        combo_02 = new QComboBox(Login);
        combo_02->addItem(QString());
        combo_02->addItem(QString());
        combo_02->setObjectName(QString::fromUtf8("combo_02"));
        combo_02->setGeometry(QRect(330, 427, 181, 31));
        sizePolicy.setHeightForWidth(combo_02->sizePolicy().hasHeightForWidth());
        combo_02->setSizePolicy(sizePolicy);
        combo_02->setMinimumSize(QSize(181, 31));
        combo_02->setMaximumSize(QSize(181, 31));
        combo_02->setLayoutDirection(Qt::LeftToRight);
        psswd = new QTextEdit(Login);
        psswd->setObjectName(QString::fromUtf8("psswd"));
        psswd->setGeometry(QRect(330, 357, 181, 31));
        sizePolicy.setHeightForWidth(psswd->sizePolicy().hasHeightForWidth());
        psswd->setSizePolicy(sizePolicy);
        psswd->setMinimumSize(QSize(181, 31));
        psswd->setMaximumSize(QSize(181, 31));
        psswd->setLayoutDirection(Qt::LeftToRight);
        combo_01 = new QComboBox(Login);
        combo_01->addItem(QString());
        combo_01->addItem(QString());
        combo_01->setObjectName(QString::fromUtf8("combo_01"));
        combo_01->setGeometry(QRect(330, 212, 181, 31));
        sizePolicy.setHeightForWidth(combo_01->sizePolicy().hasHeightForWidth());
        combo_01->setSizePolicy(sizePolicy);
        combo_01->setMinimumSize(QSize(181, 31));
        combo_01->setMaximumSize(QSize(181, 31));
        combo_01->setLayoutDirection(Qt::LeftToRight);

        retranslateUi(Login);

        QMetaObject::connectSlotsByName(Login);
    } // setupUi

    void retranslateUi(QDialog *Login)
    {
        Login->setWindowTitle(QCoreApplication::translate("Login", "\353\241\234\352\267\270\354\235\270", nullptr));
        login_btn->setText(QCoreApplication::translate("Login", "LOGIN", nullptr));
        userid->setPlaceholderText(QCoreApplication::translate("Login", "user id", nullptr));
        combo_02->setItemText(0, QCoreApplication::translate("Login", "LANGUAGE", nullptr));
        combo_02->setItemText(1, QCoreApplication::translate("Login", "\355\225\234\352\265\255\354\226\264", nullptr));

        psswd->setPlaceholderText(QCoreApplication::translate("Login", "password", nullptr));
        combo_01->setItemText(0, QCoreApplication::translate("Login", "COMPANY", nullptr));
        combo_01->setItemText(1, QCoreApplication::translate("Login", "\353\263\270\354\202\254", nullptr));

    } // retranslateUi

};

namespace Ui {
    class Login: public Ui_Login {};
} // namespace Ui

QT_END_NAMESPACE

#endif // TEST_LOGINKKMUXW_H
